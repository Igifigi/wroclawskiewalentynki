from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import UserProfile, School, Match

admin.site.register(School)
admin.site.register(Match)

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_filter = ('school',)
