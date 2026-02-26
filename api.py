from fastapi import FastAPI, HTTPException
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


@app.post("/predict")
def predict(payload: FlightFeatures):
    X = pd.DataFrame([payload.model_dump()])

    y_pred = model.predict(X)[0]

    return {
            "predicted_price": round(y_pred, 2),
            "currency": "INR",
            "info": "Prix estimé en Roupies Indiennes"
        }

# Lancer l'API localement si ce script est exécuté directement
if __name__ == "__main__":
    import uvicorn
    # Le paramètre reload=True permet de recharger l'API automatiquement à chaque modification du code
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)