# Qubic Intelligence Whale Tracker — n8n Workflow

This document provides the full breakdown of the n8n workflow that powers the Qubic Intelligence Whale Tracker.  
The workflow is intentionally simple, auditable, and optimized for hackathon judges to import and test instantly.

---

## 🧠 Workflow Summary

The automation performs five primary tasks:

1. Receive event from EasyConnect  
2. Transform + clean the payload  
3. Classify compute level (Whale / High Impact / Standard)  
4. Append structured row to Google Sheets  
5. Send formatted alert to Discord  

Total processing time: **under one second**.

---

## ⚙️ Node-By-Node Breakdown

### **1. Webhook (EasyConnect → n8n)**
- Accepts POST requests from EasyConnect  
- Receives fields such as:  
  - `model_name`  
  - `compute_units`  
  - `confidence`  
  - `timestamp`

---

### **2. Transform Event Data (Function Node)**
The JavaScript function:
- normalizes field names  
- parses number values  
- ensures every event contains:  
  - `model_name`  
  - `compute_units`  
  - `confidence_score`  
  - `timestamp`

---

### **3. Classify Compute Level**
Thresholds:

| Compute Units | Classification |
|---------------|----------------|
| **50B+ CU** | Whale |
| **20B–49B CU** | High Impact |
| **< 20B CU** | Standard |

---

### **4. Google Sheets — Append Row**

Writes the following columns:

- timestamp  
- model_name  
- compute_units  
- confidence_score  
- category  
- source  

---

### **5. Discord — Whale Alert**

Sends a color-coded message containing:

- model name  
- compute units  
- confidence score  
- classification  

---

## 🔄 Workflow Diagram (Text)

EasyConnect Webhook  
↓  
Transform Event Data  
↓  
Classify Compute Level  
↓  
Append Row to Google Sheets  
↓  
Send Discord Alert  

---

## 📦 Workflow Export File

`/n8n/workflow.json`

---

## 📝 Notes for Judges

- No API keys required  
- Public-safe integrations only  
- Fully deterministic, easy to audit  
- Runs in under one second  

---

## ✅ Summary

This workflow transforms raw Qubic compute events into structured logs and high-visibility alerts using minimal moving parts.  
Its simplicity ensures reliability and clarity during hackathon evaluation.
