import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Load data
print("Loading data...")
df = pd.read_csv('data_2.csv')

# Clean column names
df.columns = df.columns.str.strip()
print(f"Columns: {df.columns.tolist()}")

# Check for missing columns
required_cols = ['total_onshift_partners', 'total_busy_partners', 'total_outstanding_orders']
missing_cols = [c for c in required_cols if c not in df.columns]
if missing_cols:
    print(f"MISSING COLUMNS: {missing_cols}")
else:
    print("All required columns present.")

# --- Preprocessing ---
print("Preprocessing...")

# 1. Handle Missing Values (Simplified for robustness)
# Fill numeric NaNs with median, categorical with mode or 'Unknown'
numeric_features = ['total_items', 'subtotal', 'num_distinct_items', 'min_item_price', 
                   'max_item_price', 'total_onshift_partners', 'total_busy_partners', 
                   'total_outstanding_orders', 'estimated_store_to_consumer_driving_duration']
categorical_features = ['market_id', 'store_primary_category', 'order_protocol']

for col in numeric_features:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

for col in categorical_features:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].mode()[0])

# 2. Feature Engineering
# Convert timestamps
df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'], errors='coerce')

# Drop rows where timestamps are bad
df = df.dropna(subset=['created_at', 'actual_delivery_time'])

# Target: Delivery time in minutes
df['delivery_time_minutes'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60.0

# Time features
df['order_hour'] = df['created_at'].dt.hour
df['order_dayofweek'] = df['created_at'].dt.dayofweek

# Add new time features to numeric list for scaling
numeric_features.extend(['order_hour', 'order_dayofweek'])

# Filter outliers in target (optional but good for training stability)
df = df[(df['delivery_time_minutes'] > 0) & (df['delivery_time_minutes'] < 200)]

# Define X and y
print(f"Columns before X selection: {df.columns.tolist()}")
print(f"Numeric features: {numeric_features}")
print(f"Categorical features: {categorical_features}")
import sys; sys.stdout.flush()

missing_in_X = [c for c in numeric_features + categorical_features if c not in df.columns]
if missing_in_X:
    print(f"WARNING: The following features are missing from df and will be dropped: {missing_in_X}")
    for c in missing_in_X:
        if c in numeric_features:
            numeric_features.remove(c)
        if c in categorical_features:
            categorical_features.remove(c)

print(f"Final Numeric features: {numeric_features}")
print(f"Final Categorical features: {categorical_features}")

X = df[numeric_features + categorical_features]
y = df['delivery_time_minutes']

# 3. Build Preprocessing Pipeline
# Numeric: Standard Scaler
# Categorical: OneHotEncoder
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit preprocessor
print("Fitting preprocessor...")
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Save preprocessor
joblib.dump(preprocessor, 'preprocessor.joblib')
print("Preprocessor saved to preprocessor.joblib")

# --- Model Training ---
print("Building model...")
input_shape = X_train_processed.shape[1]

model = keras.Sequential([
    layers.Input(shape=(input_shape,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.1),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

print("Training model...")
history = model.fit(
    X_train_processed, y_train,
    validation_split=0.2,
    epochs=20,
    batch_size=128,
    verbose=1
)

# Evaluation
loss, mae = model.evaluate(X_test_processed, y_test)
print(f"Test MAE: {mae:.2f} minutes")

# Save model
model.save('model.keras')
print("Model saved to model.keras")
