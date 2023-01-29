from django.utils.translation import gettext_lazy as _

def validate_email_message(first_name, last_name, uid, token):
    return {
        'subject': _('Verify your email address'),
        'message': _(
        f'Hello {first_name} {last_name}!' + 
        'Confirm your email by clicking this link:' +
        f'/validate/{uid}/{token}'
        )
    }