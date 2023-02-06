from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_request, name='register'),
    #path('chat/', index, name='chat'),
    path('terms_of_use', show_terms, name='terms'),
    path('privacy_policy', show_privacy_policy, name='privacy'),
    path('validate/<uidb64>/<token>', validate_email, name='validate_email'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)