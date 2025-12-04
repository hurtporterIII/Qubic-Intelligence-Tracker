# WhaleTrack-AI Setup Guide

This guide explains how to set up the Airtable base, import the n8n workflow, and connect Discord webhooks.

## 1. Airtable Setup
- Create a new base
- Create fields: Name, Amount, USD_Value, Is_Whale
- Import `schema.json`

## 2. n8n Setup
- Import `workflow.json`
- Replace placeholder Discord webhook URL
- Add Cron trigger or Webhook trigger as needed

## 3. Running the System
- Start n8n
- Confirm logs show successful webhook deliveries
- Verify messages appear in Discord channel
