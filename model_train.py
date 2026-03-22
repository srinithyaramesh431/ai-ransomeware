import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

print("Training started...")

# load data
df = pd.read_csv("data1.csv", header=None)

print("Data loaded. Rows:", len(df))

if len(df) < 5:
    print("❌ Not enough data to train model")
    exit()

# feature
df['count'] = range(1, len(df)+1)
X = df[['count']]

# train model
model = IsolationForest(contamination=0.1)
model.fit(X)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")
