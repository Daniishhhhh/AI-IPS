import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"

df = pd.read_csv("ips_api_test_sampless.csv")

correct = 0
total = 0

for _, row in df.iterrows():

    true_label = row["attack_type"]
    features = row.drop("attack_type").to_dict()

    try:
        response = requests.post(
            API_URL,
            json={"features": features}
        )

        # Check HTTP status
        if response.status_code != 200:
            print("HTTP ERROR:", response.status_code)
            print(response.text)
            continue

        result = response.json()

        # API returned internal error
        if "error" in result:
            print("API ERROR:", result["error"])
            continue

        predicted = result["attack_type"]
        confidence = result["confidence"]
        action = result["recommended_action"]

        print(f"True: {true_label}")
        print(f"Predicted: {predicted}")
        print(f"Confidence: {confidence}")
        print(f"Action: {action}")
        print("-" * 50)

        total += 1
        if predicted == true_label:
            correct += 1

    except Exception as e:
        print("Request failed:", str(e))

if total > 0:
    print("\nAPI Test Accuracy:", round(correct / total, 4))
else:
    print("\nNo successful predictions made.")
