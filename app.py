from flask import Flask, render_template, request
import joblib
import numpy as np
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Load ML model
model = joblib.load("model/loan_model.pkl")

# DB model
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer)
    married = db.Column(db.Integer)
    education = db.Column(db.Integer)
    income = db.Column(db.Float)
    loan_amount = db.Column(db.Float)
    credit_history = db.Column(db.Float)
    property_area = db.Column(db.Integer)
    prediction = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    education = int(request.form['education'])
    applicant_income = float(request.form['income'])
    loan_amount = float(request.form['loan_amount'])
    credit_history = float(request.form['credit_history'])
    property_area = int(request.form['property_area'])

    input_data = np.array([[gender, married, education, applicant_income, loan_amount, credit_history, property_area]])
    prediction = model.predict(input_data)[0]
    result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"

    submission = LoanApplication(
        gender=gender,
        married=married,
        education=education,
        income=applicant_income,
        loan_amount=loan_amount,
        credit_history=credit_history,
        property_area=property_area,
        prediction=result
    )
    db.session.add(submission)
    db.session.commit()

    return render_template('index.html', result=result)  # <== this was missing


    # Prepare input
    input_data = np.array([[gender, married, education, applicant_income, loan_amount, credit_history, property_area]])
    prediction = model.predict(input_data)[0]
    result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
@app.route('/dashboard')
def dashboard():
    all_submissions = LoanApplication.query.order_by(LoanApplication.timestamp.desc()).all()
    return render_template('dashboard.html', submissions=all_submissions)


    # Save to DB
    submission = LoanApplication(
        gender=gender,
        married=married,
        education=education,
        income=applicant_income,
        loan_amount=loan_amount,
        credit_history=credit_history,
        property_area=property_area,
        prediction=result
    )
    db.session.add(submission)
    db.session.commit()

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
