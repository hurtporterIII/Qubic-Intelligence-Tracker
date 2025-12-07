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

### 1. Webhook Trigger (EasyConnect → n8n)
Receives JSON payloads containing:
- model_name  
- compute_units (CU)  
- confidence  
- category  
- timestamp  

### 2. Data Cleaning + Normalization
Standardizes field names and ensures the event can be categorized correctly.

### 3. Classification Logic
Applies the IntelligenceTrack thresholds:
- **50B+ CU → Whale**  
- **20B–49B CU → High Impact**  
- **Below 20B CU → Standard activity**

### 4. Google Sheets Logging
Writes the cleaned event into the project Google Sheet:
- timestamp  
- model_name  
- compute_units  
- confidence_score  
- category  
- source  

### 5. Discord Notification
Sends a rich embedded alert using Discord Webhook:
- Color-coded by event type  
- Instant visibility for judges  
- Includes model, compute units, and confidence  

---

## Visual Flow Diagram (Text Version)

EasyConnect → Webhook Trigger  
→ Transform Event Data  
→ Classify Event  
→ Google Sheets (Append Row)  
→ Discord (Whale Alert)

---

## Workflow File

The exported workflow JSON is located here:

`workflow.json`

This file can be imported directly into any n8n environment.

---

## Notes for Judges

- No API keys are required to test the workflow.  
- Google Sheets and Discord use public-safe integration methods.  
- The system processes events in **under 1 second**.  
- The workflow is stable, simple, and reliable for demonstration.
