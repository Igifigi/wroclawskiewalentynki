from django.urls import path
from .views import create_profile, edit_profile, start_matching, matching, match_result, export_database, assign_threads

urlpatterns = [
    path('create_profile/', create_profile, name='create_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('start_matching', start_matching, name='start_matching'),
    path('matching', matching, name='matching'),
    path('match_result', match_result, name='match_result'),
    path('export_database', export_database, name='export_database'),
    path('create_and_assign_threads', assign_threads, name='create_and_assign_threads'),
]
