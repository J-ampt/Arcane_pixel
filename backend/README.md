# Arcane pixel backend

Simple api for handling and storing data.

# Setup
* install poetry (run `pip install poetry`)
* install dependencies (in `backend` folder run `poetry install`)
* via `psql` create database for backend
* use `.env.example` to create `.env` file and create an enviroment
* in `backend` folder:
  * run `poetry run python manage.py migrate`
  * run `poetry run python manage.py runserver`
