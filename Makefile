build:
    docker build -t prgpt-api .
run-local:
    python api/app.py
test:
    pytest tests/
seed:
    python scripts/seed_db.py
lint:
    flake8 workers/