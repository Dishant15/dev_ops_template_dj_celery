from config import celery_app


# @celery_app.task(name="backend.userapp.tasks.add_things")
@celery_app.task()
def add_things(x, y):
    """A pointless Celery task to demonstrate usage."""
    return x + y
