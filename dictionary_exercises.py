# dictionary_exercises.py - this prgm answers the dictionary exercises for
#                           DC's day 5 development prgm
#
# jf - 4/19


##################
### Exercise 1 ###
##################


def main_1():
    # solves problem 1

    phonebook_dict = {
        'Alice' : '703-493-1834',
        'Bob' : '857-384-1234',
        'Elizabeth' : '484-584-2923'
    }

    # problem 1
    print(phonebook_dict['Elizabeth'])
    
    # problem 2
    phonebook_dict['Kareem'] = '938-489-1234'
    
    # problem 3
    del phonebook_dict['Alice']

    # problem 4
    phonebook_dict['Bob'] = '968-345-2345'

    # problem 5
    for person in phonebook_dict:
        print(phonebook_dict[person])


##################
### Exercise 2 ###
##################


def main_2():
    # solves problem 2

    ramit = {
        'name' : 'Ramit',
        'email' : 'ramit@gmail.com',
        'interests' : ['movies', 'tennis'],
        'friends' : [
            {
                'name' : 'Jasmine',
                'email': 'jasmine@yahoo.com',
                'interests' : ['photography', 'tennis']
            },
            {
                'name' : 'Jan',
                'email' : 'jan@hotmail.com',
                'interests' : ['movies', 'tv']
            }
        ]
    }

    # problem 1
    ramit_email = ramit['email']
    print(ramit_email)

    # problem 2
    ramit_first_interest = ramit['interests'][0]
    print(ramit_first_interest)

    # problem 3
    jasmine_email = ramit['friends'][0]['email']
    print(jasmine_email)

    # problem 4
    jan_second_interest = ramit['friends'][1]['interests'][1]
    print(jan_second_interest)


######################
### Letter Summary ###
######################


def letter_summary(str):
    '''
    param:
        str -> String
    return:
        alpha_dict -> Dict
    '''

    d = dict()

    # loop over the letters in the input string
    for letter in str:

        # check to see if it's in the count dictionary
        if letter in d:

            # if it is, then bump up its count
            d[letter] += 1

        else:

            # otherwise, initialize it 
            d[letter] = 1

    return d
    
def main_3():
    # main function associated with Letter Summary problem

    input_word = input("Please enter a word: ")

    print(letter_summary(input_word))


####################
### Word Summary ###
####################


def word_summary(str):
    '''
    param:
        str -> String
    return:
        word_dict -> Dict
    '''

    # create a list of words from the input string, having lowercased them
    words = str.lower().split()

    # init a dict to store the words & counts as key, value pairs
    word_dict = dict()

    # loop over the words in the list of words
    for word in words:

        # check if the word is in the dictionary
        if word in word_dict:

            # if it is, bump up the count
            word_dict[word] += 1
        else:

            # otherwise, initialize it
            word_dict[word] = 1

    return word_dict

def main_4():
    # main function associated with Word Summary problem

    input_sentence = input("Please enter a sentence: ")

    print(word_summary(input_sentence))


#######################
### Bonus Challenge ###
#######################


def bonus_challenge(dict):
    '''
    param:
        dict -> Dict
    return:
        None
    '''

    # get the keys & their associated values
    key_value_pairs = dict.items()

    # sort them by their key, which is the second item in each of the tuples.
    # pass in reverse as True, since by default the sort is in ascending order.
    # THEN, get the first 3 values, which represent the top 3 largest counts.
    sorted_by_count = sorted(key_value_pairs, key = lambda x: x[1], reverse = True)[:3]

    # next, iterate over said values and print them out as required
    for item in sorted_by_count:
        print(item[0] + ":", item[1])


def main_5():
    # main function associated with Bonus Challenge problem

    sentence = input("Enter a sentence: ")

    bonus_challenge(word_summary(sentence))


# to be run as script
if __name__ == '__main__':
    # main_1()
    # main_2()
    # main_3()
    # main_4()
    main_5()