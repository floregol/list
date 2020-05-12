import os
from os import listdir
from os.path import isfile, join
from utils. display_utils import validate_input
LIST_PATH = 'data'
MAIN_LIST_NAME = 'main'
MAIN_LIST_FILENAME = MAIN_LIST_NAME + '.txt'
MAIN_LIST_FILEPATH = os.path.join(LIST_PATH, MAIN_LIST_FILENAME)


def all_lists_in_order():
    
    list_names = [f.split('.')[0] for f in listdir(LIST_PATH) if isfile(join(LIST_PATH, f))]
    return list_names

def prompt_for_item():
    item = input("item to add : ")
    if item =='^[[D':
        print('yes')
    if item == '':
        return None
    else:
        return item

def prompt_for_list_name():
    while True:
        list_name = input("list to create : ")
        if list_name == '':
            print("Ok no new lists")
            return None
        else:
            if validate_input(list_name):
                return list_name
            
            

def create_list_file(list_name):
    list_filepath = list_name_to_path(list_name)
    with open(list_filepath, "w") as f:
        f.write(list_filepath + '\n')

def iterate_items_from_list(list_name, function):
    list_filepath = list_name_to_path(list_name)

    list_items = []
    with open(list_filepath, 'r') as f:
        for line in f.readlines():
            list_items.append(function(line))
    return list_items

def check_set_up():  # make sure a list is there and the fodlers is all set up
    if os.path.exists(MAIN_LIST_FILEPATH):
        return
    else:  # create it
        try:
            os.makedirs(os.path.dirname(MAIN_LIST_FILEPATH))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

        create_list_file(MAIN_LIST_NAME)
    

def process_line_item(line_file):
    return line_file.strip()


def list_name_to_path(list_name):
    return os.path.join(LIST_PATH, list_name + '.txt')