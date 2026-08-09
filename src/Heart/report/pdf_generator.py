import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


class PDFGenerator:

    def generate_report(
        self,
        prediction,
        probability,
        confidence,
        bmi,
        bmi_category,
        bp_category,
        chol_category,
        risk_level,
        shap_image
    ):

        os.makedirs("static/reports", exist_ok=True)

        filename = (
            f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )

        filepath = os.path.join(
            "static",
            "reports",
            filename
        )

        doc = SimpleDocTemplate(
            filepath,
            pagesize=A4
        )

        styles = getSampleStyleSheet()

        story = []

        # -----------------------------------------
        # Title
        # -----------------------------------------

        title = Paragraph(
            "<b><font size=20>"
            "AI Cardiovascular Risk Assessment Report"
            "</font></b>",
            styles["Title"]
        )

        story.append(title)

        story.append(Spacer(1, 20))

        # -----------------------------------------
        # Report Time
        # -----------------------------------------

        story.append(

            Paragraph(

                f"<b>Generated:</b> "
                f"{datetime.now().strftime('%d %B %Y %I:%M %p')}",

                styles["Normal"]

            )

        )

        story.append(Spacer(1, 20))

        # -----------------------------------------
        # Prediction Table
        # -----------------------------------------

        table_data = [

            ["Clinical Parameter", "Result"],

            ["Risk Level", risk_level],

            ["Prediction Probability", f"{probability}%"],

            ["Model Confidence", f"{confidence}%"],

            ["BMI", f"{bmi} ({bmi_category})"],

            ["Blood Pressure", bp_category],

            ["Cholesterol", chol_category]

        ]

        table = Table(table_data, colWidths=[220, 220])

        table.setStyle(

            TableStyle(

                [

                    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                    ("GRID", (0, 0), (-1, -1), 1, colors.black),

                    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

                    ("ALIGN", (0, 0), (-1, -1), "CENTER")

                ]

            )

        )

        story.append(table)

        story.append(Spacer(1, 25))

        # -----------------------------------------
        # SHAP Image
        # -----------------------------------------

        image_path = os.path.join(
            "static",
            shap_image
        )

        if os.path.exists(image_path):

            story.append(

                Paragraph(

                    "<b>Explainable AI (SHAP)</b>",

                    styles["Heading2"]

                )

            )

            story.append(Spacer(1, 10))

            story.append(

                Image(
                    image_path,
                    width=430,
                    height=250
                )

            )

            story.append(Spacer(1, 20))

        # -----------------------------------------
        # Recommendation
        # -----------------------------------------

        story.append(

            Paragraph(

                "<b>AI Recommendation</b>",

                styles["Heading2"]

            )

        )

        recommendation = (

            "Maintain a healthy lifestyle and continue routine "

            "cardiovascular screening."

            if prediction == 0

            else

            "Consult a cardiologist for further evaluation and "

            "follow the prescribed treatment plan."

        )

        story.append(

            Paragraph(

                recommendation,

                styles["Normal"]

            )

        )

        story.append(Spacer(1, 20))

        # -----------------------------------------
        # Disclaimer
        # -----------------------------------------

        story.append(

            Paragraph(

                "<b>Medical Disclaimer</b>",

                styles["Heading2"]

            )

        )

        story.append(

            Paragraph(

                "This report is generated using an Artificial "

                "Intelligence model and should only be used as a "

                "clinical decision support tool. Final diagnosis "

                "must always be made by a qualified healthcare "

                "professional.",

                styles["Normal"]

            )

        )

        doc.build(story)

        return filename