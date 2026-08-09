from flask import (Flask, request, render_template, jsonify, send_from_directory)
import markdown
import json
import os
import pandas as pd 
from datetime import datetime

from src.Heart.pipeline.Prediction_pipeline import (
    CustomData,
    PredictPipeline
)
from src.Heart.report.pdf_generator import PDFGenerator
from src.Heart.report.email_report import EmailReportSender

from src.Heart.explainability.shap_explainer import SHAPExplainer
from src.Heart.ai.gemini_chat import GeminiHealthAssistant
from src.Heart.ai.groq_care_planner import AICarePlanner
from src.Heart.ai.rule_based_care import RuleBasedCarePlanner
from src.Heart.ai.clinical_summary import ClinicalSummaryGenerator



app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

latest_report = {}
batch_results = []


RISK_HISTORY_FILE = os.path.join(
    app.static_folder,
    "risk_history.json"
)


def load_risk_history():

    try:

        if not os.path.exists(RISK_HISTORY_FILE):

            return []

        with open(
            RISK_HISTORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception as e:

        print("Risk history load error:", e)

        return []


def save_risk_history(probability, risk_level):

    try:

        history = load_risk_history()

        history.append({

            "date": datetime.now().strftime(
                "%d %b %Y, %I:%M %p"
            ),

            "probability": round(
                float(probability),
                2
            ),

            "risk_level": risk_level

        })

        # Keep only the latest 10 assessments

        history = history[-10:]

        with open(
            RISK_HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

        print("✓ Risk history saved")

    except Exception as e:

        print("Risk history save error:", e)



@app.route("/", methods=["GET", "POST"])
def home():
    global latest_report

    if request.method == "POST":

        try:

            print("=" * 60)
            print("REQUEST RECEIVED")
            print("=" * 60)

            # --------------------------------------------------
            # Collect Patient Data
            # --------------------------------------------------

            data = CustomData(

                age=request.form.get("age"),
                sex=request.form.get("sex"),
                cp=request.form.get("cp"),
                trestbps=request.form.get("trestbps"),
                chol=request.form.get("chol"),
                fbs=request.form.get("fbs"),
                restecg=request.form.get("restecg"),
                thalach=request.form.get("thalach"),
                exang=request.form.get("exang"),
                oldpeak=request.form.get("oldpeak"),
                slope=request.form.get("slope"),
                ca=request.form.get("ca"),
                thal=request.form.get("thal")

            )

            print("✓ CustomData created")

            final_data = data.get_data_as_dataframe()

            print("✓ DataFrame created")
            print(final_data)

            # --------------------------------------------------
            # BMI
            # --------------------------------------------------

            height = float(request.form.get("height"))
            weight = float(request.form.get("weight"))

            bmi = round(
                weight / ((height / 100) ** 2),
                2
            )

            print("BMI :", bmi)

            # --------------------------------------------------
            # BMI Category
            # --------------------------------------------------

            if bmi < 18.5:

                bmi_category = "Underweight"

            elif bmi < 25:

                bmi_category = "Healthy Weight"

            elif bmi < 30:

                bmi_category = "Overweight"

            else:

                bmi_category = "Obese"

            # --------------------------------------------------
            # Blood Pressure Category
            # --------------------------------------------------

            bp = int(request.form.get("trestbps"))

            if bp < 120:

                bp_category = "Normal"

            elif bp < 130:

                bp_category = "Elevated"

            elif bp < 140:

                bp_category = "Stage 1 Hypertension"

            else:

                bp_category = "Stage 2 Hypertension"

            # --------------------------------------------------
            # Cholesterol Category
            # --------------------------------------------------

            cholesterol = int(request.form.get("chol"))

            if cholesterol < 200:

                chol_category = "Normal"

            elif cholesterol < 240:

                chol_category = "Borderline High"

            else:

                chol_category = "High"

            # --------------------------------------------------
            # Prediction
            # --------------------------------------------------

            predict_pipeline = PredictPipeline()

            prediction_result = predict_pipeline.predict(
                final_data
            )

            print("Prediction Result")
            print(prediction_result)

            prediction = int(prediction_result["prediction"])

            probability = round(
                float(prediction_result["probability"]),
                2
            )

            confidence = round(
                float(prediction_result["confidence"]),
                2
            )

            # --------------------------------------------------
            # Risk Level
            # --------------------------------------------------

            if probability < 35:

                risk_level = "Low"

            elif probability < 70:

                risk_level = "Moderate"

            else:

                risk_level = "High"

            # --------------------------------------------------
            # SHAP Explainability
            # --------------------------------------------------

            print("Generating SHAP Explanation...")

            shap_explainer = SHAPExplainer()

            shap_result = shap_explainer.generate_explanation(
                final_data
            )

            print("✓ SHAP Generated Successfully")

            print(shap_result)


            # --------------------------------------------------
            # Generate PDF Report
            # --------------------------------------------------

            print("Generating PDF Report...")

            pdf_generator = PDFGenerator()

            pdf_file = pdf_generator.generate_report(

                prediction=prediction,

                probability=probability,

                confidence=confidence,

                bmi=bmi,

                bmi_category=bmi_category,

                bp_category=bp_category,

                chol_category=chol_category,

                risk_level=risk_level,

                shap_image=shap_result["image"]

            )

            print("✓ PDF Report Generated")
            

            latest_report = {

                "prediction": prediction,

                "risk_level": risk_level,

                "probability": probability,

                "confidence": confidence,

                "bmi": bmi,

                "bmi_category": bmi_category,

                "bp_category": bp_category,

                "chol_category": chol_category,

                "top_features": shap_result["top_features"],
                "pdf_file": pdf_file
               

            } 
            save_risk_history(
            probability,
            risk_level
            )


            risk_history = load_risk_history()
           # --------------------------------------------------
            # Generate Personalized AI Care Plan
            # --------------------------------------------------

            print("Generating AI Care Plan...")

            planner = AICarePlanner()

            try:

                ai_care_plan = planner.generate_plan(
                    latest_report
                )

                print("✓ AI Care Plan Generated (Groq)")

            except Exception as e:

                print("Groq Error:", e)

                print("Switching to Rule-Based Care Planner...")

                fallback = RuleBasedCarePlanner()

                ai_care_plan = fallback.generate_plan(
                    latest_report
                )

                print("✓ Rule-Based Care Plan Generated")

            ai_care_plan_html = markdown.markdown(

                ai_care_plan,

                extensions=[

                    "extra",

                    "nl2br"

                ]

            )
            # --------------------------------------------------
            # Generate Rule-Based Clinical Summary
            # --------------------------------------------------

            print("Generating Clinical Summary...")

            summary_generator = ClinicalSummaryGenerator()

            clinical_summary = summary_generator.generate_summary(
               report=latest_report
            )

            clinical_summary_html = markdown.markdown(
                clinical_summary,
                extensions=[
                    "extra",
                    "nl2br"
                ]
            )

            print("✓ Clinical Summary Generated")
            # --------------------------------------------------
            # Render Report
            # --------------------------------------------------

            return render_template(

                "result.html",

                prediction=prediction,

                probability=probability,

                confidence=confidence,

                bmi=bmi,

                bmi_category=bmi_category,

                bp_category=bp_category,

                chol_category=chol_category,

                risk_level=risk_level,

                shap_image=shap_result["image"],

                top_features=shap_result["top_features"],

                pdf_file=pdf_file,
                ai_care_plan=ai_care_plan_html,
                clinical_summary=clinical_summary_html,
                risk_history=risk_history


            )

        except Exception as e:

            print("=" * 60)
            print("ERROR")
            print("=" * 60)

            print(e)

            return render_template(

                "error.html",

                error_message=str(e)

            )

    return render_template("index.html")

# ==================================================
# AI Health Assistant
# ==================================================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "")

    assistant = GeminiHealthAssistant()

    try:

        answer = assistant.ask(question=question,
                 report=latest_report)

    except Exception as e:

        print(e)

        answer = (
            "Sorry, the AI Health Assistant is currently unavailable. "
            "Please try again later."
        )

    return jsonify(
        {
            "answer": answer
        }
    )

# ==================================================
# Download PDF Report
# ==================================================

@app.route("/download/<filename>")
def download_report(filename):

    return send_from_directory(

        "static/reports",

        filename,

        as_attachment=True

    )
    # ==================================================
# Email PDF Report
# ==================================================

@app.route("/email-report", methods=["POST"])
def email_report():

    try:

        data = request.get_json()

        receiver_email = data.get("email")

        if not receiver_email:

            return jsonify({
                "success": False,
                "message": "Please enter an email address."
            }), 400

        if not latest_report:

            return jsonify({
                "success": False,
                "message": "No assessment report is available."
            }), 400

        pdf_file = latest_report.get("pdf_file")

        if not pdf_file:

            return jsonify({
                "success": False,
                "message": "PDF report is not available."
            }), 400

        pdf_path = os.path.join(
            app.static_folder,
            "reports",
            pdf_file
        )

        sender = EmailReportSender()

        sender.send_report(
            receiver_email,
            pdf_path
        )

        return jsonify({
            "success": True,
            "message": "PDF report emailed successfully."
        })

    except Exception as e:

        print("Email Report Error:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
# ==================================================
# Delete Risk History Entry
# ==================================================

@app.route("/delete-risk/<int:index>", methods=["POST"])
def delete_risk_history(index):

    try:

        history = load_risk_history()

        if index < 0 or index >= len(history):

            return jsonify({
                "success": False,
                "message": "Assessment not found."
            }), 404

        # Delete selected assessment
        deleted_entry = history.pop(index)

        # Save updated history
        with open(
            RISK_HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

        print(
            "✓ Risk history deleted:",
            deleted_entry
        )

        return jsonify({
            "success": True,
            "message": "Assessment deleted successfully."
        })

    except Exception as e:

        print(
            "Risk history delete error:",
            e
        )

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
# ==================================================
# Batch CSV Prediction
# ==================================================

@app.route("/batch-prediction", methods=["GET", "POST"])
def batch_prediction():

    results = []

    if request.method == "POST":

        try:

            file = request.files.get("csv_file")

            if not file:

                return render_template(
                    "error.html",
                    error_message="Please upload a CSV file."
                )

            if file.filename == "":

                return render_template(
                    "error.html",
                    error_message="Please select a CSV file."
                )

            if not file.filename.lower().endswith(".csv"):

                return render_template(
                    "error.html",
                    error_message="Only CSV files are allowed."
                )

            # Read CSV file
            dataframe = pd.read_csv(file)

            print("=" * 60)
            print("BATCH CSV PREDICTION")
            print("=" * 60)

            print("Rows:", len(dataframe))
            print("Columns:")
            print(dataframe.columns.tolist())

            # Required model columns
            required_columns = [
                "age",
                "sex",
                "cp",
                "trestbps",
                "chol",
                "fbs",
                "restecg",
                "thalach",
                "exang",
                "oldpeak",
                "slope",
                "ca",
                "thal"
            ]

            missing_columns = [
                column
                for column in required_columns
                if column not in dataframe.columns
            ]

            if missing_columns:

                return render_template(
                    "error.html",
                    error_message=(
                        "Missing required CSV columns: "
                        + ", ".join(missing_columns)
                    )
                )

            predict_pipeline = PredictPipeline()

            for index, row in dataframe.iterrows():

                patient_data = pd.DataFrame(
                    [[
                        row["age"],
                        row["sex"],
                        row["cp"],
                        row["trestbps"],
                        row["chol"],
                        row["fbs"],
                        row["restecg"],
                        row["thalach"],
                        row["exang"],
                        row["oldpeak"],
                        row["slope"],
                        row["ca"],
                        row["thal"]
                    ]],
                    columns=required_columns
                )

                prediction_result = predict_pipeline.predict(
                    patient_data
                )

                prediction = int(
                    prediction_result["prediction"]
                )

                probability = round(
                    float(
                        prediction_result["probability"]
                    ),
                    2
                )

                confidence = round(
                    float(
                        prediction_result["confidence"]
                    ),
                    2
                )

                if probability < 35:

                    risk_level = "Low"

                elif probability < 70:

                    risk_level = "Moderate"

                else:

                    risk_level = "High"

                results.append({

                    "patient": index + 1,

                    "prediction": prediction,

                    "probability": probability,

                    "confidence": confidence,

                    "risk_level": risk_level

                })

            print("✓ Batch prediction completed")

            # Store results for CSV download
            global batch_results

            batch_results = results

            return render_template(

                "batch_prediction.html",

                results=results

            )

        except Exception as e:

            print("=" * 60)
            print("BATCH PREDICTION ERROR")
            print("=" * 60)

            print(e)

            return render_template(

                "error.html",

                error_message=str(e)

            )

    return render_template(

        "batch_prediction.html",

        results=results

    )


# ==================================================
# Batch Results CSV Download
# ==================================================

@app.route("/download-batch-results")
def download_batch_results():

    try:

        if not batch_results:

            return render_template(
                "error.html",
                error_message="No batch prediction results available."
            )

        dataframe = pd.DataFrame(batch_results)

        results_path = os.path.join(

            app.static_folder,

            "reports",

            "batch_prediction_results.csv"

        )

        dataframe.to_csv(

            results_path,

            index=False

        )

        return send_from_directory(

            os.path.dirname(results_path),

            os.path.basename(results_path),

            as_attachment=True

        )

    except Exception as e:

        return render_template(

            "error.html",

            error_message=str(e)

        )


# ==================================================
# CSV Template Download
# ==================================================

@app.route("/download-csv-template")
def download_csv_template():

    try:

        template_path = os.path.join(

            app.static_folder,

            "reports",

            "patient_batch_template.csv"

        )

        dataframe = pd.DataFrame({

            "age": [55, 45],

            "sex": [1, 0],

            "cp": [1, 2],

            "trestbps": [140, 120],

            "chol": [240, 200],

            "fbs": [0, 0],

            "restecg": [1, 0],

            "thalach": [150, 170],

            "exang": [0, 0],

            "oldpeak": [1.2, 0.5],

            "slope": [1, 2],

            "ca": [0, 0],

            "thal": [2, 2]

        })

        dataframe.to_csv(

            template_path,

            index=False

        )

        return send_from_directory(

            os.path.dirname(template_path),

            os.path.basename(template_path),

            as_attachment=True

        )

    except Exception as e:

        return render_template(

            "error.html",

            error_message=str(e)

        )
   
if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=8080,

        debug=True

    )