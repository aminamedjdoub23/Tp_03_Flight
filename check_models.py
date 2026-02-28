import joblib

models = [
    "random_forest_flight_price.pkl",
    "random_forest_flight_price_economy.pkl",
    "random_forest_flight_price_business.pkl"
]

with open("model_features.txt", "w") as f:
    for m_path in models:
        f.write(f"--- Model: {m_path} ---\n")
        try:
            model = joblib.load(m_path)
            if hasattr(model, 'feature_names_in_'):
                f.write("feature_names_in_: " + str(list(model.feature_names_in_)) + "\n")
            elif hasattr(model, 'named_steps') and 'preprocessor' in model.named_steps:
                f.write("features expected by preprocessor: " + str(list(model.named_steps['preprocessor'].feature_names_in_)) + "\n")
            else:
                f.write("Could not easily find feature names.\n")
        except Exception as e:
            f.write(f"Error loading {m_path}: {e}\n")
