import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os

# Load training dataset
df = pd.read_csv("train_loan.csv")

# Drop rows with missing values (for simplicity)
df.dropna(inplace=True)

# Encode categorical columns
categorical_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']
encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le  # Save encoder if needed later

# Define features and target
X = df[['Gender', 'Married', 'Education', 'ApplicantIncome', 'LoanAmount', 'Credit_History', 'Property_Area']]
y = df['Loan_Status']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.2f}")

# Save model to /model/ directory
if not os.path.exists("model"):
    os.makedirs("model")

joblib.dump(model, "model/loan_model.pkl")
print("✅ Model saved at model/loan_model.pkl")
