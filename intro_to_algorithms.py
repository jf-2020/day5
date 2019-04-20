# intro_to_algorithms.py - this prgm is a group exercises, completing the given
#                          introductory algorithms problems
#
# 4/19 - RJ, Angel, Jack


#############################
### Multiple Letter Count ###
#############################


def multiple_letter_count(str):
    '''
    param:
        str -> String
    return:
        ret_val -> Dict
    '''

    # assumption: ignore case

    # setup dictionary with all letters in given string 
    d = {letter: 0 for letter in str.lower()}

    # loop through the string
    for letter in str.lower():

        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    return d

def main_0():
    # this function is the main function associated with the Multiple Letter
    # Count problem

    tests = ['string', 'doodad', 'aAbbbBBB']

    for test in tests:
        print("Testing string:", test)
        print("Letter counts:", multiple_letter_count(test))


# to be run as script:
if __name__ == "__main__":
    main_0()