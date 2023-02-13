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

def exact_match_message():
    return {
        'subject': _('Your match is waiting!'),
        'message': _(
            'We managed to find the perfect match based on your answers on the Wroclaw Valentine\'s Day 2023 form. May the force be with you! '
        )
    }

def not_exact_match_message():
    return {
        'subject': _('Your match is waiting!'),
        'message': _(
            'We were able to find a great match for you based on your answers on the Wroclaw Valentine\'s Day 2023 form. ' +
            'Unfortunately, not all preferences specified in it could be met. Maybe that was destiny? See for yourself! '
        )
    }

def not_match_message():
    return {
        'subject': _('Thank you for participation!'),
        'message': _(
            'Unfortunately, we were unable to find a suitable match for you based on your answers from the Wroclaw Valentine\'s Day 2023 form. ' +
            'We apologize and thank you for participating in the action. '
        )
    }
