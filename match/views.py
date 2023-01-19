from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Successfully created profile."))
            print('mess2') #DEBUG
            return redirect('index') # TODO: change
        messages.error(request, _("Unsuccessful")) # TODO: make error message
        form = UserProfileForm()
        context = {
            "form": form
        }
        return render(request, template_name='create_user_profile.html', context=context)
