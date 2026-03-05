import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("🎓 Student Placement Prediction ")

df=pd.read_csv("placement.csv")
x=df[["cgpa","placement_exam_marks"]]
y=df["placed"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=LinearRegression()
model.fit(x_train, y_train)

cgpa=st.number_input("Enter your cgpa:")
if cgpa=="" :
    st.warning("it can not be empty  ❌")
marks=st.number_input("Enter your placement marks:")
if marks=="":
    st.warning("it can not be empty  ❌")
#button method to create interactive buttons
if st.button("Placement prediction"):
    pred=model.predict([[cgpa,marks]])
    if pred[0] >= 0.5:
        st.success("Congratulations! You are Placed")
        st.balloons()
    else:
        st.error("Not Placed ❌")
        

    
else:
    st.write("Button not clicked yet.")