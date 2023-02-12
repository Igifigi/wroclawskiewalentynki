from django.contrib import admin

from .models import Thread, ChatMessage

admin.site.register(ChatMessage)
admin.site.register(Thread)
