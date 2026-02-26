from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import os


MODEL_PATH = "random_forest_flights.pkl"
model = joblib.load(MODEL_PATH)

app = FastAPI(title="Flight Price Prediction API", version="1.0")

class FlightFeatures(BaseModel):
    airline:str = Field(...,description="airline of flight")
    flight:str = Field(...,description="flight of flight")
    source_city:str = Field(...,description="source city of flight")
    departure_time:str = Field(...,description="departure time of flight")
    stops:str = Field(...,description="number of stops of flight")
    arrival_time:str = Field(...,description="arrival time of flight")
    destination_city:str = Field(...,description="destination city of flight")
    class_ticket:str = Field(...,description="class of flight")
    duration:float = Field(...,description="duration of flight")
    days_left:int = Field(...,description="days left for flight")
    price:int = Field(...,description="price of flight") 

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def serve_frontend():
    return FileResponse("index.html")


@app.post("/predict")
def predict(payload: FlightFeatures):
    X = pd.DataFrame([payload.model_dump()])

    y_pred = model.predict(X)[0]

    return {
            "predicted_price": round(y_pred, 2),
            "currency": "INR",
            "info": "Prix estimé en Roupies Indiennes"
        }

@app.post("/optimize_date")
def optimize_date(payload: FlightFeatures):
    base_payload = payload.model_dump()
    target_days_left = base_payload["days_left"]
    
    variations = []
    # Test from purchasing today (days_left is accurately time_diff) to +14 days of waiting (days_left decreases)
    # Actually wait we are optimizing WHEN to buy.
    # So if you buy today, days_left = target_days_left
    # If you buy tomorrow, days_left = target_days_left - 1
    # Let's test a window of 7 days into the future (waiting to buy)
    for offset in range(0, 8):
        test_days_left = target_days_left - offset
        
        # Ensure we don't look past the departure date
        if test_days_left > 0:
            test_payload = base_payload.copy()
            test_payload["days_left"] = test_days_left
            variations.append({"payload": test_payload, "buy_in_days": offset})
            
    if not variations:
        raise HTTPException(status_code=400, detail="Target date is too soon to wait for buying.")
        
    X_variations = pd.DataFrame([v["payload"] for v in variations])
    prices = model.predict(X_variations)
    
    # Associate prices with the day offsets
    results = []
    for i, meta in enumerate(variations):
        results.append({
            "buy_in_days": meta["buy_in_days"],
            "days_left": meta["payload"]["days_left"],
            "predicted_price": round(float(prices[i]), 2)
        })
        
    # Find the cheapest option
    cheapest_option = min(results, key=lambda x: x["predicted_price"])
    buy_today_price = results[0]["predicted_price"]
    
    return {
        "best_option": cheapest_option,
        "savings_potential": round(buy_today_price - cheapest_option["predicted_price"], 2),
        "all_predictions": results,
        "currency": "INR"
    }

# Lancer l'API localement si ce script est exécuté directement
if __name__ == "__main__":
    import uvicorn
    # Le paramètre reload=True permet de recharger l'API automatiquement à chaque modification du code
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)