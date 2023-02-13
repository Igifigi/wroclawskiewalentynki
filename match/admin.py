from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.utils.translation import gettext as _

from .models import UserProfile, School, Match

class SchoolCodeFilter(SimpleListFilter):
    title = _('School code')
    parameter_name = 'school_code'
    
    def lookups(self, request, model_admin):
        return [(school.code, school.name) for school in School.objects.all()]
    
    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(school=self.value())

@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    questions = [str(UserProfile._meta.get_field(field).name) for field in [field.column for field in UserProfile._meta.fields if ('question' in str(field))]]
    list_filter = [SchoolCodeFilter, 'matched'] + questions
    search_fields = ['user__username',]

@admin.register(School)
class SchoolAdmin(ModelAdmin):
    search_fields = ['name', 'code']

@admin.register(Match)
class MatchAdmin(ModelAdmin):
    search_fields = ['user1__user__username', 'user2__user__username', 'matched_thread',]
