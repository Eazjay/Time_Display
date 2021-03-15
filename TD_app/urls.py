from django.urls import path
from . import views

urlpatterns = [
    path('time_display', views.time_display),
    path('display_time', views.display_time),
]