from engine.model_loader import xgb_model, label_encoder


def ips_predict(processed_array):
    """
    Accepts already preprocessed & scaled numpy array.
    Returns attack label and confidence.
    """

    prediction = xgb_model.predict(processed_array)[0]
    probabilities = xgb_model.predict_proba(processed_array)[0]

    attack_label = label_encoder.inverse_transform([prediction])[0]
    confidence = float(max(probabilities))

    return attack_label, confidence
