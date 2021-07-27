from __future__ import absolute_import, unicode_literals

import json

from celery import shared_task

from utils.APIBridge import APIBridge
from utils.RedisConnection import RedisInstance
from utils.constants import NseAPI


@shared_task(name="update_gainers")
def niftygainers():
    data = APIBridge(url=NseAPI.Gainers).get()
    if data:
        gainers = data.json()['NIFTY'].get('data', None)
        return RedisInstance().set(key='gainers', value=json.dumps(gainers))


@shared_task(name="update_loosers")
def niftyloosers():
    data = APIBridge(url=NseAPI.Loosers).get()
    if data:
        loosers = data.json()['NIFTY'].get('data', None)
        return RedisInstance().set(key='loosers', value=json.dumps(loosers))
