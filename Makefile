export DB_HOST?=127.0.0.1
export DB_PASS?=risk123
export DB_USER?=risk123
export DB_NAME?=risk
export DB_PORT?=3306

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

install: install-test
	pip install -r requirements

install-test:
	pip install -r requirements-test
