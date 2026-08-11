# 🫀 AI Cardiovascular Risk Assessment

<p align="center">
  <strong>An intelligent machine-learning powered web application for cardiovascular risk assessment.</strong>
</p>

<p align="center">
  <a href="https://github.com/mohapatranirjhala-stack/AI-Cardiovascular-Risk-Assessment">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <a href="https://ai-cardiovascular-risk-assessment.onrender.com">
    <img src="https://img.shields.io/badge/Live-Demo-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Live Demo">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/CatBoost-ML-FFCC00?style=flat-square">
  <img src="https://img.shields.io/badge/XGBoost-ML-189FDD?style=flat-square">
  <img src="https://img.shields.io/badge/SHAP-Explainability-FF6F00?style=flat-square">
  <img src="https://img.shields.io/badge/DVC-Data%20Versioning-945DD6?style=flat-square&logo=dvc&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square">
</p>

---

## 🚀 Project Overview

**AI Cardiovascular Risk Assessment** is a production-oriented machine learning web application that estimates an individual's cardiovascular disease risk from clinical and lifestyle-related health parameters.

Instead of presenting machine learning as a standalone notebook, this project transforms the complete ML workflow into an accessible web application:

> **Patient Data → Data Validation → Preprocessing → ML Prediction → Risk Probability → Risk Classification → Explainable Result → History → Notification**

The application combines machine learning, explainable AI, experiment-oriented development practices, and cloud deployment into a single end-to-end system.

### 🎯 Core Objective

The system is designed to:

- Analyze cardiovascular risk-related patient attributes.
- Process the input through a trained machine learning pipeline.
- Predict whether the patient falls into a **Low** or **High Cardiovascular Risk** category.
- Provide probability/confidence information with the prediction.
- Present the result through a user-friendly web interface.
- Maintain a local risk-assessment history.
- Support practical deployment through Docker and Render.
- Provide an extensible foundation for explainable AI and intelligent health-assistance features.

> ⚠️ **Disclaimer:** This project is intended for educational and demonstration purposes only. It is not a medical diagnostic system and should not be used as a substitute for professional medical advice.

---

# ✨ Why This Project Stands Out

This project goes beyond a traditional "train a model and display accuracy" implementation.

### 🧠 Machine Learning

A complete ML pipeline handles:

- Data ingestion
- Data transformation
- Feature preprocessing
- Model training
- Model evaluation
- Prediction
- Probability estimation
- Risk classification

### 🔍 Explainable AI

The project includes an explainability layer using **SHAP**, providing a foundation for understanding which features contribute to model predictions.

### 🌐 Production Web Application

The trained model is exposed through a Flask application instead of being limited to a Jupyter Notebook.

### 📊 Risk Assessment History

Previous assessments can be tracked through the application's risk-history functionality.

### 📧 Notification Support

The application includes email functionality for delivering assessment-related information.

### 📦 Deployment Ready

The project contains:

- Docker configuration
- Gunicorn production server
- Procfile
- Render deployment configuration
- Environment-variable based configuration

### 🔄 Reproducible ML Workflow

The project uses **DVC** for data/pipeline versioning and follows a structured ML project architecture.

---
# 🖥️ Application Experience

The application follows a simple workflow designed around the user:

```text
┌──────────────────────┐
│   Patient Information│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Input Validation   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Data Transformation  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Trained ML Pipeline  │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────────┐
│ Prediction + Probability   │
│ + Confidence Information   │
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ Cardiovascular Risk Result │
│                            │
│   LOW RISK / HIGH RISK     │
└──────────┬─────────────────┘
           │
      ┌────┴─────┐
      ▼          ▼
   History     Email
```

---

# 🧬 Dataset Features

The underlying cardiovascular dataset contains clinical and demographic attributes used for binary classification.

| Feature | Description |
|---|---|
| Age | Patient age |
| Sex | Biological sex |
| Chest Pain Type | Type of chest pain experienced |
| Resting Blood Pressure | Resting blood pressure |
| Serum Cholesterol | Serum cholesterol level |
| Fasting Blood Sugar | Fasting blood sugar indicator |
| Resting ECG | Resting electrocardiographic result |
| Maximum Heart Rate | Maximum heart rate achieved |
| Exercise-Induced Angina | Angina triggered by exercise |
| ST Depression | Exercise-induced ST depression |
| ST Slope | Slope of the peak exercise ST segment |
| Major Vessels | Number of major vessels observed |
| Thalassemia | Thalassemia-related clinical attribute |
| Target | Cardiovascular disease classification |

---

# 🧠 Machine Learning Pipeline

The project follows a modular machine learning architecture rather than placing the entire workflow inside one script.

```text
                    ┌─────────────────┐
                    │   Raw Dataset   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Data Ingestion  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Transformation  │
                    │ & Preprocessing │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Model Training  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Model Evaluation│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Saved ML Model  │
                    └────────┬────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │      Flask Prediction API   │
              └──────────────┬──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Risk Assessment │
                    └─────────────────┘
```

---

# 🏗️ Project Architecture

```text
AI-Cardiovascular-Risk-Assessment/
│
├── 📁 Artifacts/
│   ├── processed data
│   ├── trained model artifacts
│   └── preprocessing artifacts
│
├── 📁 Notebook_Experiments/
│   └── experimentation notebooks
│
├── 📁 src/
│   └── Heart/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       │
│       ├── pipeline/
│       │   ├── prediction_pipeline.py
│       │   └── train_pipeline.py
│       │
│       ├── exception.py
│       ├── logger.py
│       └── utils.py
│
├── 📁 static/
│   ├── stylesheets
│   └── risk_history.json
│
├── 📁 templates/
│   ├── index.html
│   └── result.html
│
├── 📁 logs/
│   └── application logs
│
├── 📄 app.py
├── 📄 Dockerfile
├── 📄 Procfile
├── 📄 requirements.txt
├── 📄 setup.py
├── 📄 dvc.yaml
├── 📄 dvc.lock
├── 📄 sample_patients.csv
├── 📄 README.md
└── 📄 LICENSE
```

---

# 🛠️ Technology Stack

## Programming & Web

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white">
</p>

## Machine Learning & Data Science

<p>
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/CatBoost-FFCC00?style=flat-square">
<img src="https://img.shields.io/badge/XGBoost-189FDD?style=flat-square">
<img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white">
</p>

## Explainable AI

<p>
<img src="https://img.shields.io/badge/SHAP-Explainable%20AI-FF6F00?style=flat-square">
</p>

## MLOps & Experimentation

<p>
<img src="https://img.shields.io/badge/DVC-945DD6?style=flat-square&logo=dvc&logoColor=white">
<img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white">
</p>

## Deployment & DevOps

<p>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square">
<img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white">
</p>

---

# 📦 Key Technologies Explained

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web application and prediction interface |
| **Scikit-Learn** | ML preprocessing and model pipeline |
| **CatBoost** | Gradient boosting model |
| **XGBoost** | Gradient boosting model |
| **Pandas** | Dataset manipulation |
| **NumPy** | Numerical computation |
| **SHAP** | Model explainability |
| **DVC** | Data and pipeline versioning |
| **MLflow** | Experiment tracking |
| **Docker** | Containerization |
| **Gunicorn** | Production WSGI server |
| **Render** | Cloud deployment |
| **Git/GitHub** | Source control and collaboration |

---

# 🔬 Model Development

The project follows a structured ML development lifecycle:

### 1. Data Ingestion

The dataset is loaded and separated into training and testing components.

### 2. Data Transformation

Features are prepared for machine learning through the project's transformation pipeline.

### 3. Model Training

Multiple machine learning approaches can be evaluated to identify a suitable classification model.

### 4. Model Evaluation

The trained models are evaluated using classification-oriented metrics.

### 5. Model Persistence

The selected model and preprocessing artifacts are stored for inference.

### 6. Prediction Pipeline

A dedicated prediction pipeline transforms new patient data and generates predictions without retraining the model.

---

# 📊 Prediction Output

The application converts the model output into a user-friendly assessment.

Example:

```text
Patient Assessment
        │
        ▼
Machine Learning Prediction
        │
        ├── Prediction
        │
        ├── Probability
        │
        └── Confidence
        │
        ▼
┌────────────────────────────┐
│  Cardiovascular Risk       │
│                            │
│  LOW RISK                  │
│       or                   │
│  HIGH RISK                 │
└────────────────────────────┘
```

The backend prediction layer returns structured prediction information that can be consumed by the Flask application.

---

# 🔍 Explainable AI with SHAP

Machine learning predictions can be difficult to interpret.

This project incorporates **SHAP (SHapley Additive exPlanations)** as an explainability component to investigate how individual features influence model predictions.

This provides a pathway toward:

- Feature contribution analysis
- Model transparency
- Better interpretation of predictions
- More trustworthy ML experimentation

> Explainability is especially important in high-impact domains where simply returning a prediction is not enough.

---

# 📈 Risk Assessment History

The application includes a lightweight risk-history mechanism.

This enables previously generated assessments to be retained and reviewed rather than treating every prediction as an isolated event.

The history layer can support future enhancements such as:

- Patient assessment timelines
- Risk trend visualization
- Filtering by assessment date
- Exporting historical assessments
- Analytics dashboards

---

# 📧 Email Integration

The application also supports email-based functionality for assessment-related communication.

This demonstrates how the ML prediction layer can be connected to an external communication workflow instead of remaining isolated inside the application.

---

# 🧪 Sample Patient Data

A sample dataset is included for quick experimentation:

```text
sample_patients.csv
```

This makes it easier to test the application without manually entering every parameter.

---

# 💻 Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/mohapatranirjhala-stack/AI-Cardiovascular-Risk-Assessment.git
cd AI-Cardiovascular-Risk-Assessment
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file locally and add the environment variables required by the application.

Example:

```env
# Add your local environment configuration here.
# Never commit API keys or passwords to GitHub.
```

## 5. Start the Flask Application

```bash
python app.py
```

## 6. Open the Application

```text
http://127.0.0.1:5000
```

---

# 🐳 Run with Docker

Build the image:

```bash
docker build -t ai-cardiovascular-risk-assessment .
```

Run the container:

```bash
docker run -p 5000:5000 ai-cardiovascular-risk-assessment
```

Then open:

```text
http://localhost:5000
```

---

# ☁️ Deployment

The application is deployed as a production Flask service using:

```text
GitHub
   │
   ▼
Render
   │
   ▼
Gunicorn
   │
   ▼
Flask Application
   │
   ▼
ML Prediction Pipeline
```
### Production Server

The project uses Gunicorn for production serving.

The repository also contains:

```text
Procfile
Dockerfile
```

to support deployment workflows.

### 🌐 Live Application

**Live Demo:**  
https://ai-cardiovascular-risk-assessment-webapp.onrender.com/

> If the Render URL changes, update the link above.

---

# 🔐 Security & Configuration

Sensitive configuration must be stored using environment variables.

### Never commit:

```text
.env
API keys
API tokens
passwords
private credentials
MLflow credentials
cloud credentials
```

The `.gitignore` file is configured to prevent sensitive local configuration from being committed.

---

# 📂 DVC & Reproducibility

The project includes DVC configuration:

```text
.dvc/
dvc.yaml
dvc.lock
.dvcignore
```

DVC enables the project to move toward reproducible machine learning workflows by tracking data and pipeline stages separately from application source code.

---

# 🧩 Modular Architecture

One of the key design decisions is separating responsibilities across components.

```text
                 ┌────────────────────┐
                 │     Flask App      │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Prediction Pipeline│
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Data Transformation│
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │ Trained ML Model   │
                 └────────────────────┘
```

This makes the project easier to:

- Maintain
- Test
- Extend
- Deploy
- Debug
- Reuse for future applications

---

# 🧪 Testing

The repository includes dedicated test scripts for different components and integrations.

Examples include:

```text
test_gemini.py
test_groq.py
test_shap.py
```

These provide a foundation for validating individual AI/explainability integrations independently from the main Flask application.

---

# 🚀 Future Roadmap

The current system provides a foundation that can be expanded into a more comprehensive cardiovascular intelligence platform.

### 🔮 Planned Enhancements

- [ ] Advanced SHAP visualizations in the web UI
- [ ] Patient risk trend dashboards
- [ ] Interactive historical analytics
- [ ] Model comparison dashboard
- [ ] Automated model monitoring
- [ ] Improved calibration of prediction probabilities
- [ ] Authentication and user accounts
- [ ] Secure patient record storage
- [ ] PDF assessment report generation
- [ ] Explainable natural-language risk summaries
- [ ] Automated model retraining pipeline
- [ ] CI/CD automation
- [ ] Comprehensive unit and integration testing
- [ ] Model performance monitoring
- [ ] Accessibility improvements
- [ ] Responsive mobile-first interface

---

# 🏆 Engineering Highlights

This project demonstrates practical experience across multiple areas of modern software engineering:

```text
                    AI CARDIOVASCULAR
                     RISK ASSESSMENT
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   MACHINE LEARNING     WEB ENGINEERING     MLOps
        │                  │                  │
   • Scikit-Learn       • Flask            • DVC
   • CatBoost           • HTML/CSS         • MLflow
   • XGBoost            • Prediction API   • Artifacts
   • SHAP               • Validation       • Pipelines
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                       DEPLOYMENT
                           │
                   • Docker
                   • Gunicorn
                   • Render
                   • GitHub
```

---

# 🎓 What This Project Demonstrates

### Machine Learning

- Binary classification
- Feature preprocessing
- Model training
- Model evaluation
- Prediction pipelines
- Probability-based predictions

### Software Engineering

- Modular architecture
- Separation of concerns
- Environment-based configuration
- Logging
- Error handling
- Reusable components

### MLOps

- DVC
- MLflow
- Model artifacts
- Reproducible pipelines
- Experiment-oriented workflow

### Explainable AI

- SHAP
- Feature contribution analysis
- Interpretable prediction workflow

### DevOps

- Docker
- Gunicorn
- Cloud deployment
- Production configuration

### Full-Stack Development

- Flask backend
- HTML/CSS frontend
- Form processing
- Dynamic result rendering
- Persistent risk history
- Email workflow

---

# 🌟 Project Philosophy

> **The goal is not simply to predict — it is to build an understandable, deployable and extensible machine learning system.**

This project demonstrates the transition from:

```text
Notebook Experiment
        ↓
Machine Learning Model
        ↓
Prediction Pipeline
        ↓
Web Application
        ↓
Explainability
        ↓
Containerization
        ↓
Cloud Deployment
        ↓
Production-Oriented ML System
```

---

# 👩‍💻 Author

## Nirjhala Mohapatra

**B.Tech Computer Science Engineering | VIT Bhopal University**

Interested in:

- Artificial Intelligence
- Machine Learning
- Full-Stack Development
- Cloud Computing
- MLOps
- Intelligent Software Systems

### Connect

- GitHub: https://github.com/mohapatranirjhala-stack
- LinkedIn: https://www.linkedin.com/in/nirjhala-mohapatra

---

# ⭐ Support the Project

If you find this project interesting:

⭐ Star the repository  
🍴 Fork the project  
🐛 Report an issue  
💡 Suggest an improvement  
🔀 Submit a pull request

Every contribution and suggestion is appreciated.

---

# 📜 License

This project is distributed under the MIT License.

See the `LICENSE` file for details.

---

<p align="center">

### 🫀 From clinical data to intelligent risk assessment.

**Built with Python • Machine Learning • Explainable AI • Flask • MLOps • Docker • Cloud Deployment**

</p>
