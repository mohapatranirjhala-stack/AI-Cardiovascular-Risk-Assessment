import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv

class GeminiHealthAssistant:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = genai.GenerativeModel(
            "gemini-3.6-flash"
        )

    def ask(self, question, report=None):

        if report:

            prompt = f"""
You are an AI Cardiovascular Health Assistant.

You are helping explain a patient's cardiovascular assessment report.

Patient Report:

Risk Level: {report['risk_level']}
Prediction Probability: {report['probability']}%
Model Confidence: {report['confidence']}%
BMI: {report['bmi']} ({report['bmi_category']})
Blood Pressure: {report['bp_category']}
Cholesterol: {report['chol_category']}
Top SHAP Features:
{report['top_features']}

Patient Question:
{question}

Instructions:
- Answer in simple language.
- Keep the answer under 150 words.
- Do not prescribe medicines.
- Recommend consulting a healthcare professional for diagnosis.
"""

        else:

            prompt = f"""
You are an AI Cardiovascular Health Assistant.

Patient Question:
{question}

Instructions:
- Answer in simple language.
- Keep the answer under 150 words.
"""

        response = self.model.generate_content(prompt)

        return response.text