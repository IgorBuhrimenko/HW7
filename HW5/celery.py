import os

from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW5.settings')

app = Celery('HW5')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'clear-log': {
        'task': 'main.tasks.clear_log',
        'schedule': crontab(hour=0, minute=0),

    },
    'get_exchange_rates': {
        'task': 'exchanger.tasks.get_exchange_rates',
        'schedule': crontab(minute='*/30'),
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
