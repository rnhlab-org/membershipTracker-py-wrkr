from celery import Celery

# Initialize Celery app
app = Celery("worker", broker="redis://redis.default.svc.cluster.local:6379/0")

@app.task
def send_email(name, email):
    print(f"Sending email to {name} at {email}")
