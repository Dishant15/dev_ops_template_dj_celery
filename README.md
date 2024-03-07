# Dev Ops

Dev ops template Django celery, postgis, docker, nginx, gunicorn + uvicorn

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

- To start and stop local containers

        docker-compose -f local.yml up
        docker-compose -f local.yml down

- rebuild container after configuration / requirements / script changes

        docker-compose -f local.yml up --build
        docker-compose -f local.yml run --rm django python ./backend/manage.py shell

- Migration commands

        docker-compose -f local.yml run --rm django python ./backend/manage.py makemigrations
        docker-compose -f local.yml run --rm django python ./backend/manage.py migrate

## Database Backup

        docker compose -f local.yml exec postgres backup

- view existing backups
  docker compose -f local.yml exec postgres backups
- restore backup
  docker compose -f local.yml exec postgres restore backup_2018_03_13T09_05_07.sql.gz

- copy all backups locally
  docker cp {container_id}:/backups ./backups
- You can also get the container ID using
  docker cp $(docker compose -f local.yml ps -q postgres):/backups ./backups
- With a single backup file copied to . that would be
  docker cp {container_id}:/backups/backup_2018_03_13T09_05_07.sql.gz .

### Type checks

Running type checks with mypy:

    $ mypy dev_ops

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd dev_ops
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd dev_ops
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd dev_ops
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
