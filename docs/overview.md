# Qubic Intelligence Whale Tracker — System Overview

The Qubic Intelligence Whale Tracker is a real-time monitoring system that detects, classifies, and logs high-compute AI jobs (“intelligence whales”) running on the Qubic decentralized supercomputer.

This project was built for the Qubic Hack the Future Hackathon with a focus on:
- Instant visibility into large-scale compute events  
- Transparent logging for validation  
- Clean automation using n8n  
- Zero-friction setup for judges  

---

## 🔍 What the System Does

When a high-compute AI model is deployed on Qubic, EasyConnect sends an event to our automation pipeline.  
The system:

1. Receives the event  
2. Normalizes and cleans the data  
3. Classifies the compute level (Whale / High Impact / Standard)  
4. Logs the structured event into Google Sheets  
5. Sends a formatted alert to Discord  

Everything occurs automatically in under one second.

---

## ⭐ Why This Matters

Qubic enables decentralized high-compute AI workloads. Tracking large jobs helps identify:

- Emerging AI models  
- Compute-heavy deployments  
- Network activity spikes  
- Shifts in resource usage  

The Whale Tracker provides a clear, auditable window into these events.

---

## 📡 Key Components

| Component | Description |
|----------|-------------|
| **EasyConnect Webhooks** | Streams real-time Qubic compute events |
| **n8n Workflow** | Core automation pipeline: transform → classify → log → alert |
| **Google Sheets** | Persistent event logging system |
| **Discord Webhook** | Real-time notifications for judges |

---

## 🚀 Core Features

### 1. Real-Time Detection
Events arrive instantly via EasyConnect.

### 2. Automatic Classification
Based on compute units:
- Whale: 50B+ CU  
- High Impact: 20B–49B CU  
- Standard: < 20B CU  

### 3. Structured Logging
Logs include:
- timestamp  
- model_name  
- compute_units  
- confidence_score  
- classification  
- source  

### 4. High-Visibility Alerts
Judges see activity immediately in Discord.

---

## 🧠 Architecture (Simplified)

EasyConnect Webhook  
↓  
Transform Event Data  
↓  
Classify Compute Level  
↓  
Append Row to Google Sheets  
↓  
Send Discord Alert  

This design keeps the system reliable, predictable, and extremely easy to review.

---

## 📎 Additional Documentation

- `architecture.md` — System diagram and deeper explanation  
- `workflow.md` — Full n8n workflow breakdown  
- `setup.md` — Instructions for judges to test the system  

---

## 🏁 Summary

The Qubic Intelligence Whale Tracker demonstrates how real-time AI compute events can be captured, classified, logged, and broadcast with clean, reliable automation.  
The system is simple to run, easy to verify, and designed for clarity during hackathon evaluation.
