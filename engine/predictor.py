import pandas as pd
from engine.model_loader import xgb_model, scaler, label_encoder

class_names = list(label_encoder.classes_)
infiltration_index = class_names.index("INFILTRATION")
INFILTRATION_THRESHOLD = 0.45


def ips_predict(features_dict):

    feature_names = list(scaler.feature_names_in_)

    # Convert to DataFrame in correct order
    X = pd.DataFrame([features_dict])[feature_names]

    # Scale once
    X_scaled = scaler.transform(X)

    # Predict probabilities
    probabilities = xgb_model.predict_proba(X_scaled)[0]

    # Threshold override
    if probabilities[infiltration_index] > INFILTRATION_THRESHOLD:
        prediction = infiltration_index
    else:
        prediction = probabilities.argmax()

    attack_label = label_encoder.inverse_transform([prediction])[0]
    confidence = float(probabilities[prediction])

    return attack_label, confidence
