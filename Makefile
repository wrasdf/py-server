.PHONY: build stop up run sh

build:
	docker build -t flask:latest .

compose-build:
	docker-compose build app

stop:
	docker stop $$(docker ps -aq) 1&2>/dev/null
	docker rm $$(docker ps -aq) 1&2>/dev/null
	rm -rf ./data/pg/*
	rm -rf ./data/redis/*

up: stop compose-build
	docker-compose up

run: build stop
	docker run --rm -d -v $$(pwd):/app -p 8080:8080 flask:latest

sh: build
	docker run -it -v $$(pwd):/app -e A -p 8080:8080 flask:latest /bin/bash

db/connect:
	docker-compose exec -it app psql -Upostgres

db/downgrade:
	docker-compose run --rm app python app/manage.py db downgrade

db/upgrade:
	docker-compose run --rm app python app/manage.py db upgrade

db/migrate:
	docker-compose run --rm app python app/manage.py db migrate
