.PHONY: build

build:
	docker build -t bottle:latest .

run: build
	docker run --rm -d -v $$(pwd):/app -p 8080:8080 bottle:latest

sh: build
	docker run -it -v $$(pwd):/app bottle:latest /bin/bash
