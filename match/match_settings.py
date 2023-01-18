from django.utils.translation import gettext as _

# What class are you in?
Q1 = (
    (1, _('First')),
    (2, _('Second')),
    (3, _('Third')),
    (4, _('Fourth')),
)

# You identify yourself as:
Q2 = (
    (1, _('Boy')),
    (2, _('Girl')),
    (3, _('Non-binary person')),
)

# Who would you like to be matched with?
Q3 = (
    (1, _('Boy')),
    (2, _('Girl')),
    (3, _('Non-binary person')),
    (4, _('I don\'t care')),
)

# I want to meet:
Q4 = (
    (1, _('For a date 😎')),
    (2, _('To meet someone interesting')),
)

# The ideal date/meeting is:
Q5 = (
    (1, _('Cinema')),
    (2, _('Museum')),
    (3, _('Coffee')),
    (4, _('Drink (or three)')),
    (5, _('Billards')),
)

# You have a geo test tomorrow, but you were supposed to meet your friends today. What do you do?
Q6 = (
    (1, _('I\'m going to a meeting')),
    (2, _('I go home and study for the test')),
)

# In free time:
Q7 = (
    (1, _('I play Fifa/LOL/CS or whatever')),
    (2, _('I meet with friends')),
    (3, _('I read')),
    (4, _('Sports/gym 😎💪🏋')),
    (5, _('I watch - movies, series')),
)

# If you had to listen to one musician for the next year, it would be:
Q8 = (
    (1, 'Mata'),
    (2, 'Freddie Mercury'),
    (3, 'Malik Montana'),
    (4, 'Ludwig van BeethovenDrake'),
    (5, 'Frank Sinatra'),
    (6, 'Lana Del Rey'),
    (7, 'Zbigniew Wodecki'),
    (8, 'Red Hot Chili Peppers'),
    (9, 'Dawid Podsiadło'),
    (10, 'BTS'),
    (11, 'Harry Styles'),
    (12, 'Arctic Monkeys'),
    (13, 'Pleyboy Carti'),
)

# On a scale of 1 to 10, how decisive are you?
Q9 = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
)

# Dogs or perhaps cats?
Q10 = (
    (1, _('Dogs, cats are too independent')),
    (2, _('Cats, dogs stink')),
    (3, _('I don\'t like animals')),
    (4, _('Doesn\'t matter, I love all animals')),
)

# How spontaneous are you?
Q11 = (
    (1, '1 - ' + _('I plan everything, ordnung muss sein')),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5 - ' + _('Full of spontaneity')),
)

# Do you avoid serious topics?
Q12 = (
    (1, _('Yes, I\'d rather not bother with them')),
    (2, _('No, nothing that human is to me strange')),
)

# My favorite subject at school is:
Q13 = (
    (1, _('Mathematics/Physics')),
    (2, _('Polish')),
    (3, _('Geography')),
    (4, _('IT')),
    (5, _('History/Society knowledge')),
    (6, _('Foreign Languages')),
    (7, _('Biology/Chemistry')),
    (8, _('PE')),
)
