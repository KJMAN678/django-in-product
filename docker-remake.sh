docker compose down
docker compose build
docker compose up -d
docker compose exec web uv run task start-django
