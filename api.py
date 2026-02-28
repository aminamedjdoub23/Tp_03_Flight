from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import os


MODELS = {
    "Global": joblib.load("random_forest_flight_price.pkl"),
    "Economy": joblib.load("random_forest_flight_price_economy.pkl"),
    "Business": joblib.load("random_forest_flight_price_business.pkl")
}

app = FastAPI(title="Flight Price Prediction API", version="1.0")

class FlightFeatures(BaseModel):
    airline:str = Field(...,description="airline of flight")
    source_city:str = Field(...,description="source city of flight")
    departure_time:str = Field(...,description="departure time of flight")
    stops:str = Field(...,description="number of stops of flight")
    arrival_time:str = Field(...,description="arrival time of flight")
    destination_city:str = Field(...,description="destination city of flight")
    class_ticket:str = Field(...,description="class of flight")
    duration:float = Field(...,description="duration of flight")
    days_left:int = Field(...,description="days left for flight")
    model_type:str = Field(default="Random_Forest_Global", description="Which model to use (Random_Forest_Global, Random_Forest_Economy, Random_Forest_Business)")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction de prix de vols. Utilisez /docs pour voir la documentation de l'API."}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: FlightFeatures):
    # Determine the model type
    m_type = payload.model_type
    if m_type not in MODELS:
        raise HTTPException(status_code=400, detail=f"Invalid model_type. Must be one of {list(MODELS.keys())}")

    model = MODELS[m_type]

    # Convert payload to dictionary and drop model_type
    data = payload.model_dump()
    data.pop('model_type', None)

    # For Economy and Business models, drop the class_ticket feature
    if m_type in ["Economy", "Business"]:
        data.pop('class_ticket', None)

    X = pd.DataFrame([data])

    y_pred = model.predict(X)[0]

    return {
            "predicted_price": round(y_pred, 2),
            "currency": "INR",
            "model_used": m_type,
            "info": "Prix estimé en Roupies Indiennes"
        }

# Lancer l'API localement si ce script est exécuté directement
if __name__ == "__main__":
    import uvicorn
    # Le paramètre reload=True permet de recharger l'API automatiquement à chaque modification du code
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)