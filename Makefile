# OpenClaw Factory Sync Makefile
# Author: Tech Expert 🤖
# Purpose: Initialize or sync OpenClaw configuration on a new machine

OPENCLAW_DIR := $(HOME)/.openclaw
CONFIG_REPO_DIR := $(shell pwd)

.PHONY: help sync backup check-dirs-and-files install-env-sample

help:
	@echo "OpenClaw Factory Sync Control 🤖"
	@echo "-------------------------------"
	@echo "make sync    - Sync configuration from this repo to $(OPENCLAW_DIR)"
	@echo "make backup  - Backup local $(OPENCLAW_DIR) config back to this repo"
	@echo "make status  - Check current environment status"

sync: check-dirs-and-files install-env-sample
	@echo "⚙️ Syncing global configuration..."
	@cp -v openclaw.json $(OPENCLAW_DIR)/openclaw.json
	@echo "🦞 Syncing workspaces..."
	@mkdir -p $(OPENCLAW_DIR)/workspaces
	@cp -Rv workspaces/* $(OPENCLAW_DIR)/workspaces/
	@echo "🕒 Cron jobs found in cron_jobs.json. Use 'openclaw cron add' to restore manually."
	@echo "✅ Sync complete! Please update $(OPENCLAW_DIR)/.env with your real API keys."
	@echo "🚀 Run 'openclaw gateway restart' to apply changes."

backup:
	@echo "📥 Backing up global config..."
	@cp -v $(OPENCLAW_DIR)/openclaw.json .
	@echo "📥 Backing up workspaces..."
	@mkdir -p workspaces
	@cp -Rv $(OPENCLAW_DIR)/workspaces/* workspaces/
	@echo "🕒 Backing up cron jobs (listing)..."
	@openclaw cron list > cron_list_backup.txt 2>/dev/null || true
	@echo "🧹 Cleaning up sensitive data from backup..."
	@sed -i '' 's/"apiKey": "[^"}]*"/"apiKey": "$${...}"/g' openclaw.json 2>/dev/null || true
	@sed -i '' 's/"token": "[^"}]*"/"token": "$${...}"/g' openclaw.json 2>/dev/null || true
	@echo "📦 Backup ready for git commit."

check-dirs-and-files:
	@mkdir -p $(OPENCLAW_DIR)
	@mkdir -p $(OPENCLAW_DIR)/workspaces

install-env-sample:
	@if [ ! -f $(OPENCLAW_DIR)/.env ]; then \
		echo "📄 Creating $(OPENCLAW_DIR)/.env from sample..."; \
		cp .env.sample $(OPENCLAW_DIR)/.env; \
	else \
		echo "⚠️ $(OPENCLAW_DIR)/.env already exists, skipping overwrite."; \
	fi

status:
	@echo "🔍 Repository: $(CONFIG_REPO_DIR)"
	@echo "🔍 OpenClaw Home: $(OPENCLAW_DIR)"
	@echo "🔍 Workspaces found: $$(ls -1 workspaces/ | wc -l)"
