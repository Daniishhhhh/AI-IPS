import pandas as pd
import sqlite3
from fastapi import APIRouter, HTTPException, Query

from api.schemas import FlowInput, PredictionResponse
from database.event_logger import log_event
from engine.decision_engine import hybrid_decision
from engine.model_loader import flow_scaler
from engine.predictor import predict_hybrid

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(flow: FlowInput):
    try:
        df = pd.DataFrame([flow.features])

        result = predict_hybrid(df)

        decision = hybrid_decision(
            result["attack_type"],
            result["confidence"]
        )

        response_data = {
            "attack_type": result["attack_type"],
            "confidence": round(float(result["confidence"]), 4),
            "recommended_action": decision,
            "binary_latency_ms": result["binary_latency_ms"],
            "multiclass_latency_ms": result["multiclass_latency_ms"],
            "total_latency_ms": result["total_latency_ms"]
        }

        log_event(
            response_data["attack_type"],
            response_data["confidence"],
            response_data["recommended_action"],
            response_data["total_latency_ms"]
        )

        return response_data

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Inference error: {str(e)}"
        )


@router.get("/debug/features")
def get_required_features():
    return {
        "flow_features": list(flow_scaler.feature_names_in_)
    }


@router.get("/events")
def get_all_events(limit: int = Query(50, ge=1, le=500)):
    try:
        conn = sqlite3.connect("logs.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM security_events
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch events: {str(e)}"
        )


@router.get("/events/recent")
def get_recent_events():
    try:
        conn = sqlite3.connect("logs.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM security_events
            ORDER BY id DESC
            LIMIT 10
        """)

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch recent events: {str(e)}"
        )


@router.get("/events/block-only")
def get_block_events():
    try:
        conn = sqlite3.connect("logs.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM security_events
            WHERE recommended_action LIKE 'BLOCK%'
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch blocked events: {str(e)}"
        )