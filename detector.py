
import pickle
import os

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_file(file_path):
    
    size = os.path.getsize(file_path)
    ext = os.path.splitext(file_path)[1]
    ext_map = {".exe":1, ".dll":2, ".txt":3, ".pdf":4, ".docx":5, ".xlsx":6}
    ext_feature = ext_map.get(ext.lower(), 0)
    features = [size, ext_feature]
    return model.predict([features])[0]  # 1 = suspicious / ransomware
