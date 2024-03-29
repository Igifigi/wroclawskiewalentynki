﻿from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from .plain_mails import *

def send_confirmation_mail(user):
    
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    plaintext_message = validate_email_message(uid, token)
    
    context = {
        'url': f'{settings.WWW_SITE}/validate/{uid}/{token}'
    }
    
    html_message = render_to_string('emails/validate.html', context)
    
    send_mail(
        plaintext_message['subject'],
        plaintext_message['message'],
        settings.NOREPLY_EMAIL,
        [user.email],
        html_message=html_message
        )
