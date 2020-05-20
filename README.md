# Description

## Small command line program to keep track of lists of things to do.
The program iterates through 3 steps. To run : `python main.py -u` with -u for update to add/delete items.
### [1] Delete items
### [2] Add items
### [3] Display list of items

To manage the lists, run in manage mode : `python main.py -m`

To only display the lists, run in simple mode : `python main.py`

To add items with a deadline, run : `python main.py -u -t`. After adding an item, you will be prompt to enter the amount of time to compete. 
The format is : [# number of time unit][# time unit]. The possible time units are : m for month, w for week, d for days, h for hours. So if you have 3 days to complete the item, put in 3d.
At 50 and 80 % of the allocated time passed time, the color of the item will change color.

### [1] Add list
### [2] Delete list

## How to use

### [1] To delete completed items, press y when they appear. If not, press enter. All items will be presented. If there is no items, we go straight to the add step

### [2] To add item, type in something then press enter. To not add anything, just press enter.

### [3] Display step will print all the items. Items who were just deleted will be displayed in red. Items that were deleted previously are removed.