from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import mail_admins

from match.models import Match
from .models import Thread, ChatMessage

@login_required
def redirect_to_chat(request):
    try:
        match = Match.objects.get(Q(user1=request.user.profile) | Q(user2=request.user.profile))
        thread = match.matched_thread
    except:
        return render(request, 'redirect_to_chat.html')
    return redirect('personal_chat', thread.name)

@login_required
def chat(request, thread_name):
    thread = get_object_or_404(Thread, name=thread_name)
    if not request.user in thread.allowed_users.all() and not request.user.is_superuser:
        raise PermissionDenied
    
    cant_send = False
    if not request.user in thread.allowed_users.all():
        cant_send = True
    
    try:
        current_user = request.user
        other_user = list(thread.allowed_users.all().exclude(username=current_user.username))[0]
    except:
        raise PermissionDenied
    
    messages = ChatMessage.objects.filter(thread=thread)
    
    context = {
        'chat_messages': messages,
        'my_user': current_user,
        'my_user_full_name': f'{current_user.first_name} {current_user.last_name}',
        'other_user': other_user,
        'other_user_full_name': f'{other_user.first_name} {other_user.last_name}',
        'cant_send': cant_send,
        'thread_name': thread.name,
    }
    return render(request, 'chat.html', context=context)

@login_required
def report_chat(request, thread_name):
    thread = get_object_or_404(Thread, name=thread_name)
    
    if not request.user in thread.allowed_users.all() and not request.user.is_superuser:
        messages.info(request, _('You cannot report this chat.'))
    else:
        mail_admins(
            _('Chat report'),
            _('Thread %s was reported by user %s. Check what happened!') % (thread_name, request.user)
        )
        messages.info(request, _('This chat was reported.'))
    return redirect('chat')