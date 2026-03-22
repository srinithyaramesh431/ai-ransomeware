import streamlit as st
import pickle

st.title("🔐 AI Ransomware Detector")

# File upload
uploaded_file = st.file_uploader("Choose a file to check", type=["txt","exe","py"])  

if uploaded_file is not None:
    # Load your ML model
    model = pickle.load(open("model.pkl", "rb"))

    # Read file content (example, depends on your model)
    data = uploaded_file.read()
    result = model.predict([data])  # replace with your model logic

    # Show prediction
    if result[0] == 1:
        st.error("⚠️ Ransomware Detected!")
    else:
        st.success("✅ File is Safe!")
