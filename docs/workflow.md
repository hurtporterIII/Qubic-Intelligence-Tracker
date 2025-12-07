# Qubic Intelligence Whale Tracker — n8n Workflow

This document explains the complete n8n workflow that powers the Whale Tracker automation pipeline.

The workflow is intentionally minimal, fast, and easy for judges to import and test.

---

## 🧠 Workflow Summary

The n8n automation performs five main tasks:

1. Receive event from EasyConnect  
2. Transform + clean the data  
3. Classify compute level  
4. Log event to Google Sheets  
5. Send formatted Discord alert  

The entire process completes in under one second.

---

## 🟦 1. Webhook Trigger

The workflow begins with the **Webhook** node.

EasyConnect sends a POST request containing:
- `model_name`  
- `compute_units`  
- `confidence`  
- `timestamp`  

Once received, n8n immediately passes this into the transformation step.

---

## 🔄 2. Transform Event Data

The transformation step ensures predictable data for the rest of the pipeline.

Key actions:
- Convert compute_units → number  
- Standardize field names  
- Add a `source` value (`"EasyConnect"`)  
- Remove unused or empty fields  

This guarantees consistent formatting for classification and logging.

Example transformed output:

```json
{
  "timestamp": "2025-01-01T00:00:00Z",
  "model_name": "ExampleModel",
  "compute_units": 53200000000,
  "confidence_score": 0.97,
  "source": "EasyConnect"
}
```

---

## 🧩 3. Classification Logic

A Function node assigns a category based on compute units:

| Compute Units | Category |
|---------------|----------|
| **50B+ CU** | Whale |
| **20B–49B CU** | High Impact |
| **< 20B CU** | Standard |

The category is appended to the payload and used by Sheets + Discord.

---

## 📄 4. Append Row to Google Sheets

The cleaned + classified event is written to a Google Sheet.

Logged Fields:
- timestamp  
- model_name  
- compute_units  
- confidence_score  
- category  
- source  

This provides the official audit trail for the hackathon.

Judges can refresh the sheet and see rows appear in real time.

---

## 📢 5. Discord Alert

A final Function or Webhook node formats a rich Discord embed.

Included in the alert:
- Classification (Whale / High Impact / Standard)  
- Compute units  
- Model name  
- Confidence score  
- Timestamp  

Whale-level events use stronger visual emphasis.

Example excerpt:

> **🐋 WHALE DETECTED**  
> Model: ExampleModel  
> Compute: 53.2B CU  
> Confidence: 97%  

---

## 📦 Workflow Export

The full workflow is available in the repository as:

```
/n8n/workflow.json
```

Judges can import this directly into any n8n instance with no modifications.

---

## 🛠️ Design Notes

- No API keys or tokens required  
- Pure webhook and native integrations  
- Fully deterministic execution  
- Uses only official n8n nodes  

The workflow is built to be hackathon-friendly: zero setup, zero friction.

---

## 📎 Related Files

- `overview.md` — High-level system explanation  
- `architecture.md` — How the pipeline is structured  
- `setup.md` — Instructions for running the system  


