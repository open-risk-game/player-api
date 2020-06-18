export DB_HOST?=127.0.0.1
export DB_PASS?=admin
export DB_USER?=admin
export DB_NAME?=risk
export DB_PORT?=8765

up:
	docker-compose up -d

down:
	docker-compose down

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
