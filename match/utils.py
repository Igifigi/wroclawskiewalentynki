from io import BytesIO
from django.http import HttpResponse
from django.contrib.auth.models import User
from xlsxwriter.workbook import Workbook

from .models import UserProfile, School
from .match_settings import *

def add_user_based_sheet(workbook, title, queryset, bold):
    sheet = workbook.add_worksheet(f'[USER] {title}')
    sheet.write_row(0, 0, ['id', 'username', 'first name', 'last name', 'email', 'is active'])
    sheet.set_row(0, None, bold)
    sheet.set_column(0,0,2)
    sheet.set_column(1,1,5)
    sheet.set_column(2,4,10)
    sheet.set_column(5,5,2)
    
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
    sheet = workbook.add_worksheet(f'[USERPROFILE] {title}')
    questions = [UserProfile._meta.get_field(field).verbose_name for field in [field.column for field in UserProfile._meta.fields if 'question' in str(field)]]
    sheet.write_row(0, 0, ['id', 'username'] + questions + ['ig', 'fb', 'tt', 'terms accepted'])
    sheet.set_row(0, None, bold)
    sheet.set_column(0,0,2)
    sheet.set_column(1,17,5)
    sheet.set_column(18,18,2)
    
    for index, userprofile in enumerate(queryset):
        data = (
            userprofile.id,
            userprofile.user.username,
            School.objects.get(code=userprofile.school).name,
            Q1.choices[list(zip(*Q1.choices))[0].index(userprofile.question1)],
            Q2.choices[list(zip(*Q2.choices))[0].index(userprofile.question2)],
            Q3.choices[list(zip(*Q3.choices))[0].index(userprofile.question3)],
            Q4.choices[list(zip(*Q4.choices))[0].index(userprofile.question4)],
            Q5.choices[list(zip(*Q5.choices))[0].index(userprofile.question5)],
            Q6.choices[list(zip(*Q6.choices))[0].index(userprofile.question6)],
            Q7.choices[list(zip(*Q7.choices))[0].index(userprofile.question7)],
            Q8.choices[list(zip(*Q8.choices))[0].index(userprofile.question8)],
            Q9.choices[list(zip(*Q9.choices))[0].index(userprofile.question9)],
            Q10.choices[list(zip(*Q10.choices))[0].index(userprofile.question10)],
            Q11.choices[list(zip(*Q11.choices))[0].index(userprofile.question11)],
            Q12.choices[list(zip(*Q12.choices))[0].index(userprofile.question12)],
            Q13.choices[list(zip(*Q13.choices))[0].index(userprofile.question13)],
            userprofile.instagram,
            userprofile.facebookm,
            userprofile.tiktok,
            "YES" if userprofile.accept_tems else "NIE",
        )
        sheet.write_row(index + 1, 0, data)

def export_user_related_database_as_xlsx():
    output = BytesIO
    workbook = Workbook(output)
    bold = workbook.add_format({'bold': True})
    
    add_user_based_sheet(workbook, 'all users', User.objects.all().exclude(is_superuser=True), bold)
    add_profile_based_sheet(workbook, 'matched users', UserProfile.objects.filter(matched=True), bold)
    add_profile_based_sheet(workbook, 'non-matched users', UserProfile.objects.filter(matched=False), bold)
    add_user_based_sheet(workbook, 'users without profile', User.objects.filter(profile=None), bold)
    
    workbook.close()
    output.seek(0)
    
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=user-related_db_WW.xlsx"
    return response
