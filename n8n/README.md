# n8n Workflow Integration

This folder documents the n8n automation used in the Qubic Intelligence Whale Tracker.

## Purpose
The n8n workflow is responsible for:
1. Receiving whale event notifications from EasyConnect  
2. Processing and categorizing each event  
3. Logging the structured data into Google Sheets  
4. Sending formatted Discord alerts for judges to view  

This automation acts as the central “brain” of the system.

---

## Workflow Overview
The workflow performs the following steps:

### 1. **Webhook Trigger (EasyConnect → n8n)**
Receives JSON payloads containing:
- model_name  
- compute_units (CU)  
- confidence  
- category  
- timestamp  

### 2. **Data Cleaning + Normalization**
Standardizes field names and ensures the event can be categorized correctly.

### 3. **Classification Logic**
Applies the IntelligenceTrack thresholds:
- 50B+ CU →
