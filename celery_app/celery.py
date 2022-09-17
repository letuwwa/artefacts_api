from celery import Celery


app = Celery("celery_app", broker="redis://localhost:6379/0", include=["celery_app.tasks"])
app.conf.update(result_expires=3600)


if __name__ == "__main__":
    app.start()
