# 🛡️ AI-IPS — Intelligent Intrusion Prevention System

## Real-Time AI-Powered Network Threat Detection & Prevention

AI-IPS is a **real-time Intrusion Detection and Prevention System (IDPS)** that leverages **Machine Learning and Deep Learning models** to monitor live network traffic, detect malicious behavior, classify attack types, and automatically recommend or trigger mitigation actions.

The system combines **flow-based network monitoring**, **hybrid AI classification**, and **automated decision engines** to provide an intelligent cybersecurity defense layer suitable for research, enterprise environments, and academic projects.

---

## 🎯 Project Objectives

Modern networks face continuously evolving cyber threats. Traditional signature-based systems struggle to detect:

* Zero-day attacks
* Unknown anomalies
* Sophisticated attack patterns
* High-volume distributed threats

AI-IPS aims to solve these challenges by providing:

✅ Real-time packet capture and flow extraction
✅ AI-driven threat detection using hybrid models
✅ Attack classification with confidence scoring
✅ Automated prevention recommendations
✅ Extensible architecture for deployment environments
✅ Research-grade cybersecurity experimentation platform

---

## 🚀 Key Features

### 🔍 Real-Time Network Monitoring

* Live packet capture using **Scapy**
* Automatic flow generation (NetFlow-like features)
* Supports TCP and UDP protocols
* Configurable flow timeout and feature extraction

### 🧠 Hybrid AI Detection Engine

Two-stage AI pipeline:

1️⃣ **Binary Classification (UNSW-NB15 Model)**

* Detects whether traffic is benign or malicious

2️⃣ **Multi-Class Classification (CIC-IDS Flow Model)**

* Identifies attack category (DoS, Probe, Exploit, etc.)

This hybrid architecture improves both **accuracy and interpretability**.

### ⚡ Automated Decision Engine

* Converts AI predictions into actionable responses
* Example actions:

  * ALLOW
  * ALERT
  * BLOCK
  * MONITOR

Designed for integration with firewalls and SIEM tools.

### 📊 Feature Engineering Pipeline

Extracted features include:

* Flow duration
* Packet counts
* Byte counts
* Packet rate
* TCP flag counts (SYN, ACK, RST)
* Flow statistics

Compatible with ML training datasets.

### 🛠️ Prevention Module (Extensible)

* Architecture supports automatic blocking via:

  * Windows Firewall
  * iptables
  * Network controllers
* Currently includes decision-level recommendations

### 🌐 API Integration

* FastAPI backend for:

  * Predictions
  * Monitoring
  * Integration with dashboards
  * External systems

### 📈 Model Confidence Scoring

Each prediction includes:

* Attack type
* Confidence score
* Recommended action

---

## 🧠 AI Architecture

Hybrid Detection Pipeline:

Packet Capture → Flow Extraction → Feature Engineering →
Binary Model (UNSW) → If Malicious → Multi-Class Model (CIC) →
Decision Engine → Prevention Action

This approach reduces false positives while maintaining high detection capability.

---

## 🏗️ System Architecture

### 1️⃣ Data Layer

* Real-time packets
* Flow generation
* Feature vectors

### 2️⃣ AI Layer

* Binary intrusion model
* Multi-class attack classifier
* Scalers and encoders

### 3️⃣ Decision Layer

* Hybrid decision logic
* Action mapping

### 4️⃣ Prevention Layer

* Firewall integration (extensible)
* Response automation

### 5️⃣ API Layer

* FastAPI endpoints
* Dashboard integration

---

## 🛠️ Tech Stack

**Programming Language**

* Python 3.10+

**Networking**

* Scapy

**Machine Learning**

* Scikit-learn
* TensorFlow / Keras (for DL models if used)

**Backend**

* FastAPI
* Uvicorn

**Data Processing**

* Pandas
* NumPy

**Model Storage**

* Joblib / Pickle

**Deployment**

* Virtual Environment / Docker (optional)

---

## 📂 Project Structure

```
AI-IPS/
│
├── engine/
│   ├── model_loader.py        # Load trained models & scalers
│   ├── predictor.py           # Hybrid prediction pipeline
│   ├── decision_engine.py     # Action decision logic
│
├── realtime_engine/
│   ├── flow_collector.py      # Packet capture & flow extraction
│   ├── test_realtime.py       # Real-time testing script
│
├── prevention_module/
│   ├── firewall.py            # Blocking logic (optional)
│
├── models/
│   ├── unsw_model.pkl
│   ├── flow_model.pkl
│   ├── scalers/
│
├── api/
│   ├── app.py                 # FastAPI application
│
├── utils/
│
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-IPS.git
cd AI-IPS
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the System

### 🔹 Start Real-Time Packet Monitoring

```bash
python -m realtime_engine.test_realtime
```

Run terminal as **Administrator** for packet capture permissions.

### 🔹 Start API Server

```bash
uvicorn api.app:app --reload
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing with Traffic

You can generate traffic using:

```bash
ping google.com
```

Or simulate connections:

```bash
Test-NetConnection 127.0.0.1 -Port 80
```

For malicious simulation tools (lab only):

* Nmap
* Hping3
* Metasploit

---

## 📊 Example Output

```
Flow expired: ('192.168.1.5', '8.8.8.8', 443, 52344, 'tcp')
Duration: 3.02
Packets: 12
Bytes: 2048

AI RESULT:
{
  'attack_type': 'BENIGN',
  'confidence': 0.9999,
  'recommended_action': 'ALLOW'
}
```

---

## 🔮 Future Enhancements

* Deep Learning models (BiLSTM / CNN)
* Web dashboard visualization
* Automated firewall blocking
* SIEM integration
* Distributed monitoring agents
* Kubernetes deployment
* Threat intelligence feeds
* Explainable AI (XAI) insights

---

## ⚠️ Security & Ethical Use

This project is intended for:

* Educational use
* Research environments
* Authorized security testing

Do NOT deploy or test on networks without permission.

---

## 🤝 Contribution

Contributions are welcome.

Steps:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Developed as an AI-based cybersecurity research and implementation project.

---

## ⭐ Vision

> “Intelligent networks require intelligent defense.”

AI-IPS aims to combine artificial intelligence with cybersecurity to create adaptive, real-time protection systems.

---
