from django.forms import ModelForm
from .models import UserProfile

class UserProfileCreateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'matched', 'matched_with']
