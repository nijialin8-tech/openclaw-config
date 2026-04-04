# Project Architecture: Modern FastAPI

## 🏗️ 專案架構規劃方案

本專案採用 **Layered Architecture (分層架構)** 的變體，並結合現代非同步 Python 技術棧。

### 1. 技術棧 (Tech Stack)
- **Web Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Pydantic v2)
- **Runtime**: Python 3.1x+
- **Database (Async)**: [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/) with `asyncpg`
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- **Validation**: [Pydantic V2](https://docs.pydantic.dev/latest/)
- **Environment**: [Pydantic Settings](https://docs.pydantic.dev/latest/usage/pydantic_settings/)
- **Dependency Injection**: FastAPI built-in `Depends`
- **Testing**: [Pytest](https://docs.pytest.org/en/latest/) + [HTTPX](https://www.python-httpx.org/) (for async testing)

### 2. 目錄結構分析
- `src/core/`: 存放全域配置、安全性設定、日誌紀錄與常數。
- `src/db/`: 資料庫連線實例、Base Model 設定。
- `src/models/`: SQLAlchemy 相對應的資料表定義。
- `src/schemas/`: Pydantic Models，用於 API 請求與回應的資料驗證。
- `src/api/`: API 端點路由。建議按版本 (`v1`, `v2`) 分類。
- `src/services/`: 封裝業務邏輯。API 端點應呼叫 Service，而不直接操作 Model。
- `tests/`: 單元測試與集成測試，保持與 `src` 相似的層級。

### 3. 開發模式建議
- **Type Hinting**: 全面落實型別標註，提升 IDE 支援與程式碼品質。
- **Async/Await**: 優先使用 Asynchronous 驅動 (DB, Redis, HTTP calls)。
- **Dependency Pattern**: 透過 `Depends` 注入資料庫 Session 或 Service 物件，方便 Mock 與測試。

### 4. 未來擴展
- **Domain-Driven Design (DDD)**: 若專案規模擴大，可考慮將模組改為按業務領域 (Domain) 劃分。
- **Containerization**: 提供 `Dockerfile` 與 `docker-compose.yml` 進行環境標準化。
