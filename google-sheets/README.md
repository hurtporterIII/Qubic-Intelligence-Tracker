# Google Sheets Integration

This folder documents the Google Sheets used in the Qubic Intelligence Whale Tracker.

## Sheet Purpose
The Google Sheet serves as the logging database for all detected whale events triggered by the n8n automation.

Each row represents a single AI whale event detected from the Qubic network.

## Columns Included
The automation writes the following fields to the sheet:

- **timestamp** – When the event was processed
- **model_name** – Name of the deployed AI model
- **compute_units** – Total compute units used (CU)
- **confidence_score** – Model evaluation confidence
- **category** – Whale, High Impact, or Standard event
- **source** – Where the event was detected from

## Sheet Link
The live Google Sheet can be found here:

*(Add your Google Sheet share link here)*

## Notes for Judges
This sheet is updated automatically by n8n using the Google Sheets API.  
No manual updates are required.

