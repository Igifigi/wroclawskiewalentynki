from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .match_settings import *

class School(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    code = models.CharField(_("Code"), max_length=3, validators=[MinLengthValidator(3)])

def validate_school(code):
    if not School.objects.filter(code=code):
        raise ValidationError(_('%(code)s is not valid school code'), params={'code': code})

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile', on_delete=models.CASCADE)
    school = models.CharField(_('School code'), max_length=3, validators=[MinLengthValidator(3), validate_school])
    matched = models.BooleanField(default=False)
    question1 = models.IntegerField(_('What class are you in?'), choices=Q1.choices, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question2 = models.IntegerField(_('You identify yourself as:'), choices=Q2.choices, validators=[MinValueValidator(1), MaxValueValidator(3)])
    question3 = models.IntegerField(_('Who would you like to be matched with?'), choices=Q3.choices, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question4 = models.IntegerField(_('I want to meet:'), choices=Q4.choices, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question5 = models.IntegerField(_('The ideal date/meeting is:'), choices=Q5.choices, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question6 = models.IntegerField(_('You have a geo test tomorrow, but you were supposed to meet your friends today. What do you do?'), choices=Q6.choices, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question7 = models.IntegerField(_('In free time:'), choices=Q7.choices, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question8 = models.IntegerField(_('If you had to listen to one musician for the next year, it would be:'), choices=Q8.choices, validators=[MinValueValidator(1), MaxValueValidator(13)])
    question9 = models.IntegerField(_('On a scale of 1 to 10, how decisive are you?'), choices=Q9.choices, validators=[MinValueValidator(1), MaxValueValidator(10)])
    question10 = models.IntegerField(_('Dogs or perhaps cats?'), choices=Q10.choices, validators=[MinValueValidator(1), MaxValueValidator(4)])
    question11 = models.IntegerField(_('How spontaneous are you?'), choices=Q11.choices, validators=[MinValueValidator(1), MaxValueValidator(5)])
    question12 = models.IntegerField(_('Do you avoid serious topics?'), choices=Q12.choices, validators=[MinValueValidator(1), MaxValueValidator(2)])
    question13 = models.IntegerField(_('My favorite subject at school is:'), choices=Q13.choices, validators=[MinValueValidator(1), MaxValueValidator(8)])
    instagram = models.URLField(_('Instagram profile link (non-obligatory)'), max_length=200, blank=True)
    facebook = models.URLField(_('Facebook profile link (non-obligatory)'), max_length=200, blank=True)
    tiktok = models.URLField(_('TikTok profile link (non-obligatory)'), max_length=200, blank=True)
    accept_terms = models.BooleanField(_('I accept terms of use (available in the footer of the page).'))
    
    def __str__(self):
        return f'{self.user}, {self.school}, matched: {self.matched}'

class Match(models.Model):
    user1 = models.OneToOneField(UserProfile, related_name='match1_set', on_delete=models.CASCADE)
    user2 = models.OneToOneField(UserProfile, related_name='match2_set', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user1', 'user2')
