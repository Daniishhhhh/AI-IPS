# ==========================================================
# AI-IPS Real-Time Flow Collector
# ==========================================================

from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
from typing import Dict, Tuple, Optional
import time
import pandas as pd

from engine.predictor import predict_hybrid
from engine.decision_engine import hybrid_decision


# ==========================================================
# Configuration
# ==========================================================

FLOW_TIMEOUT = 10  # seconds


# ==========================================================
# Flow Type Definitions
# ==========================================================

FlowKey = Tuple[str, str, int, int, str]
FlowValue = Dict[str, Optional[float]]


# ==========================================================
# Flow Storage
# ==========================================================

flows: Dict[FlowKey, FlowValue] = defaultdict(
    lambda: {
        "start_time": None,
        "end_time": None,
        "packet_count": 0,
        "byte_count": 0,
        "syn_count": 0,
        "ack_count": 0,
        "rst_count": 0,
    }
)


# ==========================================================
# Packet Processor
# ==========================================================

def process_packet(packet):

    if IP not in packet:
        return

    ip_layer = packet[IP]

    protocol = None
    sport = None
    dport = None
    flags = 0

    # -----------------------------
    # TCP
    # -----------------------------
    if TCP in packet:
        protocol = "tcp"
        sport = int(packet[TCP].sport)
        dport = int(packet[TCP].dport)
        flags = int(packet[TCP].flags)

    # -----------------------------
    # UDP
    # -----------------------------
    elif UDP in packet:
        protocol = "udp"
        sport = int(packet[UDP].sport)
        dport = int(packet[UDP].dport)

    else:
        return

    flow_key: FlowKey = (
        ip_layer.src,
        ip_layer.dst,
        sport,
        dport,
        protocol,
    )

    flow = flows[flow_key]
    now = time.time()

    # First packet
    if flow["packet_count"] == 0:
        flow["start_time"] = now

    flow["end_time"] = now
    flow["packet_count"] += 1
    flow["byte_count"] += len(packet)

    # TCP flag counters
    if protocol == "tcp":
        if flags & 0x02:
            flow["syn_count"] += 1
        if flags & 0x10:
            flow["ack_count"] += 1
        if flags & 0x04:
            flow["rst_count"] += 1

    print(
        f"Flow updated: {flow_key} | "
        f"Packets: {flow['packet_count']} | "
        f"Bytes: {flow['byte_count']}"
    )


# ==========================================================
# Expired Flow Detection + AI Processing
# ==========================================================

def check_expired_flows():

    now = time.time()
    expired = []

    # Identify expired flows
    for key, flow in list(flows.items()):
        if flow["end_time"] and now - flow["end_time"] > FLOW_TIMEOUT:
            expired.append(key)

    # Process expired flows
    for key in expired:

        flow = flows.pop(key)

        # Ignore extremely small flows (noise)
        if flow["packet_count"] < 3:
            continue

        duration = (
            flow["end_time"] - flow["start_time"]
            if flow["start_time"] and flow["end_time"]
            else 0.0001
        )

        src_ip, dst_ip, sport, dport, proto = key

        # ======================================================
        # Feature Engineering (Hybrid Bridge Format)
        # ======================================================

        features = {
            # -------- UNSW core --------
            "dur": duration,
            "proto": proto,
            "service": "-",
            "state": "INT",
            "spkts": flow["packet_count"],
            "dpkts": 0,
            "sbytes": flow["byte_count"],
            "dbytes": 0,
            "rate": flow["byte_count"] / duration,

            # -------- Flow features --------
            "flow_duration": duration * 1000,
            "total_fwd_packets": flow["packet_count"],
            "flow_packets_per_s": flow["packet_count"] / duration,
            "flow_bytes_per_s": flow["byte_count"] / duration,
            "syn_flag_count": flow["syn_count"],
            "ack_flag_count": flow["ack_count"],
            "rst_flag_count": flow["rst_count"],
        }

        df = pd.DataFrame([features])

        # ======================================================
        # AI Hybrid Prediction
        # ======================================================

        try:
            attack_label, confidence = predict_hybrid(df)
            result = hybrid_decision(attack_label, confidence)

            print("\n==============================")
            print("Flow expired:", key)
            print("Duration:", round(duration, 2))
            print("Packets:", flow["packet_count"])
            print("Bytes:", flow["byte_count"])
            print("AI RESULT:", result)
            print("==============================\n")

        except Exception as e:
            print("AI Processing Error:", e)


# ==========================================================
# Start Sniffing
# ==========================================================

def start_sniffing(interface=None):

    print("Starting packet capture...")

    def packet_handler(packet):
        process_packet(packet)
        check_expired_flows()

    sniff(prn=packet_handler, iface=interface, store=False)
