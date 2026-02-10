from fastapi import FastAPI
from pydantic import BaseModel

from engine.predictor import ips_predict
from engine.decision_engine import ips_decision
from engine.predictor import ips_predict
from engine.decision_engine import ips_decision
from engine.model_loader import scaler


app = FastAPI(title="AI-IPS Flow Detection API")


class FlowInput(BaseModel):
    features: dict


@app.post("/predict")
def predict(flow: FlowInput):

    try:
        # Validate features
        missing = [f for f in scaler.feature_names_in_ if f not in flow.features]
        if missing:
            return {"error": f"Missing features: {missing}"}

        # Directly call predictor (no preprocessing here)
        attack, confidence = ips_predict(flow.features)

        action = ips_decision(attack, confidence)

        return {
            "attack_type": attack,
            "confidence": round(confidence, 4),
            "recommended_action": action
        }

    except Exception as e:
        return {"error": str(e)}
