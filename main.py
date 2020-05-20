import sys, re
from datetime import datetime
from utils.display_utils import *
from utils.file_utils import *
from termcolor import colored
from utils.Item import Item
MAIN_LIST_NAME = 'main'
DELETED_MARKER = '(done)'


def display_list():
    announce_display_step()  # print on cmd that we are on display step
    for list_name in all_lists_in_order():
        list_items = iterate_items_from_list(list_name, process_line_item)
        announce_list(list_name)
        for item in list_items[1:]:
            text_display, color = item.display_item()
            print_color('\t - %s' % text_display, color)

        print()


def add_to_list(time_option=False, single_list_addition_name=None):
    isFirst = True
    update_this_list = True
    for list_name in all_lists_in_order():
        if not isFirst:  # ask if we should continue
            update_this_list = ask_question_user('Should we update list ' + list_name + ' ? ')
        if update_this_list:
            announce_add_step()
            announce_list(list_name)
            adding_items = True
            list_items = []
            while adding_items:
                text_item = prompt_for_item()
                if text_item is not None:
                    if time_option:
                        due_date = prompt_for_deadline()
                        creation_time = datetime.now()
                        item = Item(todo=text_item, creation_time=creation_time, due_date=due_date)
                    else:
                        item = Item(todo=text_item)
                    list_items.append(item)
                else:
                    adding_items = False
            list_filepath = list_name_to_path(list_name)
            with open(list_filepath, "a") as f:
                for item in list_items:
                    f.write(item.item_to_str_for_file())
        if single_list_addition_name is not None:  # single list addition, we dont ask for the other list
            return

        isFirst = False


def delete_from_list():
    isFirst = True
    update_this_list = True
    for list_name in all_lists_in_order():

        if not isFirst:  # ask if we should continue
            update_this_list = ask_question_user('Should we update list ' + list_name + ' ? ')
        if update_this_list:
            announce_delete_step()
            announce_list(list_name)
            list_items = iterate_items_from_list(list_name, process_line_item)
            line_to_mark = []  # mark the line as deleted
            line_to_delete = []  # delete the items previously deleted

            for i, item in enumerate(list_items[1:]):
                if item.is_completed:
                    line_to_delete.append(i)
                else:
                    if ask_question_user('Did you completed - ' + item.todo + ' ? '):
                        print('Completed the task', item.todo)
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

            elif len(list_items) > 1:  # if the list contained items to start
                tell_the_user_he_is_lazy()
        else:  # still have to go throught items to remove unused
            list_items = iterate_items_from_list(list_name, process_line_item)
            line_to_delete = []  # delete the items previously deleted

            for i, item in enumerate(list_items[1:]):
                if item.is_time_based_item:
                    line_to_delete.append(i)

            if len(line_to_delete) > 0:
                raw_lines = iterate_items_from_list(list_name, lambda x: x)
                list_filepath = list_name_to_path(list_name)
                with open(list_filepath, "w") as f:
                    f.write(list_name + '\n')
                    for i, line in enumerate(raw_lines[1:]):
                        if not (i in line_to_delete):
                            f.write(line)

        isFirst = False


def add_list():
    announce_add_list()
    new_list_name = prompt_for_list_name()
    if new_list_name is not None:
        create_list_file(new_list_name)
        add_to_list(single_list_addition_name=new_list_name)
        display_list()


def delete_list():
    announce_delete_list()
    for list_name in all_lists_in_order():
        if ask_question_user('Should we delete list ' + list_name + ' ? '):
            delete_list_file(list_name)


if __name__ == '__main__':
    check_set_up()

    if len(sys.argv) == 1:  # default mode, display lists
        display_list()

    elif sys.argv[1] == '-m':  # manage mode
        add_list()
        delete_list()
        display_list()

    elif sys.argv[1] == '-u':  # go through last updated list, add to last updated list and display
        time_option = (len(sys.argv) > 2) and (sys.argv[2] == '-t')
        delete_from_list()
        add_to_list(time_option=time_option)
        display_list()