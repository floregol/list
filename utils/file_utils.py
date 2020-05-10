import os


LIST_PATH = 'data'
MAIN_LIST_NAME = 'main'
MAIN_LIST_FILENAME = MAIN_LIST_NAME + '.txt'
MAIN_LIST_FILEPATH = os.path.join(LIST_PATH, MAIN_LIST_FILENAME)




def prompt_for_item():
    item = input("item to add : ")
    if item == '':
        return None
    else:
        return item
        
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

        with open(MAIN_LIST_FILEPATH, "w") as f:
            f.write(MAIN_LIST_NAME + '\n')
    

def process_line_item(line_file):
    return line_file.strip()


def list_name_to_path(list_name):
    return os.path.join(LIST_PATH, list_name + '.txt')