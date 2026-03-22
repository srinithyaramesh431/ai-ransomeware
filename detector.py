import streamlit as st
import pickle

st.title("🔐 AI Ransomware Detector")
st.subheader("Upload a file to check if it is ransomware")

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["txt","exe","py", "docx", "pdf"])  

if uploaded_file is not None:
    # Load your ML model (make sure model.pkl is in repo root)
    model = pickle.load(open("model.pkl", "rb"))

    # Read file bytes (example, adapt to your model)
    file_bytes = uploaded_file.read()
    
    # Prediction
    prediction = model.predict([file_bytes])  # replace with your ML model logic

    # Show result
    if prediction[0] == 1:
        st.error("⚠️ Ransomware Detected!")
    else:
        st.success("✅ File is Safe!")
