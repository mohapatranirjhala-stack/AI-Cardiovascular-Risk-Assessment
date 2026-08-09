import os

from dotenv import load_dotenv

from groq import Groq

# Load .env file
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class AICarePlanner:

    def generate_plan(self, report):

        prompt = f"""
You are an expert cardiologist and clinical nutritionist.

Create a personalized cardiovascular care plan based ONLY on the patient's report.

Patient Report

Risk Level: {report['risk_level']}
Prediction Probability: {report['probability']}%
Model Confidence: {report['confidence']}%
BMI: {report['bmi']} ({report['bmi_category']})
Blood Pressure: {report['bp_category']}
Cholesterol: {report['chol_category']}

Important Instructions

Generate the report in Markdown.

Include these sections exactly.

# Personalized Cardiovascular Care Plan

## Overall Health Summary

Briefly explain the patient's current condition.

## Food Recommendations

Give 8-10 foods to eat.

## Foods to Avoid

Give 8-10 foods to avoid.

## Exercise Plan

Suggest weekly exercise according to the patient's risk level.

## Lifestyle Improvements

Suggest sleep, stress management, smoking, alcohol etc.

## Monitoring Plan

Mention BP, cholesterol, BMI and medical checkups.

## Expected Improvement

Explain how following this plan may reduce cardiovascular risk.

Never prescribe medicines.

Always end with:

"This plan is AI-generated and should not replace consultation with a qualified healthcare professional."

Keep the response around 500 words.
"""

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5

        )

        return response.choices[0].message.content