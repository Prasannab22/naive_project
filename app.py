import streamlit as st
import pickle

model = pickle.load(open("diabetes_nb.pkl","rb"))

st.title("🩺 Diabetes Prediction (Naive Bayes)")

fields=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]

vals=[]
for f in fields:
    vals.append(st.number_input(f,0.0))

if st.button("Predict"):
    pred=model.predict([vals])[0]
    st.success("Diabetic" if pred==1 else "Not Diabetic")
