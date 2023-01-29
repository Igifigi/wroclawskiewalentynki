﻿from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_request, name='register'),
    path('chat/', index, name='chat'),
    path('terms_of_use', show_terms, name='terms'),
    path('validate/<uid>/<token>', validate_email, name='validate_email'),
]
