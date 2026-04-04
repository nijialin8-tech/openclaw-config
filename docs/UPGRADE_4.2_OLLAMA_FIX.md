# OpenClaw 4.2 Upgrade Node - Ollama Config Fix

## Issue Summary
When upgrading from OpenClaw 2026.3.1 to 2026.4.2, there was a mismatch in Ollama model provider names and IDs. Specifically, models previously labeled as `:cloud` (like `gemini-3-flash-preview:cloud`) were failing due to incorrect provider names or ID references after the update.

## Resolution
- **Provider Name**: Unified Ollama Cloud access under the provider ID `ollama-cloud` to separate it from local `ollama` instances.
- **Model IDs**: Updated the Gemini model ID from `gemini-3-flash-preview:cloud` to `gemini-3-flash-preview:latest` to match the current cloud deployment naming.
- **Default Agent Configs**: Updated `defaults.model.primary` and individual agent `model` settings across `openclaw.json` to use `ollama-cloud/gemini-3-flash-preview:latest`.
- **Cleanup**: Local Ollama (127.0.0.1) configurations were removed from agent-specific `models.json` for technical experts to avoid confusion on machines without local instances running.

## Version
- Recorded for OpenClaw version **4.2**.
- Date: 2026-04-05
- Fix verified in `tech-expert` workspace and `openclaw-config/openclaw.json`.
