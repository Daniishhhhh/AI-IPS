import numpy as np
from .model_loader import xgb_primary, xgb_infiltration, scaler, label_encoder


def ips_predict(sample):
    """
    sample: numpy array of shape (1, 57)
    """

    # Scale
    sample_scaled = scaler.transform(sample)

    # Primary model prediction
    probs = xgb_primary.predict_proba(sample_scaled)[0]
    pred_class = np.argmax(probs)
    confidence = np.max(probs)

    attack_label = label_encoder.inverse_transform([pred_class])[0]

    # Secondary infiltration check
    if confidence < 0.90:
        probs_secondary = xgb_infiltration.predict_proba(sample_scaled)[0]
        pred_secondary = np.argmax(probs_secondary)
        attack_label_secondary = label_encoder.inverse_transform([pred_secondary])[0]

        if attack_label_secondary == "INFILTRATION":
            attack_label = "INFILTRATION"
            confidence = np.max(probs_secondary)

    return attack_label, float(confidence)
