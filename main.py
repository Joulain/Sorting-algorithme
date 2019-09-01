# ## Writing a sorting programme ## version 1.5


# ## start import ##

# import information to sort
import sys
text = ["x", "b", "a", "f", "e"]
# ## end import ##


# define sort

# ## bubble sort ##     worst case complexity O(n²)     Best case complexity O(
def bubble(arg):

    # get the length of the given argument
    arg_length = len(arg)

    # read all element of the argument
    for i in range(arg_length):

        # reset the presence of swap
        swapped = False

        # compare pairs of element, can't take last one
        for j in range(0, arg_length - i - 1):

            # traverse the array from 0 to n-i-1
            # swap if the element found is greater than the next element
            if arg[j] > arg[j + 1]:

                # we used a swap
                swapped = True
                # swap the two elements
                arg[j], arg[j + 1] = arg[j + 1], arg[j]

        # if we didn't swap two elements, the list is sorted
        if not swapped:
            break

    # return the list sorted
    return arg


# ## reverse bubble sort ##     worst case complexity O(n²)     Best case complexity O(n)
def reverse_bubble(arg):

    # get the length of the given argument
    arg_length = len(arg)

    # read all element of the argument
    for i in range(arg_length):

        # reset the presence of swap
        swapped = False

        # compare pairs of element, can't take last one
        for j in range(0, arg_length - i - 1):

            # traverse the array from 0 to n-i-1
            # swap if the element found is smaller than the next element
            if arg[j] < arg[j + 1]:

                # we used a swap
                swapped = True
                # swap the two elements
                arg[j], arg[j + 1] = arg[j + 1], arg[j]

        # if we didn't swap two elements, the list is sorted
        if not swapped:
            break

    # return the list sorted
    return arg


# ## selection sort ##      complexity O(n²)
def selection(arg):

    # get the length of the given argument
    arg_length = len(arg)

    # read all element of the argument
    for i in range(arg_length):

        # the first minimal element is our first value
        minimal_element_index = i

        # read all other elements of the list
        for j in range(i + 1, arg_length):

            # stock the index of the lowest element from the list
            if arg[minimal_element_index] > arg[j]:

                # save the new minimal element index
                minimal_element_index = j

        # once we have our minimal element we swap it
        arg[minimal_element_index], arg[i] = arg[i], arg[minimal_element_index]

    # return the list sorted
    return arg


# ## reverse selection sort ##      complexity O(n²)
def reverse_selection(arg):

    # get the length of the given argument
    arg_length = len(arg)

    # read all element of the argument
    for i in range(arg_length):

        # the first minimal element is our first value
        minimal_element_index = i

        # read all other elements of the list
        for j in range(i + 1, arg_length):

            # stock the index of the lowest element from the list
            if arg[minimal_element_index] < arg[j]:

                # save the new minimal element index
                minimal_element_index = j

        # once we have our minimal element we swap it
        arg[minimal_element_index], arg[i] = arg[i], arg[minimal_element_index]

    # return the list sorted
    return arg


# ## merging sort ##      complexity O(nLogn)
def merge(arg):

    # get the length and half the length of the given argument
    arg_length = len(arg)
    half = arg_length // 2

    # split the argument before merging
    first_half = arg[:half]
    second_half = arg[half:]

    # if one half has multiple element, use merge function again
    if len(first_half) > 1:
        merge(first_half)
    if len(second_half) > 1:
        merge(second_half)

    # set multiple index for incrementation
    index_first = index_second = index_arg = 0

    # go through both half to sort them
    while index_first < len(first_half) and index_second < len(second_half):

        # if first half is smaller than the second half, stack first half
        if first_half[index_first] < second_half[index_second]:
            arg[index_arg] = first_half[index_first]
            index_first += 1

        # otherwise stack second half, if it is greater or equal to the first one
        else:
            arg[index_arg] = second_half[index_second]
            index_second += 1

        # increment index to not stack element on each other
        index_arg += 1

    # if there is element left on the first half, we can stack them after
    while index_first < len(first_half):
        arg[index_arg] = first_half[index_first]
        index_first += 1
        index_arg += 1

    # same for second half
    while index_second < len(second_half):
        arg[index_arg] = second_half[index_second]
        index_second += 1
        index_arg += 1

    # return the argument sorted
    return arg


# ## reverse merging sort ##      complexity O(nLogn)
def reverse_merge(arg):

    # get the length and half the length of the given argument
    arg_length = len(arg)
    half = arg_length // 2

    # split the argument before merging
    first_half = arg[:half]
    second_half = arg[half:]

    # if one half has multiple element, use merge function again
    if len(first_half) > 1:
        reverse_merge(first_half)
    if len(second_half) > 1:
        reverse_merge(second_half)

    # set multiple index for incrementation
    index_first = index_second = index_arg = 0

    # go through both half to sort them
    while index_first < len(first_half) and index_second < len(second_half):

        # if first half is smaller than the second half, stack first half
        if first_half[index_first] > second_half[index_second]:
            arg[index_arg] = first_half[index_first]
            index_first += 1

        # otherwise stack second half, if it is greater or equal to the first one
        else:
            arg[index_arg] = second_half[index_second]
            index_second += 1

        # increment index to not stack element on each other
        index_arg += 1

    # if there is element left on the first half, we can stack them after
    while index_first < len(first_half):
        arg[index_arg] = first_half[index_first]
        index_first += 1
        index_arg += 1

    # same for second half
    while index_second < len(second_half):
        arg[index_arg] = second_half[index_second]
        index_second += 1
        index_arg += 1

    # return the argument sorted
    return arg


# ## insertion sort ## complexity O(n²)
def insertion(arg):

    # get the argument length
    arg_length = len(arg)

    # read all element of the argument
    for index in range(1, arg_length):

        # save the element to sort on another variable
        key = arg[index]

        # set a new index to manipulate the element without losing track
        sorter = index - 1

        # we manipulate if the key is smaller a previous element
        while sorter >= 0 and key < arg[sorter]:

            # advance the previous element
            arg[sorter + 1] = arg[sorter]

            # decrement
            sorter -= 1

            # place the saved element where the index stopped
        arg[sorter + 1] = key

    # return the argument sorted
    return arg


# ## reverse insertion sort ## complexity O(n²)
def reverse_insertion(arg):

    # get the argument length
    arg_length = len(arg)

    # read all element of the argument
    for index in range(1, arg_length):

        # save the element to sort on another variable
        key = arg[index]

        # set a new index to manipulate the element without losing track
        sorter = index - 1

        # we manipulate if the key is greater a previous element
        while sorter >= 0 and key > arg[sorter]:

            # advance the previous element
            arg[sorter + 1] = arg[sorter]

            # decrement
            sorter -= 1

            # place the saved element where the index stopped
        arg[sorter + 1] = key

    # return the argument sorted
    return arg


# ## help ##
def help(arg):

    helper = "\nAll sort have different complexity \n" \
             "The higher it is, the faster the program will sort \n" \
             "Here is the list of different sort available : \n" \
             "Insertion sort {O(n²)} : insertion \n" \
             "Reverse insertion sort {O(n²)} : rinsertion \n" \
             "Bubble sort {O(n²)} : bubble \n" \
             "Reverse bubble sort {O(n²)} : rbubble \n" \
             "Selection sort {O(n²)} : selection \n" \
             "Reverse selection sort {O(n²)} : rselection \n" \
             "Merging sort {O(nLogn)} : merge \n" \
             "Reverse merging sort {O(nLogn)} : rmerge \n" \
             "\nTo quit the program type exit \n"
    return helper


# ## default answer if no match for the switch ##
def f_default(arg):
    return "this type of sort isn't available"


# ## quit the program ##
def stop(arg):
    sys.exit("you choose to end the program")


# start the switch
def switcher(case):
    return{
        "bubble": bubble,
        "rbubble": reverse_bubble,
        "selection": selection,
        "rselection": reverse_selection,
        "merge": merge,
        "rmerge": reverse_merge,
        "insertion": insertion,
        "rinsertion": reverse_insertion,
        "help": help,
        "exit": stop,
        "stop": stop,
        "quit": stop,
    }.get(case, f_default)


# print the result of the sort
while True:
    # get type of sort
    switching = input("What type of sort would you like ? (help) \n")
    print(switcher(switching)(text))
