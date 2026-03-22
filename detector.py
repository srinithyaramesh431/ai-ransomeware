import pickle

# Load model once
model = pickle.load(open("model.pkl", "rb"))

def predict_file(file_bytes):
    """
    Takes file bytes as input and returns 1 if ransomware, 0 if safe.
    """
    # Replace this with your actual model preprocessing if needed
    # For example, convert bytes to features
    features = [file_bytes]  # simple example
    prediction = model.predict([features])
    return prediction[0]
