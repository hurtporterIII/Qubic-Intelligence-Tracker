# Qubic Intelligence Whale Tracker — Setup Guide

This guide shows judges exactly how to test and verify the Whale Tracker system.  
No coding, configuration, or credentials are required.

---

## ✅ What You Need

- A browser  
- Access to n8n (local, cloud, or demo instance)  
- The provided Google Sheet (read/write enabled)  
- The `workflow.json` file from the `/n8n` folder  

That’s it.

---

## 🟦 1. Import the n8n Workflow

1. Open your n8n instance  
2. Go to **Import**  
3. Upload:

```
/n8n/workflow.json
```

4. Save → Activate the workflow  
5. n8n will display a URL for the Webhook Trigger  

Copy that URL — you will paste it into EasyConnect.

---

## 🟩 2. Connect EasyConnect to n8n

1. Open the EasyConnect integration panel  
2. Create a new webhook  
3. Paste the n8n Webhook URL  
4. Choose the **Qubic Intelligence Tracker** event stream  
5. Press **Send Test Notification**

If everything is connected properly, you will see:
- A new Google Sheets row  
- A Discord alert  
- Successful workflow execution in n8n  

---

## 🟨 3. Verify Google Sheets Logging

Open the project’s Google Sheet.

Each event should populate a new row containing:

- timestamp  
- model_name  
- compute_units  
- confidence_score  
- category  
- source  

Rows appear instantly — no refresh delay.

---

## 🟥 4. Verify Discord Alerts

In your Discord webhook test channel:

You should immediately see formatted alerts like:

```
🐋 WHALE DETECTED
Model: ExampleModel
Compute: 50B+ CU
Confidence: 98%
```

Or, for lighter activity:

```
⚡ High Impact Compute Event
```

Everything is delivered in under one second.

---

## 🧪 5. Testing Scenarios

You may trigger multiple events to confirm behavior:

### Whale-Level  
Send compute_units ≥ 50,000,000,000  
→ Expect whale classification + bold visual alert

### High Impact  
20B–49B  
→ Yellow/medium alert

### Standard  
< 20B  
→ Low-priority alert

---

## 🛡️ Troubleshooting

### Nothing appears in Google Sheets  
- Ensure workflow is **Activated**  
- Verify the Google Sheets node is authenticated  
- Confirm EasyConnect sent the event successfully  

### Discord alert missing  
- Check the Discord Webhook URL in the workflow  
- Ensure no rate limits were hit  

### n8n shows an error  
- Open **Execution Logs**  
- Most issues come from malformed test payloads  
- Re-import workflow.json if necessary  

---

## 🏁 Done

You now have a fully running Qubic Whale Tracker system.

The entire process — import, connect, test — takes under 2 minutes.

---

## 📎 Related Documentation

- `overview.md` — What the system is and why it matters  
- `architecture.md` — System structure and data flow  
- `workflow.md` — Detailed breakdown of each automation step  


