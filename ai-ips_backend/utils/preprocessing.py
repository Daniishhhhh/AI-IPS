import pandas as pd
from engine.model_loader import flow_scaler

# EXACT training feature order (CIC+CSE model)
FEATURE_NAMES = flow_scaler.feature_names_in_.tolist()


def preprocess_input(input_dict):
    """
    Align incoming JSON to exact CIC+CSE training schema.
    """

    df = pd.DataFrame([input_dict])

    # Add missing columns
    for col in FEATURE_NAMES:
        if col not in df.columns:
            df[col] = 0

    # Enforce exact order
    df = df[FEATURE_NAMES]

    scaled = flow_scaler.transform(df)

    return scaled
