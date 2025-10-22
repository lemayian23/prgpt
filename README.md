MaasaiPRGPT
MaasaiPRGPT is a pull request triage and code review assistant, inspired by Maasai precision, designed to enhance engineering workflows with efficient PR management.
Overview
This MVP includes a REST API, static analysis worker, React-based web UI, PostgreSQL database, and Docker support to streamline code reviews.
Getting Started
Prerequisites

Node.js (Download)
Python 3.x (Download)
PostgreSQL (Download)
Docker Desktop (Download)

Installation

Navigate to the project:cd D:\DP\prgpt


Install dependencies:
API: cd api && npm init -y && npm install express body-parser axios
Workers: cd workers && python -m venv venv && venv\Scripts\activate && pip install flake8
Web UI: cd webui && npx create-react-app . --template typescript && npm install


Set up PostgreSQL:psql -U postgres
CREATE DATABASE maasai_prgpt;
\c maasai_prgpt
CREATE TABLE pr_metadata (id SERIAL PRIMARY KEY, pr_id INT UNIQUE, summary TEXT, review_bullets JSONB, comment TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
\q


Build and run:docker build -t maasai-prgpt-api .
make run-local
cd webui && npm start


Seed database:cd scripts && python seed_db.py



Usage

Configure a GitHub webhook to http://localhost:3000/webhook.
Open a PR to trigger analysis; view results in the web UI at http://localhost:3000.

File Structure
D:\DP\prgpt\
│   Dockerfile
│   Makefile
│
├───api
│   └───app.py
├───infra
│   └───k8s
│       └───deployment.yaml
├───scripts
│   └───seed_db.py
├───tests
│   └───unit
│       └───test_webhook.py
├───webui
│   ├───App.js
│   └───index.html
└───workers
    └───analyze.py

Contributing
Fork the repo, submit PRs, and add tests in tests/unit/.
License
MIT (create a LICENSE file with MIT terms).