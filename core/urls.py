from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('register', register_request, name='register'),
    path('chat', index, name='chat'),
]
