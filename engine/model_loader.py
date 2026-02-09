import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

xgb_model = joblib.load(os.path.join(MODEL_DIR, "xgb_flow_model_v1.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler_flow_v1.pkl"))
label_encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder_flow_v1.pkl"))
