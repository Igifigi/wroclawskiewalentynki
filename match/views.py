from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from .forms import UserProfileCreateForm, UserProfileEditForm
from .models import UserProfile
from .logic import make_matches
from .utils import export_user_related_database_as_xlsx

@login_required
def create_profile(request):
    if not request.user.is_active:
        messages.error(_('You need to activate your account.'))
        return redirect('index') #TODO: change
    if UserProfile.objects.filter(user=request.user):
        return redirect('edit_profile')
    if request.method == 'POST':
        form = UserProfileCreateForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.matched = False
            object.save()
            messages.success(request, _("Successfully created profile."))
            return redirect('index') # TODO: change
        messages.error(request, _("Unsuccessful")) # TODO: make error message
    else:
        form = UserProfileCreateForm()
    context = {
        'form': form,
        'form_name': _('Create your profile'),
        'form_title': _('Create your profile'),
        'submit_button_label': _('Submit'),
    }
    return render(request, template_name='profile_form.html', context=context)

@login_required
def edit_profile(request):
    if not UserProfile.objects.filter(user=request.user):
        return redirect('create_profile')
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=UserProfile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            messages.success(request, _('Successfully updated profile.'))
            return redirect('index') # TODO: change
        messages.error(request, _('Unsuccessful')) # TODO: make error message
    else:
        form = UserProfileEditForm(instance=UserProfile.objects.get(user=request.user))
    context = {
        'form': form,
        'form_name': _('Edit your profile'),
        'form_title': _('Edit your profile'),
        'submit_button_label': _('Submit'),
    }
    return render(request, template_name='profile_form.html', context=context)

@login_required
@permission_required('match.match', raise_exception=True)
def start_matching(request):
    context = {
        'title': _('Start matching'),
        'message': _('Are you sure to start the matching process? It may take a while (depends on how much data does it have). Remember to make a backup of the database!'),
        'button_label': _('Proceed'),
        'alert_message': _('Please remember to make a backup of the database! (before clicking OK button)'),
        'redirect_url': 'matching',
    }
    return render(request, 'flexible_site.html', context=context)
    
def matching(request):
    context = {
        'title': _('Matching, please wait'),
        'message': _('Matching process has started. Please wait a while.'),
        'button_label': _('Go to result'),
        'alert_message': 'None',
        'redirect_url': 'match_result',
    }
    make_matches()
    return render(request, 'flexible_site.html', context=context)
    
def match_result(request):
    with_match = UserProfile.objects.filter(matched=True)
    without_match = UserProfile.objects.filter(matched=False)
    without_profile = User.objects.filter(profile=None)
    context = {
        'with_match': with_match,
        'with_match_count': len(with_match),
        'without_match': without_match,
        'without_match_count': len(without_match),
        'without_profile': without_profile,
        'without_profile_count': len(without_profile)
    }
    return render(request, 'match_result.html', context=context)

@login_required
@permission_required('match.download_database', raise_exception=True)
def export_database(request):
    output = export_user_related_database_as_xlsx()
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=user-related_db_WW.xlsx"
    return response
    