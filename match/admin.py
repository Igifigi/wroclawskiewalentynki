from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.utils.translation import gettext as _

from .models import UserProfile, School, Match

admin.site.register(School)
admin.site.register(Match)

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
    list_filter = (SchoolCodeFilter,)
