import streamlit as st
import pickle

st.title("🔐 AI Ransomware Detector")

# File upload
uploaded_file = st.file_uploader("Upload a file to check", type=["txt","exe","py"])  

if uploaded_file is not None:
    model = pickle.load(open("model.pkl", "rb"))
    data = uploaded_file.read()
    result = model.predict([data])  # your model logic

    if result[0] == 1:
        st.error("⚠️ Ransomware Detected!")
    else:
        st.success("✅ File is Safe!")
