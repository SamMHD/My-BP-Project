from django.urls import path

from . import controller

urlpatterns = [
    path('', controller.get_all_exercises, name='index'),
]