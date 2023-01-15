from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm



from .forms import NewUserForm

def index(request):
    return render(request, 'base.html')

def register_request(request):
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _("Registration successfull."))
            print('mess1') # DEBUG
            return redirect('index') # TODO: change
        messages.error(request, _("Unsuccessful registration. Invalid information."))
    form = NewUserForm()
    context = {
        "register_form": form
    }
    return render(request, template_name='register.html', context=context)

def login_request(request):
    if request.POST:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, _(f"You are now logged in as {username}."))
                return redirect('index') #TODO: change
            else:
                messages.error(request, _("Invalid username or password."))
        else:
            messages.error(request, _("Invalid username or password."))
            # TODO: czy tych ifów nie można uprościć?
    form = AuthenticationForm()
    context = {
        "login_form": form
    }
    return render(request, 'login.html', context=context)

def logout_request(request):
    logout(request)
    messages.info(request, _("You have successfully logged out."))
    return redirect('index')
