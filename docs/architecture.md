# Qubic Intelligence Whale Tracker — Architecture

This document explains how the Whale Tracker system is structured internally.  
The architecture is intentionally simple, stable, and easy for hackathon judges to verify.

---

## 🏗️ High-Level Architecture

The system processes Qubic compute events through a clean, linear pipeline:

EasyConnect Webhook  
↓  
Transform Event Data  
↓  
Classify Compute Level  
↓  
Append Row to Google Sheets  
↓  
Send Discord Alert

Each step is isolated, auditable, and easy to modify if needed.

---

## 🔌 1. EasyConnect Webhook

EasyConnect pushes real-time compute events when Qubic AI jobs begin running.

A typical event contains:
- model name  
- compute units (CU)  
- confidence score  
- timestamp  

These events are delivered directly into n8n via webhook.

---

## 🔄 2. Transform Event Data (n8n)

Raw events are normalized so the system always works with clean fields.

The transformation step:
- Renames inconsistent event keys  
- Ensures numbers are correctly typed  
- Adds a `source` field for traceability  
- Removes unused fields  

This guarantees predictable downstream behavior.

---

## 📊 3. Classification Logic

The system determines what kind of event has occurred using compute-unit thresholds:

| Compute Units | Classification |
|---------------|----------------|
| **50B+ CU** | 🐋 Whale |
| **20B–49B CU** | ⚡ High Impact |
| **< 20B CU** | Standard |

The classification is added to the event before logging.

---

## 📄 4. Google Sheets Logging

A dedicated Google Sheet stores all structured events with columns:

- timestamp  
- model_name  
- compute_units  
- confidence_score  
- classification  
- source  

Judges can instantly verify the system by watching rows appear in real time.

No credentials are exposed — the sheet uses safe integrations.

---

## 📢 5. Discord Notification

A formatted Discord embed is sent for each whale or high-impact event.

Alerts include:
- event category  
- compute units  
- confidence score  
- timestamp  
- model name  

This gives the hackathon judges immediate visibility into compute spikes.

---

## 🧩 Architectural Principles

The system was built around three core goals:

### **1. Reliability**
Each step is deterministic and isolated.  
Nothing depends on external servers except EasyConnect → n8n, which is provided by the hackathon.

### **2. Auditability**
Both Google Sheets and Discord provide permanent logs.  
Judges can confirm throughput and behavior instantly.

### **3. Zero-Complexity Setup**
The architecture avoids:
- databases  
- custom servers  
- authentication complexity  
- external APIs  

Everything runs inside n8n + Google Sheets + Discord, which simplifies testing dramatically.

---

## 🧠 Why This Architecture Works

- Real-time, event-driven
- Minimal moving parts
- Clean data flow  
- Easy to debug and extend  
- Fully transparent for validation  

This keeps the Whale Tracker predictable, fast, and ideal for a hackathon environment.

---

## 📎 Related Files

- `overview.md` — System summary  
- `workflow.md` — Detailed n8n workflow explanation  
- `setup.md` — Instructions for replicating and testing the system  


