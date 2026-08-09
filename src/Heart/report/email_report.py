import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


class EmailReportSender:

    def __init__(self):

        self.sender_email = os.getenv("REPORT_EMAIL")
        self.sender_password = os.getenv("REPORT_EMAIL_PASSWORD")

    def send_report(self, receiver_email, pdf_path):

        # Check email credentials
        if not self.sender_email or not self.sender_password:

            raise ValueError(
                "Email credentials are not configured."
            )

        # Check PDF file
        if not os.path.exists(pdf_path):

            raise FileNotFoundError(
                f"PDF file not found: {pdf_path}"
            )

        # Create email
        message = EmailMessage()

        message["Subject"] = (
            "AI Cardiovascular Risk Assessment Report"
        )

        message["From"] = self.sender_email

        message["To"] = receiver_email

        # Email body
        message.set_content(
            """
Hello,

Your AI Cardiovascular Risk Assessment report is attached.

This report contains:

- Cardiovascular risk prediction
- Risk probability
- Model confidence
- BMI and clinical indicators
- SHAP explainability
- Personalized AI care plan
- Clinical summary

Please consult a qualified healthcare professional
for medical interpretation.

Regards,
AI Cardiovascular Risk Assessment System
"""
        )

        # Read PDF
        with open(pdf_path, "rb") as file:

            pdf_data = file.read()

        # Attach PDF
        message.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path)
        )

        # Connect to Gmail SMTP server
        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                self.sender_email,
                self.sender_password
            )

            server.send_message(message)

        return True