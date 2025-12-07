import streamlit as st
import requests
from datetime import datetime

# ** THIS IS YOUR LIVE WEBHOOK URL (FIXED) **
WEBHOOK_URL = "https://thetempledp.app.n8n.cloud/webhook-t/intelligence-alert" 

st.set_page_config(
    page_title="Qubic Intelligence Whale Tracker Demo",
    page_icon="🐋",
    layout="centered"
)

st.title("🐋 Qubic Intelligence Whale Tracker Demo")
st.subheader("Simulate a High-Impact AI Job")

st.markdown("""
    Click the button below to simulate a 'GOD MODE WHALE' event. 
    This triggers the classification workflow and instantly logs the 
    data into the transparent ledger (Google Sheet) and fires the Discord alert.
""")

# Data that simulates the "GOD MODE WHALE" tier (Accuracy >= 0.95 and Cycles >= 50 Billion)
SIMULATED_DATA = {
    "compute_cycles": 60000000000,
    "model_accuracy": 0.97,
    "usd_cost_estimate": 12.50,
    "job_id": "SIM-42-HACKATHON",
    "miner_address": "TEMPLE-RIG-01"
}

def send_whale_data():
    try:
        response = requests.post(WEBHOOK_URL, json=SIMULATED_DATA)

        if response.status_code == 200:
            st.success("✅ Whale Event Sent! Check your Google Sheet and Discord for the instant 'GOD MODE WHALE' classification.")
        else:
            st.error(f"❌ Webhook failed. Status Code: {response.status_code}. Ensure your n8n workflow is ACTIVE.")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Connection Error: {e}")

if st.button("🚀 TRIGGER GOD MODE WHALE EVENT 🚀"):
    send_whale_data()

st.markdown("---")
st.markdown("This interactive component demonstrates the **Cost vs. Quality** auditing core.")
