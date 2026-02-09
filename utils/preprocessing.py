import pandas as pd
import numpy as np
from engine.model_loader import scaler

# Exact training feature order
FEATURE_NAMES = list(scaler.feature_names_in_)


def preprocess_input(input_dict):
    """
    Converts incoming JSON dict into properly ordered
    and scaled numpy array for model inference.
    """

    # Convert to DataFrame
    df = pd.DataFrame([input_dict])

    # Ensure correct feature order
    df = df[FEATURE_NAMES]

    # Convert all values to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Replace inf values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Fill missing values safely (0 is acceptable for flow features)
    df.fillna(0, inplace=True)

    # Scale
    scaled = scaler.transform(df)

    return scaled
