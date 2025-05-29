# 💰 Loan Approval Predictor

A full-stack FinTech web application that predicts whether a loan should be approved based on user inputs. Built using Python, Flask, Scikit-learn, and SQLite with a Bootstrap-powered UI.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-orange.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🚀 Features

- 🔍 Predict loan approval status using a trained ML model (Logistic Regression)
- 📋 Responsive loan application form
- 💾 Submissions stored in SQLite database
- 📊 Admin dashboard to view all loan records
- ✅ Input validation for form fields
- 🧠 Clean backend logic using Flask + SQLAlchemy

---

## 🧪 Tech Stack

| Layer       | Tech                                |
|-------------|-------------------------------------|
| Frontend    | HTML, CSS, Bootstrap                |
| Backend     | Python, Flask                       |
| ML Model    | Scikit-learn, Pandas, Joblib        |
| Database    | SQLite + SQLAlchemy ORM             |
| Deployment  | Render (optional)                   |


---

## 📦 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/AayushA10/loan-approval-predictor.git
cd loan-approval-predictor
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python train_model.py
python app.py
Visit in browser
http://127.0.0.1:5000/ — submit the form
http://127.0.0.1:5000/dashboard — admin view
loan-approval-predictor/
├── app.py                  # Main Flask backend
├── train_model.py          # ML training script
├── model/loan_model.pkl    # Trained model file
├── templates/              # index.html, dashboard.html
├── static/                 # (optional CSS)
├── submissions.db          # SQLite DB
├── requirements.txt
└── README.md
