import numpy as np
import joblib
import os
 
 
 
def predict_diabetes(input):
    model_path = os.path.join('saved', 'diabetes_predict_age_glucose.pkl')
    model = joblib.load(model_path)
    result=model.predict(input)
    return result

