def ips_decision(attack_type, confidence):

    if attack_type == "DDOS":
        return "BLOCK_IP_IMMEDIATELY"

    elif attack_type == "PORTSCAN":
        return "BLOCK_IP_TEMPORARY"

    elif attack_type == "BRUTEFORCE":
        return "THROTTLE_AND_MONITOR"

    elif attack_type == "INFILTRATION":
        return "ESCALATE_TO_ADMIN"

    elif attack_type == "BOT":
        return "ISOLATE_HOST"

    elif attack_type == "DOS":
        return "RATE_LIMIT"

    else:
        return "ALLOW"
