import click

TGREEN = '\033[32m'
TEND = '\033[m'
TRED = '\033[31m'


def print_color(text, color):
    if color == 'G':
        print(TGREEN + text, TEND)
    elif color == 'R':
        print(TRED + text, TEND)


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


def announce_list(list_name):
    print('List : ', list_name)
    print('-----------------')