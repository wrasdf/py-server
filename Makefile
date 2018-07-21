.PHONY: build stop up

compose-build:
	docker-compose build app

stop:
	docker stop $$(docker ps -aq) 1&2>/dev/null
	docker rm $$(docker ps -aq) 1&2>/dev/null
	rm -rf ./data/pg/*
	rm -rf ./data/redis/*

up: stop compose-build
	docker-compose up

db/downgrade:
	docker-compose run --rm app python app/manage.py db downgrade

db/upgrade:
	docker-compose run --rm app python app/manage.py db upgrade

db/migrate:
	docker-compose run --rm app python app/manage.py db migrate

build:
	docker build -t te .

sh: build
	docker run --rm -it -v $$(pwd):/app te /bin/bash
