import joblib
import pandas as pd
import sklearn

print(f"Pandas version: {pd.__version__}")
print(f"Scikit-learn version: {sklearn.__version__}")

try:
    model = joblib.load('random_forest_flights_business.pkl')
    print("Successfully loaded model!")
except Exception as e:
    import traceback
    traceback.print_exc()
