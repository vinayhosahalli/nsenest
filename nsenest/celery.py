from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nsenest.settings')

app = Celery('nsenest')


app.config_from_object('django.conf:settings', namespace='CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    # Execute tasks every 5 minutes
    'update_gainers': {
        'task': 'update_gainers',
        'schedule': crontab(minute='*/5'),
    },
    'update_loosers': {
        'task': 'update_loosers',
        'schedule': crontab(minute='*/5'),
    },
}


