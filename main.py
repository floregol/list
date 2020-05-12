import os
import sys
import click
from utils.display_utils import *
from utils.file_utils import *

MAIN_LIST_NAME = 'main'
DELETED_MARKER = '(done)'


def load_items_from_list(list_name):
    return iterate_items_from_list(list_name, process_line_item)


def check_if_deleted(item):
    return item[0:6] == DELETED_MARKER


def dispay_list(list_name=MAIN_LIST_NAME):

    announce_display_step()
    for list_name in all_lists_in_order():
        list_items = load_items_from_list(list_name)
        announce_list(list_name)
        for item in list_items[1:]:
            if check_if_deleted(item):  # to be deleted print in red
                text = '\t - %s' % item
                print_color(text, 'R')
            else:
                print('\t - %s' % item)
        print()


def add_to_list(list_name=MAIN_LIST_NAME):
    isFirst = True
    update_this_list = True
    for list_name in all_lists_in_order():

        if not isFirst:  # ask if we should continue
            update_this_list = ask_user('Should we update list ' + list_name + ' ?')
        if update_this_list:
            announce_add_step()
            announce_list(list_name)
            adding_items = True
            list_items = []
            while adding_items:
                item = prompt_for_item()
                if item is not None:
                    list_items.append(item)
                else:
                    adding_items = False
            list_filepath = list_name_to_path(list_name)
            with open(list_filepath, "a") as f:
                for item in list_items:
                    f.write("%s\n" % item)

        isFirst = False


def delete_from_list(list_name=MAIN_LIST_NAME):
    isFirst = True
    update_this_list = True
    for list_name in all_lists_in_order():

        if not isFirst:  # ask if we should continue
            update_this_list = ask_user('Should we update list ' + list_name + ' ?')
        if update_this_list:
            announce_delete_step()
            announce_list(list_name)
            list_items = load_items_from_list(list_name)
            line_to_mark = []  # mark the line as deleted
            line_to_delete = []  # delete the items previously deleted

            for i, item in enumerate(list_items[1:]):
                if check_if_deleted(item):
                    line_to_delete.append(i)
                else:
                    answer = input('Did you completed -' + item + ' ? ')
                    if answer == 'd' or answer == 'y' or answer == 'yes':
                        print('Completed the task', item)
                        line_to_mark.append(i)

            if len(line_to_mark) > 0 or len(line_to_delete) > 0:
                raw_lines = iterate_items_from_list(list_name, lambda x: x)
                list_filepath = list_name_to_path(list_name)
                with open(list_filepath, "w") as f:
                    f.write(list_name + '\n')
                    for i, line in enumerate(raw_lines[1:]):
                        if i in line_to_mark:
                            f.write(DELETED_MARKER + line)
                        elif not (i in line_to_delete):
                            f.write(line)
                        else:
                            print('not', i)
                            print(line_to_delete)
            else:
                print()
                print('wow so lazy')
                input()

        isFirst = False


def add_list():
    new_list_name = prompt_for_list_name()
    if new_list_name is not None:
        create_list_file(new_list_name)
        add_to_list(new_list_name)
        dispay_list(new_list_name)


def delete_list():
    pass


if __name__ == '__main__':
    check_set_up()

    if len(sys.argv) == 1:  # default mode, go throught last updated list, add to last udated list and display lists
        delete_from_list()
        add_to_list()
        dispay_list()

    elif sys.argv[1] == '-m':  # manage mode
        add_list()
        delete_list()
