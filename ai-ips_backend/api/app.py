from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from engine.predictor import (
    predict_binary,
    predict_multiclass,
    predict_hybrid
)

from engine.decision_engine import (
    unsw_decision,
    flow_decision,
    hybrid_decision
)

app = FastAPI(title="AI-IPS Hybrid Detection API")


# ==========================================================
# Input Schema
# ==========================================================
class FlowInput(BaseModel):
    features: dict


@app.get("/")
def root():
    return {"message": "AI-IPS Hybrid Engine Running"}


# ==========================================================
# 1️⃣ UNSW Binary Endpoint
# ==========================================================
@app.post("/predict/unsw")
def predict_unsw(flow: FlowInput):
    try:
        df = pd.DataFrame([flow.features])

        prediction, confidence = predict_binary(df)
        action = unsw_decision(prediction, confidence)

        return {
            "model": "UNSW-Binary",
            "prediction": int(prediction),
            "confidence": round(float(confidence), 4),
            "recommended_action": action
        }

    except Exception as e:
        return {"error": str(e)}


# ==========================================================
# 2️⃣ Flow Multi-class Endpoint
# ==========================================================
@app.post("/predict/flow")
def predict_flow(flow: FlowInput):
    try:
        df = pd.DataFrame([flow.features])

        attack_label, confidence = predict_multiclass(df)
        action = flow_decision(attack_label, confidence)

        return {
            "model": "CIC+CSE-Flow",
            "attack_type": attack_label,
            "confidence": round(float(confidence), 4),
            "recommended_action": action
        }

    except Exception as e:
        return {"error": str(e)}


# ==========================================================
# 3️⃣ Hybrid Gateway Endpoint
# ==========================================================
@app.post("/predict")
def predict(flow: FlowInput):
    try:
        df = pd.DataFrame([flow.features])

        attack_label, confidence = predict_hybrid(df)

        result = hybrid_decision(attack_label, confidence)

        return result

    except Exception as e:
        return {"error": str(e)}
