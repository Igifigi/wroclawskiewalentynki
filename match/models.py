from django.db import models
from django.utils.translation import gettext as _

class School(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    code = models.CharField(_("Code"), max_length=3) # TODO: set code to exactly 3 znaki

