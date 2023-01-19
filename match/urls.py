from django.urls import path
from .views import *

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile')
]
