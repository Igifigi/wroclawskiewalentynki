from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required, permission_required

from .forms import UserProfileForm
from .models import UserProfile
from .logic import make_matches

@login_required
def create_profile(request):
    if UserProfile.objects.filter(user=request.user):
        return redirect('edit_profile')
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.matched = False
            object.save()
            messages.success(request, _("Successfully created profile."))
            return redirect('index') # TODO: change
        messages.error(request, _("Unsuccessful")) # TODO: make error message
    else:
        form = UserProfileForm()
    context = {
        'form': form,
        'form_name': _('Create your profile'),
        'form_title': _('Create your profile'),
        'submit_button_label': _('Submit'),
    }
    return render(request, template_name='flexible_form.html', context=context)

@login_required
def edit_profile(request):
    if not UserProfile.objects.filter(user=request.user):
        return redirect('create_profile')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=UserProfile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            messages.success(request, _('Successfully updated profile.'))
            return redirect('index') # TODO: change
        messages.error(request, _('Unsuccessful')) # TODO: make error message
    else:
        form = UserProfile(instance=UserProfile.objects.get(user=request.user))
    context = {
        'form': form,
        'form_name': _('Edit your profile'),
        'form_title': _('Edit your profile'),
        'submit_button_label': _('Submit'),
    }
    return render(request, template_name='flexible_form.html', context=context)

@login_required
@permission_required('match.start_matching', raise_exception=True)
def start_matching1(request):
    message = _('Are you sure to start the matching process? It may take a while (depends on how much data does it have). Remember to make a backup of the database!')
    return render(request, 'start_matching1.html', context={'message': message})

def start_matching2(request):
    messages.info(request, _('Matching process has started. Please wait a while.'))
    make_matches()
    return render(request, 'start_matching1.html')
    
    