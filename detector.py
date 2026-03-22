import pickle
import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")  # must match actual filename

# Load model safely
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = pickle.load(open(MODEL_PATH, "rb"))

def predict_file(file_bytes):
    features = [file_bytes]  # adapt to your model
    prediction = model.predict([features])
    return prediction[0]
