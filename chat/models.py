from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.db.models.signals import m2m_changed

class Thread(models.Model):
    name = models.CharField(max_length=50, unique=True)
    allowed_users = models.ManyToManyField(User, related_name='threads')
    
    def allowed_users_changed(sender, **kwargs):
        if kwargs['instance'].allowed_users.count() > 2:
            raise ValidationError(_('You can\'t assign more than 2 users.'))
        
m2m_changed.connect(Thread.allowed_users_changed, sender=Thread.allowed_users.through)
     
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread')
    message = models.TextField(null=True, max_length=settings.MAX_MESSAGE_LENGTH)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.message
