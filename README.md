# Django-simple cookiecutter template

Django-simple cookiecutter template for a basic Django project with minimal options. It creates
a custom user, a base/home template, installs bootstrap and webpack if requested. 

## Prerequisites

The use of this project template supposes the presence on your computer of **[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)**, **[pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#installing-pipenv)**
and **[nodejs](https://nodejs.org/en/download)**.

## Steps to create a new project

The following procedure can be followed to create and configure a new project:
- Create the project with `$ cookiecutter gh:start-new/django-simple` and answer the questions
- Enter the project folder with the terminal
- Install project dependencies using pipenv with `$ pipenv install --dev`
- If postgresql is used and you want to use docker, start docker-compose with `$ docker compose up -d`
- Execute the migrations using `$ pipenv run python manage.py migrate`
- Create a super user using the dedicated command `$ pipenv run python manage.py createsuperuser`
- If you have nodejs installed and you chose to use bootstrap for your frontend development:
    - Enter the frontend subfolder with your terminal: `$ cd frontend`
    - Install the frontend dependencies with `$ npm install`
    - Build the frontend files for development with `$ npm run start` (you can stop the dev server with CTRL-C)
    - When ready for production, build frontend files with production optimizations using `$ npm run build`

## Stop the database
- If postgresql is used and you use docker, you can stop the database using `$ docker compose down`
