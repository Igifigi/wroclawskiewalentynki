﻿from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.models import User
from xlsxwriter.workbook import Workbook
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings
from django.template.loader import render_to_string

from core.plain_mails import exact_match_message, not_exact_match_message, not_match_message 
from chat.models import Thread
from chat.utils import get_thread_name
from .models import UserProfile, School, Match
from .match_settings import *

def add_user_based_sheet(workbook, title, queryset, bold):
    sheet = workbook.add_worksheet(f'(USER) {title}')
    sheet.write_row(0, 0, ['id', 'username', 'first name', 'last name', 'email', 'is active'])
    sheet.set_row(0, None, bold)
    sheet.set_column(0,0,5)
    sheet.set_column(1,1,10)
    sheet.set_column(2,4,15)
    sheet.set_column(5,5,10)
    
    for index, user in enumerate(queryset):
        data = (
            user.id,
            user.username,
            user.first_name,
            user.last_name,
            user.email,
            "YES" if user.is_active else "NO",
        )
        sheet.write_row(index + 1, 0, data)

def add_profile_based_sheet(workbook, title, queryset, bold):
    sheet = workbook.add_worksheet(f'(USERPROFILE) {title}')
    questions = [UserProfile._meta.get_field(field).verbose_name for field in [field.column for field in UserProfile._meta.fields if 'question' in str(field)]]
    sheet.write_row(0, 0, ['id', 'username', 'school'] + questions + ['ig', 'fb', 'tt', 'terms accepted'])
    sheet.set_row(0, None, bold)
    sheet.set_column(0,0,5)
    sheet.set_column(1,1,10)
    sheet.set_column(2,14,15)
    sheet.set_column(15,17,5)
    sheet.set_column(18,18,10)
    
    for index, userprofile in enumerate(queryset):
        data = (
            userprofile.id,
            userprofile.user.username,
            School.objects.get(code=userprofile.school).name,
            Q1.choices[list(zip(*Q1.choices))[0].index(userprofile.question1)][1],
            Q2.choices[list(zip(*Q2.choices))[0].index(userprofile.question2)][1],
            Q3.choices[list(zip(*Q3.choices))[0].index(userprofile.question3)][1],
            Q4.choices[list(zip(*Q4.choices))[0].index(userprofile.question4)][1],
            Q5.choices[list(zip(*Q5.choices))[0].index(userprofile.question5)][1],
            Q6.choices[list(zip(*Q6.choices))[0].index(userprofile.question6)][1],
            Q7.choices[list(zip(*Q7.choices))[0].index(userprofile.question7)][1],
            Q8.choices[list(zip(*Q8.choices))[0].index(userprofile.question8)][1],
            Q9.choices[list(zip(*Q9.choices))[0].index(userprofile.question9)][1],
            Q10.choices[list(zip(*Q10.choices))[0].index(userprofile.question10)][1],
            Q11.choices[list(zip(*Q11.choices))[0].index(userprofile.question11)][1],
            Q12.choices[list(zip(*Q12.choices))[0].index(userprofile.question12)][1],
            Q13.choices[list(zip(*Q13.choices))[0].index(userprofile.question13)][1],
            userprofile.instagram,
            userprofile.facebook,
            userprofile.tiktok,
            "YES" if userprofile.accept_terms else "NIE",
        )
        sheet.write_row(index + 1, 0, data)

def add_match_based_sheet(workbook, title, queryset, bold):
    sheet = workbook.add_worksheet(f'(MATCH) {title}')
    sheet.write_row(0, 0, ['id', 'user1_username', 'user2_username', 'thread_name', 'exact'])
    sheet.set_row(0, None, bold)
    sheet.set_column(0,0,5)
    sheet.set_column(1,3,15)

    for index, match in enumerate(queryset):
        data = (
            match.id,
            match.user1.user.username,
            match.user2.user.username,
            match.thread_name,
            'YES' if match.exact else 'NO'
        )
        sheet.write_row(index + 1, 0, data)

def export_user_related_database_as_xlsx():
    output = BytesIO()
    book = Workbook(output, {})
    bold = book.add_format({'bold': True})
    
    add_user_based_sheet(book, 'all users', User.objects.all().exclude(is_superuser=True), bold)
    add_profile_based_sheet(book, 'matched users', UserProfile.objects.filter(matched=True).exclude(user__is_superuser=True), bold)
    add_profile_based_sheet(book, 'non-matched users', UserProfile.objects.filter(matched=False).exclude(user__is_superuser=True), bold)
    add_user_based_sheet(book, 'users without profile', User.objects.filter(profile=None).exclude(is_superuser=True), bold)
    add_match_based_sheet(book, 'matches', Match.objects.all())
    
    book.close()
    output.seek(0)
    
    return output

def create_and_assign_threads():
    matches = Match.objects.all()
    for match in matches:
        thread = Thread(name=get_thread_name(match.user1.user.pk, match.user2.user.pk))
        thread.save()
        thread.allowed_users.add(match.user1.user)
        thread.allowed_users.add(match.user2.user)
        thread.save()
        match.matched_thread = thread
        match.save()

def send_match_mail(userprofile):
    try:
        match = Match.objects.get(Q(user1=userprofile) | Q(user2=userprofile))
    except:
        match = None
    
    if match == None:
        plaintext_message = not_match_message()
        html_message = render_to_string(
            'emails/match.html',
            {
                'title': plaintext_message['subject'],
                'header': plaintext_message['message'],
            }
        )
        send_mail(
            plaintext_message['subject'],
            plaintext_message['message'],
            settings.NOREPLY_EMAIL,
            [userprofile.user.email],
            html_message=html_message
        )  
    elif match.exact:
        plaintext_message = exact_match_message()
        html_message = render_to_string(
            'emails/match.html',
            {
                'title': plaintext_message['subject'],
                'header': plaintext_message['message'],
                'url': f'{settings.WWW_SITE}/chat',
            }
        )
        send_mail(
            plaintext_message['subject'],
            plaintext_message['message'],
            settings.NOREPLY_EMAIL,
            [userprofile.user.email],
            html_message=html_message
        )
    elif not match.exact:
        plaintext_message = not_exact_match_message()
        html_message = render_to_string(
            'emails/match.html',
            {
                'title': plaintext_message['subject'],
                'header': plaintext_message['message'],
                'url': f'{settings.WWW_SITE}/chat',
            }
        )
        send_mail(
            plaintext_message['subject'],
            plaintext_message['message'],
            settings.NOREPLY_EMAIL,
            [userprofile.user.email],
            html_message=html_message
        )
