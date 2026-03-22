import streamlit as st
import pickle

st.title("🔐 AI Ransomware Detector")

# File upload
uploaded_file = st.file_uploader("Upload a file to check", type=["txt","exe","py"])  

if uploaded_file is not None:
    # Load model
    model = pickle.load(open("model.pkl", "rb"))

    # For example, model expects bytes or features
    # This is just pseudo code
    data = uploaded_file.read()
    result = model.predict([data])

    if result[0] == 1:
        st.error("⚠️ Ransomware Detected!")
    else:
        st.success("✅ File is Safe!")
