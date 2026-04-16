.DEFAULT_GOAL := build

migrate:
	uv run python manage.py migrate

start:
	uv run python manage.py runserver

build: migrate start
