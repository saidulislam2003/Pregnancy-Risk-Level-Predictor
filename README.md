# 🤰 Pregnancy Risk Level Predictor

![Streamlit App](https://img.shields.io/badge/Deployed-Yes-brightgreen?style=flat&logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)

A Machine Learning-powered web application that predicts the **risk level of pregnancy** based on various medical and demographic features. This tool is designed to assist medical professionals and expectant mothers in gaining early insights into potential pregnancy-related risks.

🔗 **Live App**: [pregnancy-risk-level-predictor-saidulislam2003.streamlit.app](https://pregnancy-risk-level-predictor-saidulislam2003.streamlit.app/)

## 🧠 Model Info

The model is trained using the [Pregnancy Risk Classification Dataset](https://www.kaggle.com/datasets/saurabhshahane/pregnancy-risk-classification), which includes clinical and demographic indicators. A **Random Forest Classifier** was chosen due to its robustness and accuracy in handling imbalanced and nonlinear data.

## 📊 Features Used

- Age
- Blood Pressure
- Blood Sugar
- Body Temperature
- Heart Rate
- Diabetes
- Mental Health Condition
- Other Medical Conditions

## 🚀 How It Works

1. User inputs health and medical data into the form.
2. The model predicts whether the pregnancy risk is:
   - **Low**
   - **High**
3. A risk level is displayed instantly on-screen.

## 📸 Screenshots

![App Screenshot](https://i.imgur.com/yDcQ8Qe.png)

## 🛠️ Tech Stack

- **Python 3.7+**
- **Streamlit** for the web interface
- **Scikit-learn** for model training
- **Pandas & NumPy** for data handling
- **Joblib** for model serialization

## 📂 Repository Structure
Pregnancy-Risk-Level-Predictor/
│
├── app.py # Streamlit web app
├── model/
│ └── rf_model.pkl # Trained Random Forest model
├── pregnancy.csv # Dataset used for training
├── requirements.txt # Python dependencies
└── README.md # Project documentation
