
def getDividers(value):
    """Gets a list of integer dividers of number value

    Args:
        value: number to get dividers.

    Returns:
        bool: is perfect (True) or not (False)
    """


    # create an empty list
    dividers = []

    for i in range(1,value):
        if value%i == 0: # its an integer divider
            dividers.append(i) # add this divider to the list of dividers

    return dividers

def isPerfect(value):

    dividers = getDividers(value)

    return value == sum(dividers)

