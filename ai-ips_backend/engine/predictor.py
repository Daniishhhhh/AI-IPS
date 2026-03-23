import time
import pandas as pd
import numpy as np

from engine.model_loader import (
    flow_model,
    flow_scaler,
    flow_label_encoder
)


def align_features(features_df: pd.DataFrame, required_columns: list) -> pd.DataFrame:
    """
    Align incoming feature DataFrame to the exact feature order
    expected by the trained CIC flow scaler/model.
    """
    aligned_df = features_df.reindex(columns=required_columns, fill_value=0)
    aligned_df = aligned_df.replace("-", 0)
    aligned_df = aligned_df.fillna(0)
    return aligned_df


def predict_multiclass(features_df: pd.DataFrame):
    """
    Predict attack class using the CIC multiclass model.
    """
    required_cols = list(flow_scaler.feature_names_in_)
    aligned_df = align_features(features_df, required_cols)

    X_scaled = flow_scaler.transform(aligned_df)

    prediction = flow_model.predict(X_scaled)[0]
    probability = flow_model.predict_proba(X_scaled)[0]

    attack_label = flow_label_encoder.inverse_transform([prediction])[0]
    confidence = float(np.max(probability))

    return attack_label, confidence


def predict_hybrid(features_df: pd.DataFrame):
    """
    Current active inference path.
    Kept function name unchanged to avoid touching dependent route code,
    but the implementation is now CIC-only for consistency.
    """
    start_time = time.time()

    attack_label, attack_conf = predict_multiclass(features_df)

    total_latency = (time.time() - start_time) * 1000

    return {
        "attack_type": attack_label,
        "confidence": attack_conf,
        "binary_latency_ms": 0.0,
        "multiclass_latency_ms": round(total_latency, 2),
        "total_latency_ms": round(total_latency, 2)
    }