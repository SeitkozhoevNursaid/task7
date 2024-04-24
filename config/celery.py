import os
from celery import Celery
from decouple import config
from datetime import timedelta
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.


app.autodiscover_tasks()

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.beat_schedule = {
    'change_password_month': {
        'task': 'login.tasks.change_password_month',
        'schedule': timedelta(seconds=20),
    },
    'block_inactive_users_every_day': {
        'task': 'login.tasks.block_inactive_users',
        'schedule': timedelta(seconds=30),
    },
    'notice_change_password_month': {
        'task': 'login.tasks.notice_change_password_month',
        'schedule': timedelta(seconds=25),
    },
}
