import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="CVD Risk Checker", layout="centered")

st.title("🫀 Check Your Heart Risk")

st.markdown("""
👋 **Welcome!**

This simple tool helps you check if you're at risk of **heart disease**.

Please enter your health info below. If you’re not sure, ask someone to help you.

📝 **Note:** This is not a medical diagnosis. It’s just a helpful early check.
""")


model = joblib.load('cvd_model.pkl')
scaler = joblib.load('cvd_scaler.pkl')

st.title("🫀 CVD Risk Checker")
st.markdown("Enter your health info to check your risk for cardiovascular disease.")

age = st.number_input("Age (years)", 1, 120, 50)
gender = st.radio("Gender", ["Male", "Female"])
height = st.number_input("Height (cm)", 100, 250, 170)
weight = st.number_input("Weight (kg)", 30, 200, 70)
ap_hi = st.number_input("Systolic BP", 80, 250, 120)
ap_lo = st.number_input("Diastolic BP", 40, 180, 80)
cholesterol = st.selectbox("Cholesterol Level", [1, 2, 3])
gluc = st.selectbox("Glucose Level", [1, 2, 3])
smoke = st.radio("Do you smoke?", ["No", "Yes"])
alco = st.radio("Do you drink alcohol?", ["No", "Yes"])
active = st.radio("Are you physically active?", ["No", "Yes"])

gender = 1 if gender == "Male" else 0
smoke = 1 if smoke == "Yes" else 0
alco = 1 if alco == "Yes" else 0
active = 1 if active == "Yes" else 0

# Check blood pressure status
def classify_bp(systolic, diastolic):
    if systolic > 180 or diastolic > 120:
        return "Hypertensive Crisis 🚨"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2 🔴"
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "Hypertension Stage 1 🟠"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated 🟡"
    elif systolic < 90 or diastolic < 60:
        return "Low 🟣"
    else:
        return "Normal 🟢"

bp_status = classify_bp(ap_hi, ap_lo)
st.markdown(f"### 🧾 Your Blood Pressure Status: **{bp_status}**")


if st.button("Check My Risk"):
    input_data = np.array([[age, gender, height, weight, ap_hi, ap_lo,
                            cholesterol, gluc, smoke, alco, active]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High risk of CVD ({probability * 100:.2f}% chance)")
    else:
        st.success(f"✅ Low risk of CVD ({(1 - probability) * 100:.2f}% chance)")

st.caption("⚠️ This tool is for educational use only. Please consult a doctor for medical advice.")

st.markdown("---")
st.markdown("""
<p style='text-align: center; font-size: 16px;'>
    Built with ❤️ by <strong>Eucharia Ogonna</strong><br>
    <a href='https://github.com/EuchariaOgonna' target='_blank'>GitHub</a> | 
    <a href='mailto:nwankwoeucharia33@gmail.com'>Email</a>
</p>
""", unsafe_allow_html=True)


