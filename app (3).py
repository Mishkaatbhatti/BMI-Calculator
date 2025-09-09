import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("⚖️ BMI Calculator")

st.markdown(
    """
    This app calculates your **Body Mass Index (BMI)**  
    Enter your details below 👇
    """
)

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.5)
height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    st.success(f"Your BMI is: **{bmi:.2f}**")

    # BMI categories
    if bmi < 18.5:
        st.info("💡 You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ You are overweight.")
    else:
        st.error("🚨 You are obese.")
