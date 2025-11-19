# notifications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='notifications_index'),
    path('alerts/', views.price_alerts, name='price_alerts'),
]