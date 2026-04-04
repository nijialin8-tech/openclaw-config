# Use a lightweight Python base image
FROM python:3.12-slim-bookworm

# Copy the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy project files
COPY pyproject.toml .
# If lockfile exists: COPY uv.lock .

# Install dependencies using uv
# --no-install-project is useful if you want to cache dependencies separately
RUN uv sync --frozen --no-install-project --no-dev

# Copy application source code
COPY main.py .

# Optional: Run tests (if any) or lint
# RUN uv run pytest

# Expose port
EXPOSE 8000

# Set environment variables for uvicorn
ENV HOST=0.0.0.0
ENV PORT=8000

# Command to run the application
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
