"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    insert_position_options = """
    Where would you like to add the item?
    1. Beginning 
    2. Middle
    3. End 
    >>> 
    """

    item = raw_input("Enter an item:")

    has_dup = False
    for curr_item in my_list:
        if curr_item.lower() == item.lower():
            print "Item already exists."
            has_dup = True
            break

    if has_dup == False:

        insert_position = raw_input(insert_position_options)

        if insert_position == "1":
            my_list.insert(0, item)
        elif insert_position == "2":
            middle_index = len(my_list) / 2
            my_list.insert(middle_index, item)
        elif insert_position == "3":
            my_list.append(item)
        else:
            print "unknown input"

    return my_list

def delete_from_beginning_of_list(my_list):
    """Delete an item from the beginning of the list """
    if len(my_list) == 0:
        print "There is nothing to delete."    
    else:
        del my_list[0]

    return my_list

def view_list(my_list):
    """Print each item in the list."""

    for item in my_list:
        print item

def edit_list(my_list):
    """Edit an item at a certain index. """

    new_item = raw_input("What is the new item?")
    index = raw_input("Indicate the index of the item you would like to edit.")

    if len(my_list) > 0:
        if int(index) > (len(my_list) - 1):
            print "Invalid index"
        else:
            #print new_item
            my_list[int(index)] = new_item
            #print my_list[index]
    else:
        print "There is nothing to edit."

    return my_list


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    D. Delete an item from the beginning of the list
    E. Edit list
    >>> """

    while True:
        # Collect input and include your if/elif/else statements here.
        user_input = raw_input(user_options)

        if user_input.lower() == "a":
            add_to_list(my_list)
        elif user_input.lower() == "b":
            view_list(my_list)
        elif user_input.lower() == "c":
            break
        elif user_input.lower() == "d" :
            delete_from_beginning_of_list(my_list)
        elif user_input.lower() == "e":
            edit_list(my_list)
        else:
            print "Unknown input. Please try again."

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

