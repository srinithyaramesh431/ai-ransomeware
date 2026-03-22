import pandas as pd
import pickle
from llm_module import analyze_activity

# load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# load data
df = pd.read_csv("data1.csv", header=None)

event_count = len(df)

df['count'] = range(1, len(df)+1)
X = df[['count']]

pred = model.predict(X)

if -1 in pred:
    print("⚠️ AI Detected Suspicious Activity")
else:
    print("✅ Normal Activity")

# LLM analysis
result = analyze_activity(event_count)
print("LLM Analysis:", result)