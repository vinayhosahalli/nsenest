from django.urls import path, include
from rest_framework import routers

from .views import Nifty

router = routers.DefaultRouter()
router.register('nifty', Nifty, basename='nifty')
urlpatterns = [
    path('', include(router.urls))
]


