from django.urls import path
from app_first.views import *

from app_first.models import Adress
app_name = "app_first"

urlpatterns = [
    path('room/', Adresses.as_view()),
]
