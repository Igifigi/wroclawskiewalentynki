from django.urls import path
from .views import *

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('start_matching', start_matching1, name='start_matching1'),
    path('match', start_matching2, name='start_matching2'),
]
