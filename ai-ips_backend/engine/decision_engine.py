# ==========================================================
# HYBRID Decision Engine
# Final Clean Production Version
# ==========================================================

def hybrid_decision(attack_label: str, confidence: float) -> str:
    """
    Determines final action based on predicted attack label
    and confidence score.
    Returns ONLY the recommended action as string.
    """

    action_map = {
        "BENIGN": "ALLOW",
        "BOT": "ISOLATE_HOST",
        "DDOS": "BLOCK_IP_IMMEDIATELY",
        "DOS": "RATE_LIMIT",
        "BRUTEFORCE": "THROTTLE_AND_MONITOR",
        "PORTSCAN": "BLOCK_IP_TEMPORARY",
        "INFILTRATION": "ESCALATE_TO_ADMIN"
    }

    # Safety fallback
    if confidence is None:
        confidence = 0.0

    # Low confidence → monitor only
    if confidence < 0.60:
        return "MONITOR"

    # High confidence → mapped action
    return action_map.get(attack_label, "MONITOR")