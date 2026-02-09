from fastapi import FastAPI
from pydantic import BaseModel

from engine.predictor import ips_predict
from engine.decision_engine import ips_decision
from utils.preprocessing import preprocess_input, FEATURE_NAMES


app = FastAPI(title="AI-IPS Flow Detection API")


class FlowInput(BaseModel):
    features: dict


@app.post("/predict")
def predict(flow: FlowInput):

    try:
        missing = [f for f in FEATURE_NAMES if f not in flow.features]
        if missing:
            return {"error": f"Missing features: {missing}"}

        processed = preprocess_input(flow.features)

        attack, confidence = ips_predict(processed)

        action = ips_decision(attack, confidence)

        return {
            "attack_type": attack,
            "confidence": round(confidence, 4),
            "recommended_action": action
        }

    except Exception as e:
        return {"error": str(e)}
