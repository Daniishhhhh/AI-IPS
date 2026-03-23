# 🛡️ AI-IPS — AI-Powered Intrusion Prevention System

## 📌 Overview

AI-IPS is a **real-time AI-powered Intrusion Detection and Prevention System** designed to monitor network traffic, detect malicious activity, classify attack types, and recommend automated security actions.

The system combines:

* **Machine Learning-based threat detection**
* **Real-time network flow processing**
* **Security decision intelligence**
* **Interactive monitoring dashboard**

This project bridges the gap between **academic ML models** and **practical cybersecurity systems**, demonstrating how AI can be integrated into real-world network defense pipelines.

---

## 🎯 Objectives

* Detect malicious network traffic in real-time
* Classify different types of cyber attacks
* Provide automated prevention recommendations
* Maintain a persistent log of security events
* Build a deployable ML microservice (FastAPI)
* Visualize results through a frontend dashboard

---

## 🏗️ System Architecture

```
                 ┌──────────────────────────────┐
                 │   Network Traffic (Packets)  │
                 └──────────────┬───────────────┘
                                │
                                ▼
                    ┌─────────────────────┐
                    │  Scapy Packet Sniff │
                    └─────────┬──────────┘
                              │
                              ▼
                ┌───────────────────────────┐
                │ Flow Aggregation Engine   │
                │ (Session-based grouping)  │
                └─────────┬─────────────────┘
                          │
                          ▼
                ┌───────────────────────────┐
                │ Feature Extraction Layer  │
                └─────────┬─────────────────┘
                          │
                          ▼
        ┌──────────────────────────────────────────┐
        │ Hybrid AI Detection Pipeline             │
        │                                          │
        │  Stage 1: Binary Classifier (UNSW-NB15)  │
        │  → Benign / Attack                       │
        │                                          │
        │  Stage 2: Multi-class Model (CIC-IDS)    │
        │  → DDOS / DOS / BOT / etc                │
        └─────────┬────────────────────────────────┘
                  │
                  ▼
        ┌──────────────────────────────┐
        │ Decision Engine              │
        │ (Policy-based responses)     │
        └─────────┬────────────────────┘
                  │
                  ▼
        ┌──────────────────────────────┐
        │ Actions                      │
        │ ALLOW / BLOCK / ALERT        │
        └─────────┬────────────────────┘
                  │
                  ▼
        ┌──────────────────────────────┐
        │ Logging (SQLite DB)          │
        └─────────┬────────────────────┘
                  │
                  ▼
        ┌──────────────────────────────┐
        │ Frontend Dashboard (Next.js) │
        └──────────────────────────────┘
```

---

## 🤖 Machine Learning Models

### 1️⃣ Binary Classification Model

* **Dataset:** UNSW-NB15
* **Purpose:** Detect whether traffic is malicious or benign
* **Algorithm:** XGBoost / Random Forest
* **Output:** Binary (0 = Benign, 1 = Attack)

---

### 2️⃣ Multi-Class Classification Model

* **Dataset:** CIC-IDS / CSE-CIC
* **Purpose:** Identify specific attack type
* **Algorithm:** XGBoost
* **Output Classes:**

  * BENIGN
  * DDOS
  * DOS
  * BOT
  * BRUTEFORCE
  * PORTSCAN
  * INFILTRATION

---

### 3️⃣ Hybrid Detection Pipeline

* Stage 1 filters traffic (fast binary detection)
* Stage 2 classifies attack type (only if needed)
* Improves efficiency and scalability

---

## 🛡️ Attack Types Detected

| Attack Type  | Description                   |
| ------------ | ----------------------------- |
| BENIGN       | Normal traffic                |
| DDOS         | Distributed Denial of Service |
| DOS          | Denial of Service             |
| BOT          | Botnet activity               |
| BRUTEFORCE   | Password guessing attacks     |
| PORTSCAN     | Port probing                  |
| INFILTRATION | Unauthorized internal access  |

---

## ⚙️ Decision Engine Logic

The system maps predictions to actions:

| Attack Type  | Action               |
| ------------ | -------------------- |
| BENIGN       | ALLOW                |
| DDOS         | BLOCK_IP_IMMEDIATELY |
| DOS          | RATE_LIMIT           |
| BOT          | ISOLATE_HOST         |
| BRUTEFORCE   | THROTTLE_AND_MONITOR |
| PORTSCAN     | BLOCK_IP_TEMPORARY   |
| INFILTRATION | ESCALATE_TO_ADMIN    |

Low confidence → `MONITOR`

---

## 🚀 Features

* Real-time prediction API using FastAPI
* Hybrid ML detection pipeline
* Feature alignment to avoid data mismatch
* Latency tracking (binary + multiclass)
* SQLite-based persistent logging
* Frontend dashboard (Next.js + Tailwind)
* Manual testing via JSON input
* Color-coded attack visualization

---

## 🧪 API Endpoints

### POST `/predict`

Predict intrusion from input features

```json
{
  "features": {
    "flow_duration": 1577064,
    "packet_length_mean": 123.0,
    ...
  }
}
```

### GET `/events/recent`

Fetch recent security events

### GET `/debug/features`

Get required feature list

---

## 💻 Tech Stack

### Backend

* Python
* FastAPI
* Scikit-learn
* XGBoost
* Pandas / NumPy
* Scapy (packet capture)
* SQLite

### Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Axios

---

## 🗂️ Project Structure

```
AI-IPS/
│
├── AI-IPS_Backend/
│   ├── api/
│   ├── engine/
│   ├── database/
│   ├── models/
│   └── scalers/
│
├── AI-IPS_Frontend/
│   ├── src/app/
│   ├── components/
│   └── lib/
│
└── README.md
```

---

## 📊 Performance Metrics

* Real-time inference latency: **10–50 ms**
* Hybrid pipeline improves efficiency
* High confidence detection (>0.9 for attacks)
* Supports scalable deployment via API

---

## 🔄 How It Works (Flow Summary)

1. Network traffic is captured (Scapy)
2. Packets are grouped into flows
3. Features are extracted
4. Binary model checks for attack
5. Multi-class model identifies attack type
6. Decision engine determines action
7. Event is logged into database
8. Dashboard displays results

---

## ⚠️ Current Limitations

* No real firewall integration yet
* Uses offline-trained models
* Limited dataset generalization
* No distributed streaming (Kafka)

---

## 🔮 Future Enhancements

* Real firewall blocking (iptables / Windows firewall)
* Kafka-based real-time streaming
* Deep learning models (LSTM / CNN)
* Docker deployment
* Cloud deployment (AWS/GCP)
* SIEM integration
* Alert system (email/SMS)

---

## 📚 References / Sources

1. **UNSW-NB15 Dataset**
   https://research.unsw.edu.au/projects/unsw-nb15-dataset

2. **CIC-IDS2017 Dataset**
   https://www.unb.ca/cic/datasets/ids-2017.html

3. **Scapy Documentation**
   https://scapy.net/

4. **FastAPI Documentation**
   https://fastapi.tiangolo.com/

5. **XGBoost Documentation**
   https://xgboost.readthedocs.io/

6. **Scikit-learn Documentation**
   https://scikit-learn.org/

7. Research Paper:

   * *Moustafa & Slay (2015)* — UNSW-NB15 Dataset Analysis
   * *Sharafaldin et al. (2018)* — CICIDS Dataset Paper

---

## 🎯 Conclusion

AI-IPS demonstrates a **practical implementation of AI in cybersecurity**, combining:

* Real-time data processing
* Machine learning-based threat detection
* Intelligent decision-making
* Interactive monitoring

It serves as a strong foundation for building **production-grade intrusion prevention systems**.

---

## 👨‍💻 Author

Danish Sidiq
Irshad Ahmad S
Computer Science Engineering

---

## ⭐ Final Note

This project represents a transition from:
👉 Academic ML → Real-world AI system design

---
