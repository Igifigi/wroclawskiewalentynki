from django.db import models
from django.utils.translation import gettext_lazy as _

# What class are you in?
class Q1(models.IntegerChoices):
    FIRST = 1, _('First'),
    SECOND = 2, _('Second'),
    THIRD = 3, _('Third'),
    FOURTH = 4, _('Fourth'),

# You identify yourself as:
class Q2(models.IntegerChoices):
    BOY = 1, _('Boy'),
    GIRL = 2, _('Girl'),
    NON_BINARY = 3, _('Non-binary person'),


# Who would you like to be matched with?
class Q3(models.IntegerChoices):
    BOY = 1, _('Boy'),
    GIRL = 2, _('Girl'),
    NON_BINARY = 3, _('Non-binary person'),
    IDC = 4, _('I don\'t care'),

# I want to meet:
class Q4(models.IntegerChoices):
    DATE = 1, _('For a date 😎'),
    INTERESTING = 2, _('To meet someone interesting'),

# The ideal date/meeting is:
class Q5(models.IntegerChoices):
    CINEMA = 1, _('Cinema'),
    MUSEUM = 2, _('Museum'),
    COFFEE = 3, _('Coffee'),
    DRINK = 4, _('Drink (or three)'),
    BILLARDS = 5, _('Billards'),

# You have a geo test tomorrow, but you were supposed to meet your friends today. What do you do?
class Q6(models.IntegerChoices):
    MEETING = 1, _('I\'m going to a meeting'),
    STUDY = 2, _('I go home and study for the test'),

# In free time:
class Q7(models.IntegerChoices):
    GAMES = 1, _('I play Fifa/LOL/CS or whatever'),
    FRIENDS = 2, _('I meet with friends'),
    READ = 3, _('I read'),
    SPORT = 4, _('Sports/gym 😎💪🏋'),
    WATCH = 5, _('I watch - movies, series'),

# If you had to listen to one musician for the next year, it would be:
class Q8(models.IntegerChoices):
    MATA = 1, 'Mata',
    FREDDIE = 2, 'Freddie Mercury',
    MALIK = 3, 'Malik Montana',
    LUDWIG = 4, 'Ludwig van BeethovenDrake',
    FRANK = 5, 'Frank Sinatra',
    LANA = 6, 'Lana Del Rey',
    ZBIGNIEW = 7, 'Zbigniew Wodecki',
    RED_HOT = 8, 'Red Hot Chili Peppers',
    DAWID = 9, 'Dawid Podsiadło',
    BTS = 10, 'BTS',
    Harry = 11, 'Harry Styles',
    Arctic = 12, 'Arctic Monkeys',
    PLEYBOY = 13, 'Pleyboy Carti',

# On a scale of 1 to 10, how decisive are you?
class Q9(models.IntegerChoices):
    ONE = 1, '1',
    TWO = 2, '2',
    THREE = 3, '3',
    FOUR = 4, '4',
    FIVE = 5, '5',
    SIX = 6, '6',
    SEVEN = 7, '7',
    EIGHT = 8, '8',
    NINE = 9, '9',
    TEN = 10, '10',

# Dogs or perhaps cats?
class Q10(models.IntegerChoices):
    DOGS = 1, _('Dogs, cats are too independent'),
    CATS = 2, _('Cats, dogs stink'),
    NO_ANIMALS = 3, _('I don\'t like animals'),
    ALL_ANIMALS = 4, _('Doesn\'t matter, I love all animals'),

# How spontaneous are you?
class Q11(models.IntegerChoices):
    PLAN_EVERYTHING = 1, '1 - ' + _('I plan everything, ordnung muss sein'),
    TWO = 2, '2',
    THREE = 3, '3',
    FOUR = 4, '4',
    FULL_SPONTANEITY = 5, '5 - ' + _('Full of spontaneity'),

# Do you avoid serious topics?
class Q12(models.IntegerChoices):
    AVOID_SERIOUS_TOPICS = 1, _('Yes, I\'d rather not bother with them'),
    NO_AVOID_SERIOUS_TOPICS = 2, _('No, nothing that human is to me strange'),

# My favorite subject at school is:
class Q13(models.IntegerChoices):
    MATHEMATICS_PHYSICS = 1, _('Mathematics/Physics'),
    POLISH = 2, _('Polish'),
    GEOGRAPHY = 3, _('Geography'),
    IT = 4, _('IT'),
    HISTORY_SOCIETY = 5, _('History/Society knowledge'),
    FOREIGN_LANGUAGES = 6, _('Foreign Languages'),
    BIOLOGY_CHEMISTRY = 7, _('Biology/Chemistry'),
    PE = 8, _('PE'),

Q1_matches = [
    (1,1),
    (2,2),
    (2,3),
    (3,3),
    (4,4),
]

Q8_matches = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (1,3),
    (1-5),
    (2-9),
    (4-6),
    (4-8),
    (7,12),
    (9,13),
    (10,12),
    (12,13),
]

Q9_matches = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (1,2),
    (1,3),
    (2,3),
    (4,5),
    (4,6),
    (5,6),
    (7,8),
    (7,9),
    (7,10),
    (8,9),
    (8,10),
    (9,10),
]

Q10_matches = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (1,4),
    (2,4),
]

Q11_matches = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (2,3),
    (2,4),
    (3,4),
]

Q13_matches = [
    (1,4),
    (2,5),
    (3,7),
    (6,6),
    (7,7),
]
