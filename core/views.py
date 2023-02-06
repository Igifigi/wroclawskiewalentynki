from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.encoding import force_str

from .forms import NewUserForm
from .utils import send_confirmation_mail

def index(request):
    return render(request, 'index.html')

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_confirmation_mail(user)
            messages.success(request, _("Please go to your email %s to verify your account. Remember to check your SPAM folder.") % user.email)
            return redirect('index')
        for error in form.errors.values():
            messages.error(request, error)
    form = NewUserForm()
    context = {
        'caption': _('Sign up'),
        'form': form,
    }
    return render(request, template_name='flexible_login_form.html', context=context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, _("You are now logged in as %s.") % username)
                return redirect('index') #TODO: change
        for error in form.errors.values():
            messages.error(request, error)
    form = AuthenticationForm()
    context = {
        'caption': _('Log in'),
        'form': form,
    }
    return render(request, template_name='flexible_login_form.html', context=context)

def logout_request(request):
    logout(request)
    messages.info(request, _("You have successfully logged out."))
    return redirect('index')

def show_terms(request):
    return render(request, 'terms.html')

def show_privacy_policy(request):
    return render(request, 'privacy_policy.html')

def validate_email(request, uidb64, token):
    print(uidb64, token)    
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and default_token_generator.check_token(user, token) and not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, _('Successfully activated email. You can now login to your account.'))
        return redirect('login')
    else:
        messages.error(request, _('Activation link is invalid!'))
        
    return redirect('index')
