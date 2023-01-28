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

def make_matches():
    userprofiles = list(UserProfile.objects.all().exclude(matched=True))
    
    for u in userprofiles:
        
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
        
        matched = list(matched)
        answer = list(zip(matched, [common_parameters_count(u, user) for user in matched]))
        
        if answer:
            result = min(answer, key = lambda t: t[1])
            m = Match(user1=u, user2=result[0])
            u.matched = True
            result[0].matched = True
            
            u.save()
            result[0].save()
            m.save()
            
            userprofiles.remove(u)
            userprofiles.remove(result[0])
    
