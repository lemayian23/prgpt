build:
    docker build -t prgpt-api .
run-local:
    node api/app.py
test:
    pytest tests/
seed:
    python scripts/seed_db.py
lint:
    flake8 workers/