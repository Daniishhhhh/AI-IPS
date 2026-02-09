import numpy as np
from engine.predictor import ips_predict
from engine.decision_engine import ips_decision


def run_demo():

    # Example dummy input (replace with real flow later)
    sample = np.random.rand(1, 57)

    attack, confidence = ips_predict(sample)
    action = ips_decision(attack, confidence)

    print("Predicted Attack:", attack)
    print("Confidence:", confidence)
    print("IPS Action:", action)


if __name__ == "__main__":
    run_demo()
