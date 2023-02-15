# Django-simple cookiecutter template

Django-simple cookiecutter template for a basic Django project with minimal options. It creates
a custom user, a base/home template, installs bootstrap and webpack if requested. 

## Steps to create a new project

The following procedure can be followed to install a new project:
- Create the project with `$ cookiecutter gh:start-new/django-simple`
- Answers the questions
- Enter the project with the terminal
- Install project dependencies using pipenv: `$ pipenv install`
- If postgresql is used and you want to use docker, start docker-compose with `$ docker-compose up -d`
- Execute the migrations using `$ pipenv run python manage.py migrate`
- If you have nodejs installed and you chose to use webpack:
    - Go to the frontend subfolder with your terminal: `$ cd frontend`
    - Install the frontend dependencies with `$ npm install`
    - Build the frontend files with `$ npm run build`