.DEFAULT_GOAL := build

migrate:
	python manage.py migrate

start:
	python manage.py runserver

build: migrate start