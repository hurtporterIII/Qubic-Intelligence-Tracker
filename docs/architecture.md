# System Architecture

WhaleTrack-AI uses a simple but powerful architecture:

1. **On-chain Data Source**
   - Listens for token transfers exposed via Qubic or API endpoint.
  
2. **n8n Workflow**
   - Fetches new whale transactions.
   - Normalizes and filters by amount.
   - Writes data into Airtable.
   - Sends formatted alert to Discord.

3. **Airtable Database**
   - Stores normalized whale transactions.
   - Used for dashboarding and CSV export.

4. **Discord Webhook**
   - Sends real-time whale alerts.

This architecture ensures real-time monitoring with minimal infrastructure.
