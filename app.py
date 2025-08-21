import streamlit as st
import numpy as np
from predict import predict_diabetes


st.title("Diabetes Prediction App")
st.write("Input your data and check you diabetes")

age=st.number_input("Enter Age",18,100,20)
glucose=st.number_input("Enter Glucose",0,400,100)


if st.button("Predict"):
    input=[[age,glucose]]
    output=predict_diabetes(input)

    # print(output)
    # print(type(output))
    # print(output[0])

    if output==1:
        st.error("Chance of diabetes, see a doctor")
        st.snow()
    else:
        st.success("Diabetes not detected")
        st.balloons()

# while(True):
#     st.snow()