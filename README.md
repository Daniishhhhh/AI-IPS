🛡️ AI-IPS
Intelligent Network Intrusion Prevention System

CIC-IDS2018 + CSE-CIC-IDS2018 | XGBoost Production Model | FastAPI Deployment

📌 Project Overview

AI-IPS is a production-ready, machine learning–driven Intrusion Prevention System (IPS) designed to detect and respond to modern network attacks in real time.

This system is built using:

CIC-IDS2018 dataset

CSE-CIC-IDS2018 dataset

XGBoost (Production Model – v1.0)

Random Forest (Baseline Model)

FastAPI for inference deployment

The system performs:

Flow-level attack classification

Confidence scoring

Automated prevention decision mapping

API-based real-time detection

🎯 Problem Statement

Modern enterprise networks face increasing threats such as:

DDoS

DoS

Brute Force

Botnet

PortScan

Infiltration

Traditional signature-based IDS systems fail against evolving threats and unknown variants.

This project aims to:

Build a high-accuracy ML-based detection engine

Reduce false positives

Improve infiltration detection

Enable automated prevention decisions

Provide modular extensibility (UNSW module upcoming)

🏗️ Architecture Overview
Incoming Flow Data
        ↓
Preprocessing (Feature Order + Scaling)
        ↓
XGBoost Flow Model (v1)
        ↓
Label Decoding
        ↓
Decision Engine
        ↓
Recommended Action (IPS Response)

📊 Current Model Performance (CIC + CSE v1)
XGBoost Production Model

Accuracy: 94.99%

Weighted F1: 0.95

Strong detection for:

DDOS

DOS

BOT

PORTSCAN

BRUTEFORCE

Moderate detection for:

INFILTRATION (improvement planned)

API Validation Accuracy

End-to-end API test accuracy:

88.57%


This reflects real-world inference performance.

📁 Project Structure
AI-IPS/
│
├── api/
│   └── app.py
│
├── engine/
│   ├── model_loader.py
│   ├── predictor.py
│   └── decision_engine.py
│
├── utils/
│   └── preprocessing.py
│
├── models/
│   ├── xgb_flow_model_v1.pkl
│   ├── scaler_flow_v1.pkl
│   ├── label_encoder_flow_v1.pkl
│
├── test_api.py
├── requirements.txt
└── README.md

📦 Model Files (Stored on Google Drive)

Large models are stored separately.

Download models from:

https://drive.google.com/drive/folders/1wdymHdOO-XliM08TnqnCjhyEZ7EqhtCK


Place them inside:

AI-IPS/models/


Required files:

xgb_flow_model_v1.pkl

scaler_flow_v1.pkl

label_encoder_flow_v1.pkl

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/Daniishhhhh/AI-IPS.git
cd AI-IPS

2️⃣ Create Virtual Environment
python -m venv .venv


Activate:

Windows:

.venv\Scripts\activate


Mac/Linux:

source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Download Models

Download from Google Drive and place inside:

AI-IPS/models/

🚀 Running the API

Start server:

uvicorn api.app:app --reload


Server runs at:

http://127.0.0.1:8000


Test endpoint:

GET /


Prediction endpoint:

POST /predict

📡 Example Prediction Request
{
  "features": {
    "flow_duration": 12345,
    "flow_bytes_per_s": 4500,
    ...
  }
}


Response:

{
  "attack_type": "DDOS",
  "confidence": 0.9987,
  "recommended_action": "BLOCK_IP_IMMEDIATELY"
}

🔐 IPS Decision Mapping
Attack Type	Recommended Action
BENIGN	ALLOW
DDOS	BLOCK_IP_IMMEDIATELY
DOS	RATE_LIMIT
BRUTEFORCE	THROTTLE_AND_MONITOR
BOT	ISOLATE_HOST
PORTSCAN	BLOCK_IP_TEMPORARY
INFILTRATION	ESCALATE_TO_ADMIN
🧪 API Testing

Run:

python test_api.py


This:

Loads structured test flows

Sends requests to API

Prints prediction + confidence

Calculates accuracy

🧠 Engineering Decisions

✔ Feature order strictly preserved from scaler
✔ Production model versioning (v1)
✔ Model and preprocessing consistency enforced
✔ Separate decision engine
✔ Modular design (UNSW ready)
✔ No large files pushed to GitHub

📌 Known Limitations (v1)

Infiltration recall moderate

Trained only on CIC+CSE datasets

No real-time packet capture integration yet

🛣️ Roadmap
v1.1

Improve INFILTRATION recall

Threshold tuning

v2.0

Add UNSW-NB15 detection module

Dual-model architecture

Ensemble IPS engine

v3.0

Real-time packet capture integration

Dashboard monitoring

Containerized deployment

👨‍💻 Author

Danish Sidiq
AI Security & Network Defense Research

📜 License

This project is developed for research and academic purposes.
For enterprise usage, further validation and compliance review is recommended.

🔥 Current Status

✅ CIC+CSE Flow Model Locked
✅ API Production Ready
✅ GitHub Versioned
⏳ Moving to UNSW Module Next
