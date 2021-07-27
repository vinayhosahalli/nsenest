from rest_framework.viewsets import GenericViewSet
from utils.CustomResponse import success, notfound
from rest_framework.decorators import action
from utils.RedisConnection import RedisInstance
import json


# Create your views here.


class Nifty(GenericViewSet):

    @action(detail=False, methods=['GET'])
    def gainers(self, request):
        instance = RedisInstance()
        data = instance.get(key='gainers')
        if data:
            return success(data=json.loads(data))
        return notfound()

    @action(detail=False, methods=['GET'])
    def loosers(self, request):
        instance = RedisInstance()
        data = instance.get(key='loosers')
        if data:
            return success(data=json.loads(data))
        return notfound()

