export DB_HOST?=127.0.0.1
export DB_PASS?=tilesdev
export DB_USER?=tilesdev
export DB_NAME?=tiles
export DB_PORT?=3306

run: 
	python app.py

dev-run: 
	adev runserver .

test:
	pytest

build:
	docker build -t player-api .

dev-run:
	adev runserver .

install:
	pip install -r requirements-test
