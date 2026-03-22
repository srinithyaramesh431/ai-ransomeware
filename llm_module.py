def analyze_activity(event_count):
    if event_count > 20:
        return "⚠️ High file activity detected. Possible ransomware behavior."
    elif event_count > 10:
        return "⚠️ Moderate suspicious activity detected."
    else:
        return "✅ Normal system behavior."