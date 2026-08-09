class RuleBasedCarePlanner:

    def generate_plan(self, report):

        risk = report["risk_level"]
        bmi = report["bmi_category"]
        bp = report["bp_category"]
        chol = report["chol_category"]

        foods = []
        avoid = []
        exercise = []
        lifestyle = []
        monitoring = []

        # -----------------------------
        # Cholesterol Rules
        # -----------------------------

        if chol == "High":

            foods.extend([
                "Oats",
                "Brown rice",
                "Leafy vegetables",
                "Salmon",
                "Walnuts",
                "Beans",
                "Apples",
                "Olive oil"
            ])

            avoid.extend([
                "Butter",
                "Fried food",
                "Red meat",
                "Processed meat",
                "Bakery products",
                "Fast food"
            ])

        elif chol == "Borderline High":

            foods.extend([
                "Whole grains",
                "Fruit",
                "Vegetables",
                "Fish"
            ])

            avoid.extend([
                "Sugary drinks",
                "Excess fried food"
            ])

        # -----------------------------
        # Blood Pressure Rules
        # -----------------------------

        if bp != "Normal":

            foods.extend([
                "Bananas",
                "Spinach",
                "Tomatoes",
                "Low-fat yogurt"
            ])

            avoid.extend([
                "Extra salt",
                "Pickles",
                "Packaged snacks"
            ])

        # -----------------------------
        # BMI Rules
        # -----------------------------

        if bmi == "Obese":

            exercise = [
                "Walking 45 minutes daily",
                "Cycling",
                "Swimming",
                "Weight reduction exercises"
            ]

        elif bmi == "Overweight":

            exercise = [
                "Walking 30 minutes",
                "Jogging",
                "Stretching",
                "Yoga"
            ]

        else:

            exercise = [
                "150 minutes moderate exercise/week",
                "Brisk walking",
                "Light strength training"
            ]

        # -----------------------------
        # Lifestyle
        # -----------------------------

        lifestyle = [

            "Sleep 7-8 hours daily",

            "Reduce stress",

            "Drink enough water",

            "Avoid smoking",

            "Limit alcohol",

            "Maintain healthy weight"

        ]

        # -----------------------------
        # Monitoring
        # -----------------------------

        monitoring = [

            "Check blood pressure weekly",

            "Monitor cholesterol every 6 months",

            "Maintain BMI",

            "Annual heart checkup"

        ]

        return f"""
# Personalized Cardiovascular Care Plan

## Overall Health Summary

Current Risk Level: **{risk}**

BMI Category: **{bmi}**

Blood Pressure: **{bp}**

Cholesterol: **{chol}**

---

## Food Recommendations

{chr(10).join("- "+x for x in foods)}

---

## Foods To Avoid

{chr(10).join("- "+x for x in avoid)}

---

## Exercise Plan

{chr(10).join("- "+x for x in exercise)}

---

## Lifestyle Improvements

{chr(10).join("- "+x for x in lifestyle)}

---

## Monitoring Plan

{chr(10).join("- "+x for x in monitoring)}

---

## Expected Improvement

Following these recommendations consistently may help lower cardiovascular risk over time, improve blood pressure, cholesterol levels, and overall heart health.

---

**This care plan was automatically generated using the built-in clinical rule engine because the AI service is currently unavailable. Always consult a qualified healthcare professional before making medical decisions.**
"""