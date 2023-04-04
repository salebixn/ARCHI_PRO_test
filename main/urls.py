from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name=('index')),
    path('result/', ResultHandler.as_view(), name=('result-handler')),
]
