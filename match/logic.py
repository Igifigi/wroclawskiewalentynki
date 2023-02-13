"""
This algorithm and the entire content of this file is the private property of Ignacy Świderski.
It cannot be used, copied, modified or distributed without the consent of the author.
(C) 2023
"""

from django.db.models import Q

from .models import UserProfile, Match
from .match_settings import *


def common_parameters_count(user1, user2):
    common = 0

    t1 = (user1.question1, user2.question1)
    t2 = tuple(reversed(t1))
    common += t1 in Q1_matches or t2 in Q1_matches
    common += user1.question5 == user2.question5
    common += user1.question6 == user2.question6
    common += user1.question7 == user2.question7
    t1 = (user1.question8, user2.question8)
    t2 = tuple(reversed(t1))
    common += t1 in Q8_matches or t2 in Q8_matches
    t1 = (user1.question9, user2.question9)
    t2 = tuple(reversed(t1))
    common += t1 in Q9_matches or t2 in Q9_matches
    t1 = (user1.question10, user2.question10)
    t2 = tuple(reversed(t1))
    common += t1 in Q10_matches or t2 in Q10_matches
    t1 = (user1.question11, user2.question11)
    t2 = tuple(reversed(t1))
    common += t1 in Q11_matches or t2 in Q11_matches
    common += user1.question12 == user2.question12
    t1 = (user1.question13, user2.question13)
    t2 = tuple(reversed(t1))
    common += t1 in Q13_matches or t2 in Q13_matches

    return common


def get_the_chosen_one(profile, matches, exact):
    matches = list(matches)
    answer = list(
        zip(matches, [common_parameters_count(profile, user) for user in matches]))

    if answer:
        result = max(answer, key=lambda t: t[1])
        m = Match(user1=profile, user2=result[0], exact=exact)
        profile.matched = True
        result[0].matched = True

        profile.save()
        result[0].save()
        m.save()


def make_matches():

    # First stage
    ups = UserProfile.objects.filter(matched=False)
    for u in ups:
        if UserProfile.objects.get(pk=u.pk).matched:
            continue
        matched = UserProfile.objects.filter(
            Q(matched=u.matched) &
            ~Q(school=u.school) &
            (Q(question3=u.question2) | Q(question3=Q3.IDC)) &
            Q(question4=u.question4)
        )
        if not u.question3 == Q3.IDC:
            matched = matched.filter(
                Q(question2=u.question3)
            )
        get_the_chosen_one(u, matched, True)

    # Second stage
    ups = UserProfile.objects.filter(matched=False)
    for u in ups:
        if UserProfile.objects.get(pk=u.pk).matched or not u.question4 == Q4.INTERESTING:
            continue
        matched = UserProfile.objects.filter(
            Q(matched=u.matched) &
            ~Q(school=u.school) &
            Q(question4=u.question4)
        )
        get_the_chosen_one(u, matched, False)

    # Third stage
    ups = UserProfile.objects.filter(matched=False)
    for u in ups:
        if UserProfile.objects.get(pk=u.pk):
            continue
        matched = UserProfile.objects.filter(
            Q(matched=u.matched) &
            Q(question4=u.question4)
        )
        get_the_chosen_one(u, matched, False)
