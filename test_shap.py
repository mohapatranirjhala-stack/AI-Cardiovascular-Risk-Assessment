import pandas as pd

from src.Heart.explainability.shap_explainer import SHAPExplainer

sample = pd.DataFrame([{
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 140,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 1,
    "ca": 0,
    "thal": 2
}])

explainer = SHAPExplainer()

image_path = explainer.generate_explanation(sample)

print("SHAP image generated at:", image_path)