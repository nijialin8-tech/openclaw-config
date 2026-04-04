# 🚀 Modern FastAPI Project Template

🏗️ **Architect Lobster (架構龍蝦)** 出動。這是一個為現代非同步 Python 應用程式量身打造的 FastAPI 專案模板。

## 📍 專案宗旨
本專案模板旨在提供一個可擴充、易測試、結構清晰的 Web 框架基礎，完全支持 Python 3.1x+ 與 Pydantic V2。

## 📁 目錄結構 (Directory Structure)
```text
.
├── src/                    # 原始程式碼
│   ├── api/                # API 路由與端點
│   │   └── v1/             # API v1 實現
│   ├── app/                # FastAPI 實體與中間件配置
│   ├── core/               # 核心配置 (Config, Security, Logging)
│   ├── db/                 # 資料庫連線實體與 Base 定義
│   ├── models/             # SQLAlchemy ORM Models
│   ├── schemas/            # Pydantic 資料模型 (Request/Response)
│   └── services/           # 商業邏輯運算層
├── tests/                  # 測試案例 (Pytest)
├── docs/                   # 專案文件 (Markdown, Diagrams)
├── ARCHITECTURE.md         # 詳細架構規劃
├── README.md               # 專案概覽
└── ...
```

## 🛠️ 快速開始 (Getting Started)
1. **安裝環境 (Python 3.10+):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install fastapi[standard] sqlalchemy[asyncio] asyncpg pydantic-settings
   ```
2. **啟動開發伺服器:**
   ```bash
   fastapi dev src/app/main.py
   ```
3. **訪問 API 文件:**
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## 🧪 運行測試
```bash
pytest
```

---
*Created by Architect Lobster (OpenClaw Subagent)*
