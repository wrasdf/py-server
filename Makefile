.PHONY: build

build:
	docker build -t flask:latest .

compose-build:
	docker-compose build

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
	docker run -it -v $$(pwd):/app -p 8080:8080 flask:latest /bin/bash
