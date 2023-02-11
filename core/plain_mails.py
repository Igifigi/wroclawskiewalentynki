from django.utils.translation import gettext_lazy as _
from django.conf import settings

def validate_email_message(uid, token):
    return {
        'subject': _('Verify e-mail address'),
        'message': _(
            'Hello! ' +
            'You have received this message because an instruction to create an account on the wroclawskiewalentynki.pl website has been issued. ' +
            'Please copy and paste the following URL into your web browser to verify your e-mail address: ' +
            f'{settings.WWW_SITE}/validate/{uid}/{token}. ' +
            'If you did not issue the instruction, write an e-mail to kontakt@wroclawskiewalentynki.pl. ' +
            'Thank you for being part of our community. ' +
            'Team of Wroclaw Valentine\'s Day 2023 ' +
            'Message generated automatically. Please do not reply to it.'
        )
    }

def reset_password_message(uid, token):
    return {
        'subject': _('Reset your password'),
        'message': _(
            'Hello! ' +
            'You have received this message because an instruction to change the password from your account at wroclawskiewalentynki.pl has been issued. ' +
            'Please copy and paste the following URL into your web browser to verify your e-mail address: ' +
            f'{settings.WWW_SITE}/validate/{uid}/{token}. ' +
            'If you did not issue the instruction, write an e-mail to kontakt@wroclawskiewalentynki.pl. ' +
            'Thank you for being part of our community. ' +
            'Team of Wroclaw Valentine\'s Day 2023 ' +
            'Message generated automatically. Please do not reply to it.'
        )
    }
