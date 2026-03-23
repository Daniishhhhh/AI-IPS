from pydantic import BaseModel
from typing import Dict


class FlowInput(BaseModel):
    features: Dict[str, float]

    model_config = {
        "json_schema_extra": {
            "example": {
                "features": {
                    "duration": 10.0,
                    "src_bytes": 500.0,
                    "dst_bytes": 1200.0,
                    "packet_count": 4.0
                }
            }
        }
    }


class PredictionResponse(BaseModel):
    attack_type: str
    confidence: float
    recommended_action: str
    binary_latency_ms: float
    multiclass_latency_ms: float
    total_latency_ms: float