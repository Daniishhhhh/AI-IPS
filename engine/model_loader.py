import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_PATH = os.path.join(BASE_DIR, "models")

# Load models
xgb_primary = joblib.load(os.path.join(MODELS_PATH, "xgb_flow_primary.pkl"))
xgb_infiltration = joblib.load(os.path.join(MODELS_PATH, "xgb_flow_infiltration.pkl"))
scaler = joblib.load(os.path.join(MODELS_PATH, "scaler.pkl"))
label_encoder = joblib.load(os.path.join(MODELS_PATH, "label_encoder.pkl"))
