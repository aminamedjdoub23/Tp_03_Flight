import requests
import json

url = "http://127.0.0.1:8000/predict"

base_payload = {
    "airline": "Vistara",
    "source_city": "Mumbai",
    "departure_time": "Morning",
    "stops": "one",
    "arrival_time": "Night",
    "destination_city": "Delhi",
    "class_ticket": "Economy",
    "duration": 5.5,
    "days_left": 10
}

for model_type in ["Global", "Economy", "Business"]:
    print(f"\n--- Testing Model: {model_type} ---")
    payload = base_payload.copy()
    payload["model_type"] = model_type
    
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response:", json.dumps(response.json(), indent=2))
        else:
            print("Error details:", response.text)
    except requests.exceptions.ConnectionError:
        print("API is not running at", url)
