import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import xgboost
from xgboost import XGBClassifier

# Function to train the model
def train_model(data):
    # Handling missing values
    imputer = SimpleImputer(strategy="mean")
    data.iloc[:, :-1] = imputer.fit_transform(data.iloc[:, :-1])

    # Splitting the data into features and target
    X = data.drop('Potability', axis=1)
    y = data['Potability']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training the Random Forest Classifier
    model = XGBClassifier(random_state=42)
    model.fit(X_train, y_train)

    return model

# Load the dataset
def load_data():
    data = pd.read_csv('water_potability.csv')
    return data

# Streamlit app
st.title("Water Quality Test")
st.write("This application predicts the potability of water based on provided parameters.")

# Load the dataset
data = load_data()
st.write("Dataset Loaded Successfully!")

# Train the model
st.write("Training the model...")
model = train_model(data)
st.write("Model trained successfully!")

# User input
st.header("Enter Water Parameters")
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
solids = st.number_input("Solids (mg/L)", min_value=0.0, value=20000.0)
chloramines = st.number_input("Chloramines (mg/L)", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=250.0)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=500.0)
organic_carbon = st.number_input("Organic Carbon (mg/L)", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=80.0)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=4.0)

# Predict button
if st.button("Predict Water Quality"):
    user_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(user_data)
    result = "Potable" if prediction[0] == 1 else "Not Potable"
    st.subheader(f"Prediction: The water is {result}.")
