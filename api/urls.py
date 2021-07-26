from django.urls import path
from . import views

urlpatterns = [
    path('sensex/', views.Nifty.as_view())
]


