from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.utils.translation import gettext as _

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('register/', register_request, name='register'),
    path('terms_of_use', show_terms, name='terms'),
    path('privacy_policy', show_privacy_policy, name='privacy'),
    path('validate/<uidb64>/<token>', validate_email, name='validate_email'),
    path(
        'reset_password/',
        PasswordResetView.as_view(
            template_name='password_reset.html',
            html_email_template_name='emails/password_reset.html',
            subject_template_name='emails/password_reset_subject.txt'
        ),
        name='password_reset'
    ),
    path(
        'reset_password/done/',
        message_and_redirect,
        {
            'message': _('If there is an account assigned to the given email address, instructions for changing the password have been sent.'),
            'redirect_url': 'index',
        },
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset_password/complete',
        message_and_redirect,
        {
            'message': _('Password changed successfully. You can now log in.'),
            'redirect_url': 'login',
        },
        name='password_reset_complete'
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
