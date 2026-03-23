import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ==========================================================
# UNSW Binary Model
# ==========================================================

unsw_model = joblib.load(os.path.join(MODEL_DIR, "xgb_unsw_binary_v1.pkl"))
unsw_scaler = joblib.load(os.path.join(MODEL_DIR, "unsw_scaler_v1.pkl"))
unsw_feature_order = joblib.load(os.path.join(MODEL_DIR, "unsw_feature_order_v1.pkl"))

# ==========================================================
# CIC+CSE Multi-class Model
# ==========================================================

flow_model = joblib.load(os.path.join(MODEL_DIR, "xgb_flow_model_v1.pkl"))
flow_scaler = joblib.load(os.path.join(MODEL_DIR, "scaler_flow_v1.pkl"))
flow_label_encoder = joblib.load(os.path.join(MODEL_DIR, "label_encoder_flow_v1.pkl"))
