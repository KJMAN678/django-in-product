FROM python:3.13-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.9.11 /uv /uvx /bin/

# psycopg2 ビルドに必要なパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app/backend
COPY . .
RUN uv sync --dev --link-mode=copy
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
