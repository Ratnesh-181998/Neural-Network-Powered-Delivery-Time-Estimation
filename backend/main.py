from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import joblib
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Porter Delivery Time Prediction API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os

# Load artifacts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.keras')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'preprocessor.joblib')

try:
    model = keras.models.load_model(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    print(f"Model loaded from {MODEL_PATH}")
    print(f"Preprocessor loaded from {PREPROCESSOR_PATH}")
except Exception as e:
    print(f"Error loading artifacts: {e}")
    model = None
    preprocessor = None

class OrderInput(BaseModel):
    market_id: float
    store_primary_category: str
    order_protocol: float
    total_items: int
    subtotal: int
    num_distinct_items: int
    min_item_price: int
    max_item_price: int
    total_outstanding_orders: float
    estimated_store_to_consumer_driving_duration: float
    created_at: str  # ISO format string expected

@app.get("/")
def read_root():
    return {"message": "Porter Delivery Prediction API is running"}

@app.post("/predict")
def predict_delivery_time(order: OrderInput):
    if model is None or preprocessor is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        # Parse timestamp
        dt = pd.to_datetime(order.created_at)
        order_hour = dt.hour
        order_dayofweek = dt.dayofweek

        # Create DataFrame for input
        data = {
            'market_id': [order.market_id],
            'store_primary_category': [order.store_primary_category],
            'order_protocol': [order.order_protocol],
            'total_items': [order.total_items],
            'subtotal': [order.subtotal],
            'num_distinct_items': [order.num_distinct_items],
            'min_item_price': [order.min_item_price],
            'max_item_price': [order.max_item_price],
            'total_outstanding_orders': [order.total_outstanding_orders],
            'estimated_store_to_consumer_driving_duration': [order.estimated_store_to_consumer_driving_duration],
            'order_hour': [order_hour],
            'order_dayofweek': [order_dayofweek]
        }
        
        df_input = pd.DataFrame(data)

        # Preprocess
        X_processed = preprocessor.transform(df_input)

        # Predict
        prediction = model.predict(X_processed)
        predicted_minutes = float(prediction[0][0])

        return {
            "predicted_delivery_time_minutes": round(predicted_minutes, 2),
            "input_summary": data
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
