import streamlit as st
from detector import predict_file  # import function from detector.py

# -------------------------
# UI
# -------------------------
st.set_page_config(page_title="AI Ransomware Detector", layout="centered")
st.title("🔐 AI Ransomware Detector")
st.subheader("Upload a file to check if it is ransomware")

# File upload
uploaded_file = st.file_uploader(
    "Choose a file",
    type=["txt", "exe", "py", "docx", "pdf"]
)

if uploaded_file is not None:
    try:
        # Read file bytes
        file_bytes = uploaded_file.read()

        # Call detector
        result = predict_file(file_bytes)

        # Show result
        if result == 1:
            st.error("⚠️ Ransomware Detected!")
        else:
            st.success("✅ File is Safe!")

    except Exception as e:
        st.error(f"Error processing file: {e}")
