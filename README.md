# Dev Ops

Dev ops template Django celery, postgis, docker, nginx, gunicorn + uvicorn

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

- view container logs
  docker compose -f production.yml logs django -f --tail 100

  use : --since=2m ; for logs of last 2 minutes, 1h for last 1 hour
  --tail 100 ; for last 100 lines of logs

  Use any container service name at the end: nginx | postgres | celeryworker

- Connect to django server with shell
  docker compose -f production.yml exec -it django bash

- To start and stop containers

  docker compose -f production.yml up -d
  docker compose -f production.yml down

- rebuild container after configuration / requirements / script changes

  docker compose -f production.yml up --build
  docker compose -f production.yml run --rm django python manage.py shell

- Migration commands

  docker compose -f production.yml run --rm django python manage.py makemigrations
  docker compose -f production.yml run --rm django python manage.py migrate

- Test django with pdb set trace
  docker attach <django-container-id>

- check space used by docker
  docker system df

- system runs out of space
  docker system prune

  Remove volumes as well
  docker system prune --force --volumes

  More info:
  https://medium.com/@alexeysamoshkin/reclaim-disk-space-by-removing-stale-and-unused-docker-data-a4c3bd1e4001

## Database Backup

- backup
  docker compose -f production.yml exec postgres backup
- view existing backups
  docker compose -f production.yml exec postgres backups
- restore backup
  docker compose -f production.yml exec postgres restore backup_name.sql.gz
- remove backup
  docker compose -f production.yml exec postgres rmbackup backup_name.sql.gz

## Move backups between servers

- docker volume TO server file system
  docker cp $(docker compose -f production.yml ps -q postgres):/backups ./backups
- server file system To Docker volume
  docker cp ./backups $(docker compose -f production.yml ps -q postgres):/backups

- With a single backup file copied to . that would be
  docker cp {container_id}:/backups/backup_name.sql.gz .

## Postgres commands (pgAdmin):

- check max allowed connection

```
SHOW max_connections;
```

- get current connections

```
SELECT * FROM pg_stat_activity;
```

- Terminate idle connections that have been idle for more than 5 minutes

```
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle' AND now() - state_change > interval '5 minutes';
```

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

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

## Deployment

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
