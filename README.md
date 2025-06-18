# Cvd-risk-checker App.
CVD Risk Checker App: This interactive Streamlit app extends my previous cardiovascular disease (CVD) risk analysis project. It uses the same trained logistic regression model to help users input their health details and instantly check their risk of CVD. Built with Python, Scikit-learn, and Streamlit.

# 🫀 CVD Risk Checker App

This is a simple, web-based health tool that helps users check their risk of **Cardiovascular Disease (CVD)** using a machine learning model trained on real patient data.

Built with **Python**, **Streamlit**, and **Scikit-learn**, this app is easy to use even for older users and it works on mobile and desktop.

---

## 🔗 Live Demo

👉 [Click here to use the app](https://cvd-risk-checker-wkmr9pdtlscwwrqzeeeixp.streamlit.app/)

---

## 🧠 How It Works

1. The user enters basic health information:
   - Age, Gender
   - Blood Pressure (systolic/diastolic)
   - Weight, Height
   - Cholesterol & Glucose levels
   - Lifestyle (smoking, alcohol, activity)

2. The app scales the inputs and sends them to a **Logistic Regression model** trained on over 68,000 medical records.

3. It returns:
   - ✅ **Low risk** or ⚠️ **High risk**
   - With a confidence percentage

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- NumPy
- Joblib

---

## 📁 Project Structure

```plaintext
📦 cvd-risk-checker
├── app.py              # Streamlit app interface
├── cvd_model.pkl       # Trained logistic regression model
├── cvd_scaler.pkl      # Feature scaler
└── requirements.txt    # Python dependencies
```



---

## ⚠️ Disclaimer

This tool is for educational and awareness purposes only.  
It does not replace medical diagnosis. Always consult a qualified healthcare provider.

---

## 🙌 Special Thanks

This app is a continuation of my previous CVD data analysis project.  
Check out the full notebook and model training process here:  
📎 [Google Colab Notebook](https://colab.research.google.com/drive/1-xM-4wTFAPAEeGv1pzTdb2kZTUme4VLm?usp=sharing)



