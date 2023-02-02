from django.forms import ModelForm, RadioSelect
from .models import UserProfile

class UserProfileCreateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'matched']
        widgets = {
            'question1': RadioSelect,
            'question2': RadioSelect,
            'question3': RadioSelect,
            'question4': RadioSelect,
            'question5': RadioSelect,
            'question6': RadioSelect,
            'question7': RadioSelect,
            'question8': RadioSelect,
            'question9': RadioSelect,
            'question10': RadioSelect,
            'question11': RadioSelect,
            'question12': RadioSelect,
            'question13': RadioSelect,
        }

class UserProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'school', 'matched', 'accept_terms',]
        widgets = {
            'question1': RadioSelect,
            'question2': RadioSelect,
            'question3': RadioSelect,
            'question4': RadioSelect,
            'question5': RadioSelect,
            'question6': RadioSelect,
            'question7': RadioSelect,
            'question8': RadioSelect,
            'question9': RadioSelect,
            'question10': RadioSelect,
            'question11': RadioSelect,
            'question12': RadioSelect,
            'question13': RadioSelect,
        }