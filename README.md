
# 🚀 AI Assisted Deployment Risk Platform

> Intelligent, policy-driven risk scoring for infrastructure changes.  
> Built for enterprise DevOps, regulated environments, and mission-critical systems.

---

## 🎯 What It Does

Before a deployment happens, this platform answers:

- 🔎 How risky is this change?
- 🌐 What is the blast radius?
- 👥 Who must approve it?
- 📊 Is this similar to past incidents?
- 🧾 Is this compliant and auditable?

All automatically.

---

## 🧠 Core Capabilities

✅ AI-powered change similarity (embeddings)  
✅ Dependency graph blast radius analysis (Neo4j)  
✅ Historical incident learning (ML model)  
✅ Policy-driven risk weighting (`.risk.yaml`)  
✅ GitHub App PR risk comments  
✅ Per-tenant isolation (SaaS ready)  
✅ SOC2 immutable audit trail (hash chain)  
✅ Kubernetes production deployment  
✅ Canary + Blue/Green rollout support  
✅ Billing + usage metering  
✅ Prometheus + OpenTelemetry observability  

---

# ⚙️ Architecture Overview

GitHub PR  
↓  
Webhook → FastAPI Risk Engine  
↓  
ML Feature Extraction  
↓  
Embedding Similarity Model  
↓  
Neo4j Blast Radius  
↓  
Policy Multiplier  
↓  
Risk Score + Approval Tier  
↓  
Audit Log (Immutable Hash Chain)

---

# 🛠 Installation

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Run Locally

```bash
uvicorn app.main:app --reload
```

API available at:

http://localhost:8000

---

# 🔐 Authentication (RBAC)

Generate a JWT token:

```python
from app.core.auth import create_token
token = create_token("ENGINEER")
```

Use it in requests:

Authorization: Bearer <token>

Roles supported:

- ENGINEER  
- DIRECTOR  
- VP  

Approval tier automatically escalates based on risk score.

---

# 📦 Example Usage

## 📌 Example 1 — Low Risk Change

### Input

```json
{
  "files": ["README.md"],
  "lines_added": 5,
  "lines_removed": 2,
  "dependencies": [],
  "past_incidents": [],
  "criticality": "LOW"
}
```

### Output

```json
{
  "risk_score": 10,
  "approval_required": "ENGINEER"
}
```

---

## 📌 Example 2 — High Risk Production Change

### Input

```json
{
  "files": ["k8s/deployment.yaml", "terraform/main.tf"],
  "lines_added": 200,
  "lines_removed": 80,
  "dependencies": ["payments-api", "ledger-service"],
  "past_incidents": ["INC-1001", "INC-1044"],
  "criticality": "MISSION_CRITICAL"
}
```

### Output

```json
{
  "risk_score": 82,
  "approval_required": "VP"
}
```

---

# 🤖 GitHub App Flow

1. Install GitHub App  
2. PR opened  
3. Webhook triggers risk engine  
4. Risk score posted as PR comment  
5. Deployment gate enforced via policy  

---

# 🧾 SOC2 Audit Trail

Every scoring event generates:

- Timestamp  
- Payload  
- Previous record hash  
- Current record hash  

Tamper-evident hash chaining ensures audit integrity.

---

# 🧪 ML Risk Learning

Feature Engineering Includes:

- File count  
- Lines changed  
- Dependency depth  
- Incident similarity  
- Service criticality  

Model:

- Gradient Boosting Classifier  
- Extensible to historical retraining  

Train model:

```bash
python app/ml/train.py
```

---

# ☁️ Kubernetes Deployment

### Standard Deploy

```bash
kubectl apply -f k8s/
```

### Canary Strategy

```bash
kubectl apply -f k8s/strategies/canary.yaml
```

### Blue/Green Strategy

```bash
kubectl apply -f k8s/strategies/blue-green.yaml
```

---

# 📈 Observability

Metrics:

- risk_requests_total  

Tracing:

- OpenTelemetry integrated  

Ready for:

- Prometheus  
- Grafana  
- Jaeger  

---

# 💳 Enterprise Billing

Tracks:

- Per-tenant usage  
- Risk scoring events  
- Approval escalations  

Ready for Stripe or metered SaaS integration.

---

# 🌍 SaaS Blueprint

Terraform provisions:

- AWS EKS  
- RDS PostgreSQL  
- Multi-cluster readiness  

Deploy:

```bash
cd terraform
terraform init
terraform apply
```

---

# 🏗 Multi-Tenant Isolation

Each tenant uses:

tenant_<tenant_id> schema  

Isolation enforced at database level.

---

# 📌 Why This Platform Matters

Traditional deployment tools show:

• Logs  
• Status  
• Success/Failure  

This platform adds:

✔ Predictive risk intelligence  
✔ AI-assisted approval workflows  
✔ Automated compliance guardrails  
✔ Measurable operational risk reduction  

---

# 🚀 Vision

> Make infrastructure changes measurable, explainable, and risk-aware — before they break production.
