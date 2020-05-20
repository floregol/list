
DELETED_MARKER = '(done)'
PERCENT_RED_DISPLAY = 80
from datetime import datetime

class Item:
    def __init__(self, todo, creation_time=None, due_date=None):
        self.todo = todo
        self.due_date = due_date
        self.creation_time = creation_time
        self.is_time_based_item =  (creation_time is not None) and (due_date is not None)
        self.is_completed = self.check_if_completed()

    

    def item_to_str_for_file(self):
        if self.is_time_based_item:
            return "%s\t%s\t%s\n" % (self.todo, str(self.creation_time.strftime("%Y-%m-%d-%H-%M-%S")),
                                                  str(self.due_date.strftime("%Y-%m-%d-%H-%M-%S")))
        else:
            return "%s\n" % self.todo

    def check_if_completed(self):
        return self.todo[:len(DELETED_MARKER)] == DELETED_MARKER

    def check_how_close_to_completion(self):
        time_diff = self.due_date - datetime.now()
        time_diff_in_sec = time_diff.total_seconds()

        days = divmod(time_diff_in_sec, 86400)  # Get days (without [0]!)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)

        total_diff = self.due_date - self.creation_time
        total_diff_in_sec = total_diff.total_seconds()

        percent_ongoing = 100 * (1 - (time_diff_in_sec / total_diff_in_sec))

        if days[0] > 0:
            time_display = "\t(due in %d day(s), %.2f%% time passed)" % (days[0], percent_ongoing)
        elif hours[0] > 0:
            time_display = "\t(due in %d hour(s), %.2f%% time passed)" % (hours[0], percent_ongoing)
        elif minutes[0] > 0:
            time_display = "\t(due in %d minute(s), %.2f%% time passed)" % (minutes[0], percent_ongoing)

        
        return percent_ongoing, time_display


    def display_item(self):
        color = 'B'
        if self.is_completed:
            color = 'G'
        elif self.is_time_based_item:
            percent, time_display = self.check_how_close_to_completion()
            if percent > PERCENT_RED_DISPLAY:
                color = 'R'
            return self.todo + time_display, color
        return self.todo, color


    
def str_to_token(line_file):
    line_file = line_file.strip()
    return line_file.split('\t')