import numpy as np
import joblib
import os

def predict_diabetes(input):
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'saved', 'diabetes_predict_age_glucose.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
    
    model = joblib.load(model_path)
    result = model.predict(input)
    return result

