from fastapi import FastAPI
from pydantic import BaseModel

from engine.predictor import ips_predict
from engine.decision_engine import ips_decision
from utils.preprocessing import preprocess_input, FEATURE_NAMES

from utils.preprocessing import preprocess_input, FEATURE_NAMES

import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"

df = pd.read_csv("ips_api_test_sampless.csv")

correct = 0
total = 0

for index, row in df.iterrows():

    true_label = row["attack_type"]
    features = row.drop("attack_type").to_dict()

    try:
        response = requests.post(API_URL, json={"features": features})

        # Check HTTP status
        if response.status_code != 200:
            print("HTTP ERROR:", response.status_code)
            print(response.text)
            continue

        result = response.json()

        # If API returned error
        if "error" in result:
            print("API ERROR:", result["error"])
            continue

        predicted = result.get("attack_type")
        confidence = result.get("confidence")
        action = result.get("recommended_action")

        print("True:", true_label)
        print("Predicted:", predicted)
        print("Confidence:", confidence)
        print("Action:", action)
        print("-" * 50)

        total += 1
        if predicted == true_label:
            correct += 1

    except Exception as e:
        print("Request failed:", str(e))

# Print accuracy
if total > 0:
    print("\nAPI Test Accuracy:", round(correct / total, 4))
else:
    print("\nNo successful predictions made.")
