import streamlit as st
from PIL import Image

img = Image.open("bmi image.JPG")
st.image(img.resize((300,300)))

st.header("BMI CHECKER")

w = st.number_input("Weight in Kilogram",step = 0.1)
h = st.number_input("Height in Meter")

def bmi_cal(w,h):
    bmi = w/(h**2)
    bmi = round(bmi,1)
    return (bmi)

def bmi_status(bmi):
    if bmi < 18.5:
        return "You are at risk of being under weight"
    elif 18.4 < bmi < 25:
        return "You are Healthy"
    elif 24.5 < bmi < 30:
        return "You are at risk of being Obese"
    else:
        return "You are at risk of being Obese"
    
if st.button("Calculate"):
    bmi = bmi_cal(w,h)
    status = bmi_status(bmi)

    st.write(f"Your BMI is {bmi}")

    st.write(status)