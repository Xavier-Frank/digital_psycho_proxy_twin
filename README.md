# Digital Twin Prototype – Beyond the PIN

## Overview

This project is a **Digital Twin prototype** designed to demonstrate how transaction systems can go **beyond PIN-based authentication** by introducing **intent inference, behavioral trust, and coercion detection**.

The system shows how a user’s actions can be evaluated using a **Digital Twin intelligence layer**, instead of assuming:

> Correct PIN = Legitimate intent

This prototype focuses on detecting **abnormal user agency patterns** that may indicate:
- Social engineering
- Coercion
- Forced transactions
- Scam facilitation
- Fraud-by-proxy
- Scripted fraud flows

---

## Core Idea

Traditional systems verify **identity**.  
This system evaluates **intent authenticity**.

It introduces a **trust layer above authentication** using Digital Twin intelligence.

---

## Digital Twin Concept

Each user is represented by **one Digital Twin** composed of multiple internal dimensions:

- Behavioral Model
- Social Graph Model
- Contextual Model
- Financial Model
- Psychological Proxy Model

All dimensions work together as **one unified intelligence system** that produces a trust/risk decision.

---

## Prototype Scope

This repository implements the **Psychological Proxy Twin**, which focuses on:

> Detecting loss of user agency and coercion risk using behavioral interaction signals and session patterns.

This model does **not** analyze emotions or psychology directly.  
It uses **behavioral deviation as a proxy** for cognitive pressure and external influence.

---

## Psychological Proxy Twin

### Detects:
- Behavioral compression
- Linear scripted navigation
- Zero hesitation flows
- Abnormal speed patterns
- No-verification behavior
- Lack of autonomy signals
- Cognitive pressure proxies
- External influence signatures

### Produces:
- Risk score (0–100)
- Explainable signals
- Risk interpretation
- Fusion-ready output
- Decision intelligence data

---

## System Flow

- Session Input (USSD / mock logs)
- ↓
- Psychological Proxy Engine
- ↓
- Risk Scoring Model
- ↓
- Interpretation Engine
- ↓
- JSON Output (Fusion-ready)


---

## Project Structure

- digital_twin_prototype/
- │
- ├── app/
- │ ├── main.py
- │ ├── psych_proxy/
- │ │ ├── model.py
- │ │ ├── scorer.py
- │ │ ├── signals.py
- │ │ └── baseline.py
- │ │
- │ ├── fusion/
- │ │ └── aggregator.py # future integration layer
- │ │
- │ ├── api/
- │ │ └── server.py
- │
- ├── data/
- │ ├── baseline_users.json
- │ ├── normal_session.json
- │ └── coerced_session.json
- │
- ├── requirements.txt
- └── README.md


---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- NumPy

Chosen for:
- Rapid prototyping
- Fast iteration
- Modeling flexibility
- Demo-readiness
- Low setup complexity

---

## Setup Instructions

### 1. Create Virtual Environment
```bash
  python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows 
```

### 2.Install Dependencies
```bash
  pip install -r requirements.txt
```

### 3. Run the Server
```bash
  python app/main.py
```

### 4. Server Runs at:
- http://127.0.0.1:8000

### 5. API 

- Endpoint

- POST /psych-proxy

- Parameters
  - user_id (string)
  - session (JSON body)

#### Example Request 
    {
    "step_delay": 0.2,
    "session_time": 20,
    "corrections": 0,
    "retries": 0,
    "backtracks": 0,
    "pin_delay": 0.2,
    "amount_hesitation": 0.1,
    "linear_flow": true
    }

#### Example Response
    {
    "subtwin": "psych_proxy",
    "risk_score": 82.4,
    "signals": {
    "linear_flow": true,
    "zero_hesitation": true,
    "behavioral_compression": true
    },
    "interpretation": "Critical agency anomaly"
    }

### 6. Risk Interpretation
| Score Range | Meaning                  |
| ----------- | ------------------------ |
| 0–20        | Normal autonomy          |
| 21–40       | Mild anomaly             |
| 41–60       | Elevated pressure        |
| 61–80       | High coercion likelihood |
| 81–100      | Critical agency anomaly  |

### 7. Integration Model 
#### Each sub-twin exposes a standard interface:
    {
      "sub_twin": "psych_proxy",
      "user_id": "s2345235246346236234623"
      "risk_score": 78,
      "confidence": 0.81,
      "signals": {...},
      "interpretation": "..."
    }

### 8. Strategic Objective

- To demonstrate that Digital Twin intelligence enables a new security paradigm:
####  
    Identity Trust +
      + Behavioral Trust +
        + Context Trust +
        + Social Trust + 
        + Agency Trust
          = Transaction Trust







