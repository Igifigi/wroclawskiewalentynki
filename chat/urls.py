from django.urls import path

from .views import *

urlpatterns = [
    path('', redirect_to_chat, name='chat'),
    path('<str:thread_name>', chat, name='personal_chat'),
    path('report/<str:thread_name>', report_chat, name='report_chat'),
]
