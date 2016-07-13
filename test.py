"""
user_input = input('what would you like le piggy to say: ')

print('You entered:')
print(user_input)

vegetable = input('Enter a name of a vegetable: ')
print('{} is a lovely vegetable.'.format(vegetable))

user_input = input('Please type something and press enter: ')

test_length = len(user_input)
top_line = ('_' * test_length)
bottom_line = ('-' * test_length)

print('Characters entered:')
print('         {}'.format('_' * test_length))
print('       < {} >'.format(user_input))
print('         {}'.format('-' * test_length))

FINISH CHAPTER
"""

"""# The cost of one server per hour.
cost_per_hour = 1.02
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
cost_per_day_for_20 = (24 * cost_per_hour) * 20
cost_per_month_for_20 = (30 * cost_per_day) * 20
total_cash = 1836
duration_till_bankrupt = total_cash / cost_per_day

# Display the results.
print('Cost to operate ONE server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate ONE server per month is ${:.2f}.'.format(cost_per_month))
print('Cost to operate TWENTY servers per day is ${:.2f}.'.format(cost_per_day_for_20))
print('Cost to operate TWENTY servers per month is ${:.2f}.'.format(cost_per_month_for_20))
print('Cost to operate ONE server for as long as possible is {:.2f}.'.format(duration_till_bankrupt))
FINISH CHAPTER
"""

'''user_input = input('What distance are you traveling in miles?')

if user_input < 3:
    print('walk yo')
elif user_input > 3 and user_input < 300:
    print('drive bitch')
elif user_input >= 300:
    print('ya gotta fly homie')


def say_hello(name = 0):
    """Simply prints a name."""
    print('Hello {}!'.format(name))

help(say_hello)
FINISH CHAPTER
'''

'''
def get_user_input(word_class):
    """This function gets the user input."""
    return input('Enter a word that is a {1}: '.format(word_class))

def create_story():
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')
    the_story = get_user_input(noun, verb, adjective)
    print_story(fill_in_the_blanks)

def fill_in_the_blanks(user_adjective, user_noun, user_verb):
    """So this is where I'll somehow replace the string"""
    story = ('There was once a {0} {1} and he could {2} very high.'.format(user_adjective, user_noun, user_verb))
    return story

def get_input_then_fill_blanks():
    """All together now"""
    input = get_user_input(word_class)
    fill_in_the_blanks(input)

get_input_then_fill_blanks()
FINISH CHAPTER
'''

'''
user_input = input('Enter an item for your grocery list. Press <ENTER> when done:')
arrayOfInput = []
finished = False
index = 0

while not finished:
    user_input = input('Enter an item for your grocery list. Press <ENTER> when done:')
    if len(user_input) == 0:
        finished = True
    else:
        arrayOfInput.append(user_input)
        print('Item added.')

print('\n')
print('Your Grocery List:')
for item in arrayOfInput:
    print(item)

FINISH CHAPTER
'''





































