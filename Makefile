.PHONY: build

build:
	docker build -t flask:latest .

stop:
	docker stop $$(docker ps -aq) 2>/dev/null

run: build stop
	docker run --rm -d -v $$(pwd):/app -p 8080:8080 flask:latest

sh: build
	docker run -it -v $$(pwd):/app -p 8080:8080 flask:latest /bin/bash
