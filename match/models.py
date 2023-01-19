from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from .match_settings import *

class School(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    code = models.CharField(_("Code"), max_length=3) # TODO: set code to exactly 3 znaki

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True ,on_delete=models.CASCADE)
    instagram = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    tiktok = models.URLField(max_length=200, blank=True)
    question1 = models.IntegerField(label=_('What class are you in?'), choices=Q1, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question2 = models.IntegerField(label=_('You identify yourself as:'), choices=Q2, validators=[MinValueValidator(1), MaxValueValidator(3)])
    question3 = models.IntegerField(label=_('Who would you like to be matched with?'), choices=Q3, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question4 = models.IntegerField(label=_('I want to meet:'), choices=Q4, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question5 = models.IntegerField(label=_('The ideal date/meeting is:'), choices=Q5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question6 = models.IntegerField(label=_('You have a geo test tomorrow, but you were supposed to meet your friends today. What do you do?'), choices=Q6, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question7 = models.IntegerField(label=_('In free time:'), choices=Q7, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question8 = models.IntegerField(label=_('If you had to listen to one musician for the next year, it would be:'), choices=Q8, validators=[MinValueValidator(1), MaxValueValidator(13)])
    question9 = models.IntegerField(label=_('On a scale of 1 to 10, how decisive are you?'), choices=Q9, validators=[MinValueValidator(1), MaxValueValidator(10)])
    question10 = models.IntegerField(label=_('Dogs or perhaps cats?'), choices=Q10, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question11 = models.IntegerField(label=_('How spontaneous are you?'), choices=Q11, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question12 = models.IntegerField(label=_('Do you avoid serious topics?'), choices=Q12, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question13 = models.IntegerField(label=_('My favorite subject at school is:'), choices=Q13, validators=[MinValueValidator(1), MaxValueValidator(8)])