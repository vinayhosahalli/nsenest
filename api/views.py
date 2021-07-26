from rest_framework.views import APIView

from utils.APIBridge import APIBridge
from utils.CustomResponse import success
from utils.constants import NseAPI
# Create your views here.


class Nifty(APIView):

    def get(self, request):
        res = APIBridge(url=NseAPI.Gainers).get()
        return success(res)


