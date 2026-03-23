import requests
import pandas as pd

# Change endpoint here
API_URL = "http://127.0.0.1:8000/predict/flow"

df = pd.read_csv("ips_api_test_sampless.csv")

correct = 0
total = 0

for index, row in df.iterrows():

    true_label = row["attack_type"]
    features = row.drop("attack_type").to_dict()

    response = requests.post(
        API_URL,
        json={"features": features}
    )

    if response.status_code != 200:
        print("HTTP ERROR:", response.status_code)
        print(response.text)
        continue

    result = response.json()

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

if total > 0:
    print("\nAPI Test Accuracy:", round(correct / total, 4))
else:
    print("\nNo successful predictions made.")
