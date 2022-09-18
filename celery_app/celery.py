import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery(
    "celery_app",
    include=["celery_app.tasks"],
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)
app.conf.update(result_expires=3600)


if __name__ == "__main__":
    app.start()
