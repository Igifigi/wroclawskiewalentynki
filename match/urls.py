from django.urls import path
from .views import *

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('start_matching', start_matching, name='start_matching'),
    path('matching', matching, name='matching'),
    path('match_result', match_result, name='match_result')
]
