from src.Heart.ai.groq_care_planner import AICarePlanner

planner = AICarePlanner()

report = {
    "risk_level": "High",
    "probability": 86.5,
    "confidence": 94.2,
    "bmi": 31.4,
    "bmi_category": "Obese",
    "bp_category": "Stage 2 Hypertension",
    "chol_category": "High"
}

print(planner.generate_plan(report))