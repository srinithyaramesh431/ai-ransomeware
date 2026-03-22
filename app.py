import streamlit as st
import pandas as pd

st.title("🛡️ AI Ransomware Detection Dashboard")

try:
    df = pd.read_csv("data1.csv", header=None)
    count = len(df)

    st.write("📊 Total Events:", count)

    if count > 20:
        st.error("⚠️ High Risk: Possible Ransomware Attack")
    elif count > 10:
        st.warning("⚠️ Suspicious Activity Detected")
    else:
        st.success("✅ System Normal")

    st.subheader("📄 Activity Logs")
    st.dataframe(df)

except:
    st.write("No data available yet.")
    