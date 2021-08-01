from django.urls import path
from .views import shorten_url, redirect_origin_url

urlpatterns = [
    path('shorten_url/', shorten_url),
    path('<str:code>/', redirect_origin_url)   
]
