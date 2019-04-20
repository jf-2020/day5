# intro_to_algorithms.py - this prgm is was a group exercise, though it was completed
#                          in full by jf. the problems are intoductory algorithm questions
#                          wherein builtins are to be largerly avoided in their solution.
#
# 4/20 - jf


###########################
### Single Letter Count ###
###########################


def single_letter_count(word, letter):
    '''
    parameters:
        word    -> String
        letter  -> String
    return:
        count   -> Int
    '''

    # Assumption: case doesn't matter
    
    # initialize a variable to keep track of how many times the letter
    # is encounted in the search word
    count = 0

    # loop over the letters in the lowercased search word
    for char in word.lower():

        # check to see if the current character is the letter we're looking
        # for
        if char == letter:

            # if it is, then we'll bump up th count
            count += 1

        # otherwise, continue with the next character

    return count

def main_0():
    # the main function associated with the Single Letter Count problem

    tests = [("Hello World", "h"),
             ("Hello World", "z"),
             ("Hello World", "l")]

    for test in tests:
        print("Calling single_letter_count(\'%s\', \'%s\')" % (test[0], test[1]))
        print("Returned: %d" % single_letter_count(*test), "\n")


#############################
### Multiple Letter Count ###
#############################


def multiple_letter_count(word):
    '''
    parameter:
        word        -> String
    return:
        counts_dict -> Dict
    '''

    # Assumption: case doesn't matter

    # first, setup an empty dictionary to use for the counts  
    counts_dict = dict()

    # traverse the given lowercased word, one character at a time
    for letter in word.lower():

        # check to see if the current letter is in the dictionary already
        if letter in counts_dict:

            # if it is, bump up it's count
            counts_dict[letter] += 1
        
        # otherwise, we need to initialize a key, value pair for it
        else:

            # setting its value to one, since it's the first time it has
            # been encountered
            counts_dict[letter] = 1

    return counts_dict

def count_vowels_only(word):
    '''
    parameter:
        word                -> String
    return:
        all_letters_count   -> Dict
    '''

    # Assumption: case doesn't matter

    # instead of mostly redoing the same problem again as found in the multiple
    # letter function definition above, i'll just re-use the code & remove any
    # key from the returned counts_dict that isn't a vowel.
    all_letters_counts = multiple_letter_count(word)

    # n.b. iterate over the word and not the count_dict because the object over
    # which the iteration is being performed cannot be edited while it's being
    # iterated over. therefore, it's necessary to check if the letter is both
    # not a vowel AND still in the count_dict.

    # look at each letter in the word
    for letter in word:

        # check to see if it's not a vowel & it's (still) in the count_dict
        if letter not in "aeiouy" and letter in all_letters_counts:

            # then remove it from the count_dict
            del all_letters_counts[letter]

    return all_letters_counts

def count_letters_in_sentence(word):
    '''
    parameter:
        word -> String
    return:
        Dict
    '''

    # Assumption: case doesn't matter

    # like the count vowels only problem, the code from the multiple letter function
    # will be reused. the only real difference here is that spaces must be ignored.

    # first, the word, being a sentence, is split into the words by spaces, thrown into
    # a list, and then the words in said list are joined together without spaces, with
    # the last step being a lowercase operation. the final result is simply a string
    # containing all the words of the input sentence with spaces removed.
    letters_in_sentence = ''.join(word.split()).lower()

    return multiple_letter_count(letters_in_sentence)

def main_1():
    # this function is the main function associated with the Multiple Letter
    # Count problem

    word_tests = ['string', 'doodad', 'aAbbbBBB', 'awesome', 'aeiouy']

    for test in word_tests:
        print("Testing string: \'%s\'" % test)
        print("Letter counts:", multiple_letter_count(test))
        print("Vowel counts:", count_vowels_only(test), '\n')

    # pangrams or holoalphabetic sentences
    sentences = ['The quick brown fox jumped over the lazy dog.',
                 'How vexingly quick daft zebras jump!',
                 'The five boxing wizards jump quickly.',
                 'Pack my box with five dozen liquor jugs.'
                 ]

    for sentence in sentences:
        print("Testing sentence: \'%s\'" % sentence)
        print("Letter counts:", count_letters_in_sentence(sentence), '\n')


#########################
### Jewels and Stones ###
#########################


def jewels_and_stones(jewels, stones):
    '''
    parameters:
        jewels  -> String
        stones  -> String
    return:
        count   -> Int
    '''

    # this problem requires that for each stone, a character, it must be 
    # checked as to whether or not it is a jewel, a character.

    count = 0

    # iterate over the stones
    for stone in stones:

        # check to see whether or not it's a jewel
        if stone in jewels:

            # if it is, then bump up the count
            count += 1

        # otherwise, it's not a jewel and continue
    
    return count

def main_2():
    # this the main function associated with the Jewels and Stones problem

    tests = [('aA', 'aAAbbbb'), ('ahBut', 'aAhHHHubT')]

    for test in tests:
        print("Testing -> Stones: %s & Jewels: %s" % (test[1], test[0]))
        print("Number of Jewels in Stones:", jewels_and_stones(*test))


##########################
### Palindromic String ###
##########################


def is_palindrome(word):
    '''
    parameter:
        word -> String
    return:
        Boolean
    '''

    # Assumptions: case matters, one character strings & empty strings are palindromes
    
    # n.b. could easily do this in one line:
    #
    #       return word == word[::-1]
    #
    # but constrained to think about this without convenient builtins as such

    # there's really only two cases to consider here, (i) the number of characters
    # in word is even & (ii) the number of characters in word is odd. it turns out
    # this covers the edge cases wherein the number of characters in word is 1 OR
    # the word is the empty string.

    # a two pointer method will be used as discussed in class. more specifically,
    # one pointer will begin "pointing" at the first letter in the word, moving
    # forwards in the string as the algorithm progresses, and the other pointer
    # will begin "pointing" at the last letter in the word, moving backwards in the
    # string as the algorithm progresses. the alogrithm will halt when these two
    # points cross one another in their relative positions in the word.

    # initialize the forward pointer
    forward_pointer = 0

    # initialize the backward pointer
    backward_pointer = len(word) - 1

    # loop over the letters in the word until until the two pointers cross
    while backward_pointer > forward_pointer:

        # check to make sure the word up to this point is palindromic
        if word[forward_pointer] == word[backward_pointer]:

            # if it is, bump up the forward pointer
            forward_pointer += 1

            # and decrease the backward pointer
            backward_pointer -= 1

            # and continue
            continue

        # otherwise, it's not palindromic and return False
        return False

    # if made it through entire word succcessfully, the it's indeed
    # palindromic, so return True
    return True

def main_3():
    # this is the main function associated with the Palindromic string problem

    tests = ['testing', 'tacocat', 'hannah', 'robert', 'amanaplanacanalpanama']

    for test in tests:
        print("Testing: %s" % test)
        print("Is palindrome? (T/F)", is_palindrome(test), '\n')


########################
### Frequency Search ###
########################


def frequency(source, target):
    '''
    parameters:
        source  -> List
        target  -> Type dependent
    return:
        count   -> Int
    '''

    # Assumption: target does not have type tuple, list or dict

    # initialize a variable to keep track of number of occurrences of target 
    # in source
    count = 0

    # iterate through the source
    for item in source:

        # check to see if the item has the same value as target
        if item == target:

            # if it does then bump up the count
            count += 1

        # otherwise current item in source doesn't have the same value as the
        # target, so continue

    return count

def main_4():
    # main function associated with the Frequency Search problem

    tests = [([1, 2, 3, 4, 4, 4], 4),
             ([True, False, True, True], False)
             ]

    for test in tests:
        print("Testing ->", test[1], "against", test[0])
        print("Number of occurrences: %d" % frequency(test[0], test[1]))


#############################
### Multiply Even Numbers ###
#############################


def multiply_even_numbers(numbers):
    '''
    parameter:
        numbers -> List
    return:
        product -> Integer
    '''

    # Assumption: the list of numbers isn't empty

    # while 0 is divisible by 2 (and, therefore, it's even), initialize
    # the resulting product to 1 by default, whereas an occurrence of a
    # 0 within the list of numbers will produce the required zero product
    product = 1

    # loop over the numbers in the list
    for number in numbers:

        # check to see if it's divisible by 2 (i.e. whethere or not it's
        # even)
        if number % 2 == 0:

            # if it is, then multiply it by the current value of product
            product *= number

        # otherwise, it's not even, so continue

    return product

def main_5():
    # main function associated with Multiply Even Numbers problem

    tests = [[2,3,4,5,6],
             [i for i in range(10)],
             [2,4,6,8,10]
             ]

    for test in tests:
        print("Testing:", test)
        print("Result: %d" % multiply_even_numbers(test), '\n')


##################
### Capitalize ###
##################

def capitalize(str):
    '''
    parameter:
        str -> String
    return:
        String or None
    '''

    # since builtins such as ord() & chr() can't be used (i.e. ascii conversions) a
    # "translate" dictionary will be used

    lowercase_to_uppercase = {
                                'a' : 'A',
                                'b' : 'B',
                                'c' : 'C',
                                'd' : 'D',
                                'e' : 'E',
                                'f' : 'F',
                                'g' : 'G',
                                'h' : 'H',
                                'i' : 'I',
                                'j' : 'J',
                                'k' : 'K',
                                'l' : 'L',
                                'm' : 'M',
                                'n' : 'N',
                                'o' : 'O',
                                'p' : 'P',
                                'q' : 'Q',
                                'r' : 'R',
                                's' : 'S',
                                't' : 'T',
                                'u' : 'U',
                                'v' : 'V',
                                'w' : 'W',
                                'x' : 'X',
                                'y' : 'Y',
                                'z' : 'Z'
                            }

    # check to see if it's not capitalized by seeing whether or not it's
    # in the translate dict
    if str[0] in lowercase_to_uppercase:

        # if it is then get uppercase from translate dict and prepend it
        # to the rest of the input string following the first character
        return lowercase_to_uppercase[str[0]] + str[1:]

    # otherwise, it's already capitalized, so just return it
    else:
        return str

def main_6():
    # main function associated with Capitalize problem

    tests = ['tim', 'matt', 'hello World!', 'Samson']

    for test in tests:
        print("Testing: %s" % test)
        print("Capitalized:", capitalize(test), '\n')


############################
### Sum of Odd Multiples ###
############################

def sum_odds_by_three_fives():
    '''
    parameter:
        None
    return:
        sum -> Int
    '''

    # Assumption: the numbers to be considered are strictly positive

    # initialize a variable to store the running sum and a loop counter
    sum, count = 0, 1

    # loop until 1000 is reached
    while count < 1000:

        # check to see if current number is divisble by 3 or 5
        if count % 3 == 0 or count % 5 == 0:

            # if it is, then increase the sum by that value
            sum += count

        # bump up the count
        count += 1

    return sum

def main_7():
    # main function associated with Sum of Odd Multiples problem

    print("The sum of all positive integers divisible by 3 or 5:", sum_odds_by_three_fives())


# to be run as script:
if __name__ == "__main__":
    # main_0()
    # main_1()
    # main_2()
    # main_3()
    # main_4()
    # main_5()
    # main_6()
    main_7()
