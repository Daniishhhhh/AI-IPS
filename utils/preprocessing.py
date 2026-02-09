import numpy as np
import pandas as pd
from engine.model_loader import scaler

# Feature order must match training order
FEATURE_NAMES = [
    # paste your 57 feature names here EXACTLY in order
]


def preprocess_input(input_dict):
    """
    input_dict: dictionary with feature_name: value
    """

    # Convert dict to DataFrame
    df = pd.DataFrame([input_dict])

    # Ensure correct column order
    df = df[FEATURE_NAMES]

    # Scale
    scaled = scaler.transform(df)

    return scaled
