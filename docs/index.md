# Project Documentation Index

歡迎來到 Modern FastAPI Project 專案文件。

## 文件清單 (Available Docs)
- [Architecture Plan](../ARCHITECTURE.md) - 詳細技術架構。
- [Setup Guide](../README.md) - 快速開始。
- API Reference - (由 FastAPI 自動生成於 `/docs`)

---
### 龍蝦筆記 (Lobster Notes)
- 確保 Pydantic v2 模型定義放在 `src/schemas/`。
- 不要直接在 API Endpoint 層寫 DB Query，請封裝於 `src/services/`。
- 如果專案規模變大，請按 Domain 劃分子目錄。
