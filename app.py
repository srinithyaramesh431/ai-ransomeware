
import streamlit as st
from real_time_detector import FileEventHandler, monitor_processes
from watchdog.observers import Observer
import threading, os

st.title("Full System Ransomware Detection Dashboard")

folder = st.text_input("Folder to Monitor", "C:/Users/Nithya/Documents")

def start_monitoring(folder):
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=True)
    observer.start()
    try:
        while True:
            monitor_processes()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

t = threading.Thread(target=start_monitoring, args=(folder,), daemon=True)
t.start()
st.success(f"Monitoring started for: {folder}")
