
import os
import click
LIST_PATH = 'data'
MAIN_LIST_NAME = 'main'
MAIN_LIST_FILENAME = MAIN_LIST_NAME + '.txt'
MAIN_LIST_FILEPATH = os.path.join(LIST_PATH, MAIN_LIST_FILENAME)


def check_set_up():  # make sure a list is there and the fodlers is all set up
    if os.path.exists(MAIN_LIST_FILEPATH):
        return
    else:  # create it
        try:
            os.makedirs(os.path.dirname(MAIN_LIST_FILEPATH))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

        with open(MAIN_LIST_FILEPATH, "w") as f:
            f.write(MAIN_LIST_NAME + '\n')


def process_line_item(line_file):
    return line_file.strip()

def list_name_to_path(list_name):
    return os.path.join(LIST_PATH, list_name + '.txt')

def load_items_from_list(list_name):
    list_filepath = list_name_to_path(list_name)

    list_items = []
    with open(list_filepath, 'r') as f:
        for line in f.readlines():
            list_items.append(process_line_item(line))
    return list_items


def dispay_list(list_name=MAIN_LIST_NAME):
    # check up
    check_set_up()
    click.clear()
    list_items = load_items_from_list(list_name)
    print('LIST :  %s' % list_items[0])
    for item in list_items[1:]: 
        print('\t - %s' % item)


def prompt_for_item():
    item = input ("item to add : ") 
    if item == '':
        return None
    else:
        return item
    

def add_to_list(list_name=MAIN_LIST_NAME):
    click.clear()
    adding_items = True
    list_items = []
    while adding_items :
        item = prompt_for_item()
        if item is not None:
            list_items.append(item)
        else:
            adding_items = False
    list_filepath = list_name_to_path(list_name)
    with open(list_filepath, "a") as f:
        for item in list_items:
            f.write("%s\n" % item)


if __name__ == '__main__':
    
    add_to_list()
    dispay_list()
