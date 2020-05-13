import click

TGREEN = '\033[32m'
TEND = '\033[m'
TRED = '\033[31m'

valid_yes = ['yes', 'y', 'YES', 'Y']
valid_no = ['no', 'n', 'NO', 'N']

def ask_question_user(question):
    answer = input(question)
    if answer in valid_yes:
        return True
    return False

def print_color(text, color):
    if color == 'G':
        print(TGREEN + text, TEND)
    elif color == 'R':
        print(TRED + text, TEND)

def tell_the_user_he_is_lazy():
    print()
    print('wow so lazy')
    input()
def validate_input(name):
    while True:
        answer = input('Is ' + name + " right? ")
        if answer in valid_yes:
            return True
        elif answer in valid_no:
            return False
        else:
            print('Please choose from ' + str(valid_yes) + 'or' + str(valid_no))


def announce_delete_step():
    announce_step('Mark as completed')


def announce_add_step():
    announce_step('Add elements')


def announce_display_step():
    announce_step('Lists')


def announce_step(step_message):
    click.clear()
    print('######    ' + step_message + '    ######')
    print()
    print()

def announce_add_list():
    announce_step('Adding list')

def announce_delete_list():
    announce_step('Deleting lists')

def announce_list(list_name):
    print('List : ', list_name)
    print('-----------------')