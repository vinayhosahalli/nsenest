import logging

import redis.exceptions
from django.conf import settings


# connect to our Redis instance
class RedisInstance:
    def __init__(self):
        self.instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                          port=settings.REDIS_PORT, db=0)

    def set(self, key, value):
        try:
            return self.instance.set(name=key, value=value)
        except redis.exceptions.RedisError as er:
            logging.error('Something went wrong!' + repr(er))

    def get(self, key):
        try:
            return self.instance.get(name=key)
        except redis.exceptions.RedisError as er:
            logging.error('Something went wrong!' + repr(er))
