#!/usr/bin/make -f

LOCAL_WEB_CONTAINER=app
LOCAL_COMPOSE_OPTIONS=-f docker-compose.yaml

help:
	@echo "up - Start all the containers (web and workers)"
	@echo "build - Build local docker containers from compose file"
	@echo "server - Start web server in interactive mode"
	@echo "stop - Stops all the containers"
	@echo "restart - stops and start again all the containers"
	@echo "ssh - SSH into the web container"
	@echo "requirements - Install app dependencies into the web container"

up-d:
	docker-compose $(LOCAL_COMPOSE_OPTIONS) up -d

up:
	docker-compose $(LOCAL_COMPOSE_OPTIONS) up

build:
	docker-compose $(LOCAL_COMPOSE_OPTIONS) build

stop: ## Stop all services
	docker-compose $(LOCAL_COMPOSE_OPTIONS) stop

restart: ## stops and start again all the containers
	docker-compose $(LOCAL_COMPOSE_OPTIONS) stop
	docker-compose $(LOCAL_COMPOSE_OPTIONS) up -d

logs:
	docker-compose $(LOCAL_COMPOSE_OPTIONS) logs --tail 50 --follow

server:
	docker exec $(LOCAL_COMPOSE_OPTIONS) bash -c "gunicorn --bind 0.0.0.0:5000 run:app"

ssh:
	docker exec -it $(LOCAL_WEB_CONTAINER) /bin/bash

requirements:
	docker exec -it $(LOCAL_WEB_CONTAINER) pip install --disable-pip-version-check --exists-action w -r requirements.txt


########################################## END ##############################################