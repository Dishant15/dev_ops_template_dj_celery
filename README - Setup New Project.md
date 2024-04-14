# Steps to setup new project with devops steps

## setup env variables

## copy paste config folder

- Django settings folder with base, local, production
- specifically focus on AUTHENTICATION - for base settings
- asgi.py , based on app uses websocket or not change this file commented out blocks

## docs folder

- no idea as of now

## removed locale folder

if you app don't use locale / django template translations remove this things

- LocaleMiddleware
- template processors
- Django Dockerfile last command : python manage.py compilemessages

## requirements

add required packages at the end of base / local / production txt files

## other files for configuration

- git
- manage.py
- tests folder

## local and production docker-compose yml files

copy paste and change as required

## django project dir

copy django apps in project_name directory

- update apps.py -> name to "{project_name}.app_name"
- update base settings file with this app
- update config -> api_router.py with api urls in new app

## change dev_ops -> project_name

- rename all occurances in vs code find and replace
- rename project dir folder name

## Other extra stuff

- check out this answer to manage log limits and logger rotation of docker : https://stackoverflow.com/a/57679944/2656359
