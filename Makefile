export DB_HOST?=127.0.0.1
export DB_PASS?=risk123
export DB_USER?=risk123
export DB_NAME?=risk
export DB_PORT?=8765

up:
	docker-compose up -d

run: 
	python app.py

test:
	pytest

build:
	docker build -t player-api .

dev-run:
	adev runserver .

install:
	pip install -r requirements-test
