class ClinicalSummaryGenerator:

    def generate_summary(self, report):

        risk_level = report.get("risk_level", "Unknown")
        probability = report.get("probability", 0)
        confidence = report.get("confidence", 0)

        bmi = report.get("bmi", 0)
        bmi_category = report.get(
            "bmi_category",
            "Unknown"
        )

        bp_category = report.get(
            "bp_category",
            "Unknown"
        )

        chol_category = report.get(
            "chol_category",
            "Unknown"
        )

        top_features = report.get(
            "top_features",
            []
        )

        # ==================================================
        # Overall Risk Statement
        # ==================================================

        if risk_level == "High":

            risk_statement = (
                "The assessment indicates a high estimated "
                "cardiovascular risk based on the clinical "
                "parameters submitted to the machine learning model. "
                "Further evaluation by a qualified healthcare "
                "professional is recommended."
            )

        elif risk_level == "Moderate":

            risk_statement = (
                "The assessment indicates a moderate estimated "
                "cardiovascular risk. Preventive lifestyle measures "
                "and appropriate monitoring of cardiovascular risk "
                "factors are recommended."
            )

        else:

            risk_statement = (
                "The assessment indicates a lower estimated "
                "cardiovascular risk based on the submitted "
                "clinical parameters. Continued healthy lifestyle "
                "practices and routine monitoring are recommended."
            )

        # ==================================================
        # Clinical Findings
        # ==================================================

        findings = []

        # BMI
        if bmi_category == "Underweight":

            findings.append(
                "BMI is classified as underweight. "
                "Maintaining adequate nutrition and discussing "
                "healthy weight management with a healthcare "
                "professional may be beneficial."
            )

        elif bmi_category == "Healthy Weight":

            findings.append(
                "BMI is within the healthy-weight category."
            )

        elif bmi_category == "Overweight":

            findings.append(
                "BMI is classified as overweight. "
                "Gradual weight management through a balanced "
                "diet and regular physical activity may help "
                "reduce cardiovascular risk."
            )

        elif bmi_category == "Obese":

            findings.append(
                "BMI is classified as obese. "
                "Weight management and professional guidance "
                "may help reduce cardiovascular risk."
            )

        # Blood Pressure
        if bp_category == "Normal":

            findings.append(
                "Blood pressure is within the normal category."
            )

        elif bp_category == "Elevated":

            findings.append(
                "Blood pressure is elevated. Regular monitoring "
                "and healthy lifestyle measures are advisable."
            )

        elif bp_category == "Stage 1 Hypertension":

            findings.append(
                "Blood pressure falls within the Stage 1 "
                "hypertension category and should be monitored "
                "with appropriate clinical guidance."
            )

        elif bp_category == "Stage 2 Hypertension":

            findings.append(
                "Blood pressure falls within the Stage 2 "
                "hypertension category and warrants prompt "
                "clinical evaluation."
            )

        # Cholesterol
        if chol_category == "Normal":

            findings.append(
                "Cholesterol is within the normal category."
            )

        elif chol_category == "Borderline High":

            findings.append(
                "Cholesterol is borderline high. "
                "Heart-healthy dietary choices and regular "
                "monitoring may be beneficial."
            )

        elif chol_category == "High":

            findings.append(
                "Cholesterol is classified as high and represents "
                "a potentially modifiable cardiovascular risk factor."
            )

        # ==================================================
        # SHAP Feature Summary
        # ==================================================

        feature_summary = []

        for item in top_features[:3]:

            feature = item.get(
                "feature",
                "Clinical feature"
            )

            impact = item.get(
                "impact",
                ""
            )

            direction = item.get(
                "direction",
                ""
            )

            feature_summary.append(
                f"{feature} ({impact}, {direction})"
            )

        # ==================================================
        # Follow-Up Recommendation
        # ==================================================

        if risk_level == "High":

            follow_up = (
                "Clinical follow-up is recommended to review "
                "cardiovascular risk factors and determine whether "
                "additional investigations or interventions are "
                "appropriate."
            )

        elif risk_level == "Moderate":

            follow_up = (
                "Periodic monitoring of blood pressure, cholesterol, "
                "weight and other cardiovascular risk factors is "
                "recommended."
            )

        else:

            follow_up = (
                "Continue preventive health practices and routine "
                "cardiovascular screening as recommended by a "
                "healthcare professional."
            )

        # ==================================================
        # Build Professional Summary
        # ==================================================

        summary = []

        summary.append(
            "## Overall Assessment"
        )

        summary.append(
            f"The machine learning model estimates a "
            f"**{probability}% cardiovascular disease probability** "
            f"with a model confidence of **{confidence}%**."
        )

        summary.append(
            risk_statement
        )

        summary.append(
            "## Clinical Findings"
        )

        summary.append(
            f"- **BMI:** {bmi} — {bmi_category}"
        )

        summary.append(
            f"- **Blood Pressure:** {bp_category}"
        )

        summary.append(
            f"- **Cholesterol:** {chol_category}"
        )

        if findings:

            summary.append(
                "### Interpretation"
            )

            for finding in findings:

                summary.append(
                    f"- {finding}"
                )

        # ==================================================
        # Explainability Section
        # ==================================================

        if feature_summary:

            summary.append(
                "## Key Model Factors"
            )

            summary.append(
                "The following clinical features were among "
                "the strongest contributors identified by the "
                "explainability analysis:"
            )

            for feature in feature_summary:

                summary.append(
                    f"- {feature}"
                )

        # ==================================================
        # Follow-Up
        # ==================================================

        summary.append(
            "## Recommended Follow-Up"
        )

        summary.append(
            follow_up
        )

        # ==================================================
        # Disclaimer
        # ==================================================

        summary.append(
            "## Clinical Disclaimer"
        )

        summary.append(
            "This summary is generated from the available "
            "assessment data using predefined clinical rules "
            "and machine learning outputs. It is intended for "
            "clinical decision-support and informational "
            "purposes only and does not constitute a medical "
            "diagnosis or replace evaluation by a qualified "
            "healthcare professional."
        )

        return "\n\n".join(summary)