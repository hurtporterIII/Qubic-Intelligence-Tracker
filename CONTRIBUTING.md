# Contributing to WhaleTrack-AI

Thank you for your interest in improving WhaleTrack-AI.

## How this repo is organized

- `airtable/schema.json` – table structure for transaction records  
- `n8n/workflow.json` – n8n automation that connects Airtable and Discord  
- `docs/` – setup guide, architecture, and API documentation  
- `demo/` – project plan and flow diagram used for the hackathon submission  

## Workflow

1. **Fork** this repository.
2. Create a feature branch:
   - `git checkout -b feature/my-improvement`
3. Make your changes.
4. Update or add documentation in `docs/` if needed.
5. Open a **Pull Request** with:
   - What you changed
   - Why it improves WhaleTrack-AI
   - Any setup steps for reviewers

## Coding / project guidelines

- Do not commit secrets (API keys, webhook URLs, etc.).
- Keep JSON files valid (no comments inside JSON).
- Keep documentation clear enough that a non-coder can run the demo.
