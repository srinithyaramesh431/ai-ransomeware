import pickle
import os

# Ensure correct path to model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = pickle.load(open(MODEL_PATH, "rb"))

def predict_file(file_bytes):
    """
    Predicts if a file is ransomware.
    Returns:
        1 -> Ransomware
        0 -> Safe
    """
    # Adapt preprocessing if needed
    features = [file_bytes]
    return model.predict([features])[0]
