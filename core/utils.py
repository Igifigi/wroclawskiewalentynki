from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

from .plain_mails import *

def send_confirmation_mail(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    plaintext_message = validate_email_message(user.first_name, user.last_name, uid, token)
    send_mail(plaintext_message['subject'], plaintext_message['message'], )
