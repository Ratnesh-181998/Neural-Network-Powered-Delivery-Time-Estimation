
# Ratnesh_Porter_Case_Study
# and include cell-wise code for EDA, preprocessing, Random Forest, Neural Network, and evaluation.
# It uses the uploaded dataset at /mnt/data/data_2.csv and saves the notebook to:
# /mnt/data/Ratnesh_porter_case_study.ipynb
from caas_jupyter_tools import display_dataframe_to_user
import pandas as pd
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import os

csv_path = "/mnt/data/data_2.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Dataset not found at {csv_path}")

# Preview dataset for the user
df_preview = pd.read_csv(csv_path, nrows=8)
display_dataframe_to_user("Preview of uploaded dataset (first 8 rows)", df_preview)

nb = new_notebook()
cells = []

# Title
cells.append(new_markdown_cell("# Porter Case Study — Neural Networks Regression\n\n"
    "Notebook generated from **Ratnesh_Porter_Case_Study.pdf** (converted into runnable code). "
    "Dataset: `/mnt/data/data_2.csv`.\n\n"
    "This notebook follows the PDF's methodology step-by-step: EDA → Preprocessing → Random Forest → Neural Network → Evaluation & Insights.\n---"))

# Cell 1 - Imports
cells.append(new_code_cell("""# Cell 1 - Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
%matplotlib inline
print('Libraries imported')"""))

# Cell 2 - Load data
cells.append(new_code_cell(f"""# Cell 2 - Load dataset
DATA_PATH = r'{csv_path}'
df = pd.read_csv(DATA_PATH)
print('Dataset shape:', df.shape)
df.head()"""))

# Cell 3 - Basic info and missing values
cells.append(new_code_cell("""# Cell 3 - Data info & missing values
print(df.info())
print('\\nMissing values per column:')
print(df.isnull().sum())"""))

# Cell 4 - Create target & datetime features
cells.append(new_code_cell("""# Cell 4 - Datetime conversion and target creation
# Convert timestamps to datetime (errors='coerce' will set invalid parsing to NaT)
for col in ['created_at','actual_delivery_time']:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Target: delivery_time_mins (in minutes)
if 'created_at' in df.columns and 'actual_delivery_time' in df.columns:
    df['delivery_time_mins'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60.0

# Extract time features
if 'created_at' in df.columns:
    df['order_hour'] = df['created_at'].dt.hour
    df['order_dayofweek'] = df['created_at'].dt.dayofweek
    df['order_dayname'] = df['created_at'].dt.day_name()

print('New columns:', [c for c in df.columns if c.startswith('order_') or 'delivery_time_mins' in c])
df[['created_at','actual_delivery_time','delivery_time_mins','order_hour','order_dayofweek']].head()"""))

# Cell 5 - Quick stats & describe
cells.append(new_code_cell("""# Cell 5 - Quick statistical summary (numeric)
df.select_dtypes(include=[np.number]).describe().T"""))

# Cell 6 - Handle categorical encoding and missing values (suggested by PDF)
cells.append(new_code_cell("""# Cell 6 - Categorical handling & missing value strategy
# As in the PDF, convert store_primary_category to categorical codes (keeps ordinal mapping simple)
if 'store_primary_category' in df.columns:
    df['store_primary_category_cat'] = df['store_primary_category'].astype('category').cat.codes
# For other categorical columns we will use get_dummies later (or keep as-is)
# Fill remaining missing numeric values with -1 (simple strategy used in PDF)
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
df[num_cols] = df[num_cols].fillna(-1)
# For object columns, fill with 'Missing'
obj_cols = df.select_dtypes(include=['object']).columns.tolist()
df[obj_cols] = df[obj_cols].fillna('Missing')

print('Filled missing numeric with -1 and object with \"Missing\". Sample:')\ndf.head(3)"""))

# Cell 7 - Univariate and bivariate visualizations
cells.append(new_code_cell("""# Cell 7 - EDA: distributions and relationships
plt.figure(figsize=(8,4))
if 'delivery_time_mins' in df.columns:
    sns.histplot(df['delivery_time_mins'].dropna(), bins=100, kde=True)
    plt.title('Delivery time (minutes) distribution')
    plt.show()

plt.figure(figsize=(10,4))
if 'total_items' in df.columns and 'delivery_time_mins' in df.columns:
    sns.boxplot(x='total_items', y='delivery_time_mins', data=df.sample(5000))
    plt.title('Delivery time by total_items (sample)')
    plt.show()

plt.figure(figsize=(8,4))
if 'order_hour' in df.columns and 'delivery_time_mins' in df.columns:
    sns.scatterplot(x='order_hour', y='delivery_time_mins', data=df.sample(5000), alpha=0.3)
    plt.title('Order hour vs delivery time (sample)')
    plt.show()"""))

# Cell 8 - Correlation heatmap
cells.append(new_code_cell("""# Cell 8 - Correlation matrix (numeric columns)
plt.figure(figsize=(10,8))
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, cmap='coolwarm', center=0)
plt.title('Correlation matrix (numeric)')
plt.show()"""))

# Cell 9 - Outlier detection for target and selected features (IQR)
cells.append(new_code_cell("""# Cell 9 - Outlier detection (IQR) for target & some features
def iqr_bounds(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - k*iqr, q3 + k*iqr

if 'delivery_time_mins' in df.columns:
    lower, upper = iqr_bounds(df['delivery_time_mins'].dropna())
    print('Delivery time bounds (IQR):', lower, upper)
    print('Outliers count (delivery_time):', ((df['delivery_time_mins'] < lower) | (df['delivery_time_mins'] > upper)).sum())

for col in ['total_items','num_distinct_items']:
    if col in df.columns:
        l,u = iqr_bounds(df[col].dropna())
        print(f'Col {col} IQR bounds: {l:.2f}, {u:.2f}  Outliers: {((df[col]<l)|(df[col]>u)).sum()}')"""))

# Cell 10 - Remove outliers (as per PDF: remove extreme delivery times and a few feature outliers)
cells.append(new_code_cell("""# Cell 10 - Outlier treatment (remove rows beyond bounds)
# Remove rows where delivery_time_mins is outside IQR bounds
if 'delivery_time_mins' in df.columns:
    lower, upper = iqr_bounds(df['delivery_time_mins'].dropna())
    df = df[(df['delivery_time_mins'] >= lower) & (df['delivery_time_mins'] <= upper)].copy()
    print('After removing delivery_time outliers, shape:', df.shape)

# Also remove extreme total_items / num_distinct_items if present
for col in ['total_items','num_distinct_items']:
    if col in df.columns:
        l,u = iqr_bounds(df[col].dropna())
        df = df[(df[col] >= l) & (df[col] <= u)]
print('Shape after additional outlier removals:', df.shape)"""))

# Cell 11 - Prepare features and target for modeling
cells.append(new_code_cell("""# Cell 11 - Prepare X and y\n# Drop original timestamp columns and store_id (as in PDF)
drop_cols = [c for c in ['created_at','actual_delivery_time','store_id'] if c in df.columns]\ndf_model = df.drop(columns=drop_cols)\n\n# Target\nif 'delivery_time_mins' not in df_model.columns:\n    raise ValueError('delivery_time_mins not found; check earlier cells')\n\ny = df_model['delivery_time_mins']\nX = df_model.drop(columns=['delivery_time_mins'])\n\n# For simplicity: one-hot encode object columns (like order_dayname, order_protocol if object)\nX = pd.get_dummies(X, drop_first=True)\n\nprint('Final feature matrix shape:', X.shape)\nX.head()"""))

# Cell 12 - Train-test split and scaling for Random Forest (scaling not necessary but keep for NN later)
cells.append(new_code_cell("""# Cell 12 - Train/Test split\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nprint('Train shape:', X_train.shape, 'Test shape:', X_test.shape)\n\n# Save numeric column names for scaling later\nnumeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()\n\n# Standard scaler for numeric features (we'll use for NN)\nscaler = StandardScaler()\nX_train_scaled = X_train.copy()\nX_test_scaled = X_test.copy()\nX_train_scaled[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])\nX_test_scaled[numeric_cols] = scaler.transform(X_test[numeric_cols])\n\nprint('Scaling complete. Sample:')\nX_train_scaled.head()"""))

# Cell 13 - Random Forest baseline
cells.append(new_code_cell("""# Cell 13 - Random Forest baseline\nrf = RandomForestRegressor(random_state=42, n_estimators=100)\nrf.fit(X_train, y_train)\nrf_pred = rf.predict(X_test)\n\ndef regression_metrics(y_true, y_pred):\n    mse = mean_squared_error(y_true, y_pred)\n    rmse = np.sqrt(mse)\n    mae = mean_absolute_error(y_true, y_pred)\n    r2 = r2_score(y_true, y_pred)\n    return {'mse':mse,'rmse':rmse,'mae':mae,'r2':r2}\n\nrf_metrics = regression_metrics(y_test, rf_pred)\nprint('Random Forest metrics:')\nprint(rf_metrics)\n\n# Feature importances (top 10)\nif hasattr(rf, 'feature_importances_'):\n    fi = pd.Series(rf.feature_importances_, index=X.columns).nlargest(10)\n    print('\\nTop features by importance:')\n    print(fi)\n    fi.plot(kind='barh', title='Top 10 Feature Importances')\n    plt.show()\n"""))

# Cell 14 - Prepare numeric-only arrays for NN (use scaled versions)
cells.append(new_code_cell("""# Cell 14 - Prepare data for Neural Network (numeric array inputs)\nX_train_nn = X_train_scaled.values\nX_test_nn = X_test_scaled.values\n\ny_train_nn = y_train.values\ny_test_nn = y_test.values\n\nprint('NN input shape:', X_train_nn.shape)\n"""))

# Cell 15 - Neural Network model (Keras Functional API)
cells.append(new_code_cell("""# Cell 15 - Build and compile Neural Network (Functional API)\ninput_shape = X_train_nn.shape[1]\ninputs = keras.Input(shape=(input_shape,))\nx = layers.Dense(input_shape, activation='relu')(inputs)\nx = layers.Dense(64, activation='relu')(x)\nx = layers.Dropout(0.2)(x)\nx = layers.Dense(32, activation='relu')(x)\noutputs = layers.Dense(1, activation='linear')(x)\nmodel = keras.Model(inputs=inputs, outputs=outputs)\nmodel.compile(optimizer='adam', loss='mse', metrics=['mae'])\nmodel.summary()\n"""))

# Cell 16 - Train NN (with early stopping)
cells.append(new_code_cell("""# Cell 16 - Train Neural Network\nes = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)\nhistory = model.fit(X_train_nn, y_train_nn, validation_split=0.2, epochs=50, batch_size=512, callbacks=[es], verbose=1)\n\n# Plot training/validation loss\nplt.figure(figsize=(8,4))\nplt.plot(history.history['loss'], label='train_loss')\nplt.plot(history.history['val_loss'], label='val_loss')\nplt.legend()\nplt.title('NN Loss')\nplt.show()\n"""))

# Cell 17 - NN evaluation & comparison with Random Forest
cells.append(new_code_cell("""# Cell 17 - Evaluate NN on test set\nnn_pred = model.predict(X_test_nn).flatten()\nnn_metrics = regression_metrics(y_test_nn, nn_pred)\nprint('Neural Network metrics:')\nprint(nn_metrics)\n\n# Compare RF and NN\nprint('\\nComparison:')\nprint('Random Forest:', rf_metrics)\nprint('Neural Network:', nn_metrics)\n\n# Scatter plot actual vs predicted (NN)\nplt.figure(figsize=(6,6))\nplt.scatter(y_test_nn, nn_pred, alpha=0.3)\nplt.plot([y_test_nn.min(), y_test_nn.max()], [y_test_nn.min(), y_test_nn.max()], 'k--')\nplt.xlabel('Actual delivery_time_mins')\nplt.ylabel('Predicted (NN)')\nplt.title('Actual vs Predicted - NN')\nplt.show()\n"""))

# Cell 18 - Answering the questionnaire (text cell)
cells.append(new_markdown_cell("""## Cell 18 - Questionnaire Answers (from PDF)\n\n1. **Problem statement & use-cases**\n   - Predict delivery times to improve ETAs, partner allocation, and customer experience. Useful in e-commerce, ride-hailing, and last-mile logistics.\n\n2. **Three pandas datetime functions**\n   - `pd.to_datetime()` — convert to datetime; `.dt.hour` — extract hour; `.dt.day_name()` — day name.\n\n3. **Datetime / Timedelta / Time span**\n   - `datetime` is a point in time, `timedelta` is a duration between datetimes, and time span/period denotes a range (e.g., week/month).\n\n4. **Why check outliers?**\n   - Outliers skew metrics and model training, can be data errors or rare events; handling improves model robustness.\n\n5. **Three outlier methods**\n   - IQR-based removal/capping, Z-score filtering, winsorization.\n\n6. **Classical ML methods**\n   - Linear Regression, Decision Tree, Random Forest, Gradient Boosting (XGBoost/LightGBM).\n\n7. **Why scaling for NN?**\n   - Improves optimization convergence and prevents features with large ranges dominating gradients.\n\n8. **Optimizer choice**\n   - Adam: adaptive learning rates, robust default for many problems.\n\n9. **Activation used**\n   - ReLU for hidden layers (non-linearity, avoids vanishing gradients); linear for output (regression).\n\n10. **Why NN performs well on large datasets?**\n   - Can learn complex non-linear relationships and improve with more data; capacity increases with data.\n"""))

# Cell 19 - Recommendations & next steps
cells.append(new_markdown_cell("""## Cell 19 - Recommendations & Next Steps\n\n- Add geospatial distance and traffic features to improve predictions.\n- Use Keras Tuner or GridSearch for hyperparameter tuning.\n- Apply SHAP for model interpretability.\n- Deploy model as a REST API (FastAPI) and log predictions for monitoring and re-training.\n"""))

# Save notebook
nb['cells'] = cells
notebook_path = "/mnt/data/Ratnesh_porter_case_study.ipynb"
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

notebook_path

