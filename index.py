import streamlit as st
import numpy as np
import pickle

# Load the trained model from notebook
with open("placement_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🎯 Placement Predictor")
st.write("Enter the details below to predict if the student is placed or not:")

# Inputs
cgpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.01)
exam_marks = st.number_input("Enter Placement Exam Marks:", min_value=0, max_value=100, step=1)

if st.button("Predict Placement"):
    input_data = np.array([[cgpa, exam_marks]])
    pred = model.predict(input_data)[0]

    if pred >= 0.5:
        st.success("Hogaya bhai, placed tu! 🎉")
    else:
        st.error("Isliye bolte h class mai dhyaan doh beta!")
        st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)