import streamlit as st
import requests
import numpy as np


TIME_OPTIONS = ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night']
TIME_DISPLAY = {
    'Early_Morning': 'Aube',
    'Morning': 'Matin',
    'Afternoon': 'Après-midi',
    'Evening': 'Soirée',
    'Night': 'Nuit',
    'Late_Night': 'Milieu de la nuit'
}

DURATION_VALS = [x / 2.0 for x in range(1, 81)] 
def format_duration(val):
    h = int(val)
    m = int((val % 1) * 60)
    return f"{h}h{m:02d}"

st.set_page_config(page_title="Flight Price Predictor", layout="centered")

st.title("Prédiction de Prix de Vols")
st.markdown("Bienvenue ! Remplissez les informations de votre vol ci-dessous pour le devis (en INR).")

API_URL = "http://flight_price_api:8000/predict"

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        airline = st.selectbox("Compagnie Aérienne", ['Vistara', 'Air_India', 'Indigo', 'GO_FIRST', 'AirAsia', 'SpiceJet'])
        source_city = st.selectbox("Ville de Départ", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
        departure_time = st.selectbox("Heure de Départ", TIME_OPTIONS, format_func=lambda x: TIME_DISPLAY[x])
        stops = st.selectbox("Nombre d'escales", ['zero', 'one', 'two_or_more'], format_func=lambda x: '0' if x=='zero' else '1' if x=='one' else '+2')
        class_ticket = st.selectbox("Classe", ['Economy', 'Business'], format_func=lambda x: "Économique" if x == 'Economy' else "Affaires")
        
    with col2:
        destination_city = st.selectbox("Ville d'Arrivée", ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])
        arrival_time = st.selectbox("Heure d'Arrivée", TIME_OPTIONS, format_func=lambda x: TIME_DISPLAY[x])
        duration = st.select_slider("Durée du vol", options=DURATION_VALS, value=2.5, format_func=format_duration)
        days_left = st.slider("Jours avant le départ", min_value=1, max_value=50, value=5)
    
    st.markdown("---")
    st.subheader("Configuration du Modèle")
    model_type = st.selectbox("Modèle de Prédiction", ["Global", "Economy", "Business"], help="Choisissez le modèle IA spécifique à utiliser pour la prédiction.")
    submit_button = st.form_submit_button(label="Prédire le Prix", use_container_width=True)

if submit_button:
    data = {
        "airline": airline,
        "source_city": source_city,
        "departure_time": departure_time,
        "stops": stops,
        "arrival_time": arrival_time,
        "destination_city": destination_city,
        "class_ticket": class_ticket,
        "duration": float(duration),
        "days_left": int(days_left),
        "model_type": model_type
    }
    
    with st.spinner("Analyse par notre modèle d'Intelligence Artificielle..."):
        try:
            # Essai 1 : Si Streamlit tourne à l'intérieur de Docker
            response = requests.post("http://flight_price_api:8000/predict", json=data)
        except requests.exceptions.ConnectionError:
            try:
                # Essai 2 : Si Streamlit tourne en local sur Windows (Terminal)
                response = requests.post("http://127.0.0.1:8000/predict", json=data)
            except requests.exceptions.ConnectionError as e:
                st.error("Impossible de se connecter à l'API ni en Docker ni en local.")
                st.stop()
                
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Prix Estimé : {result['predicted_price']:,.2f} INR")

        else:
            st.error(f"Erreur de l'API : {response.text}")
