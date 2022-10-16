from ast import Constant
from tokenize import String
import constants

def check_character(character):
    '''
        Checks if the character is valid.
    '''
    if character == '!':
        return constants.GREEN_COLOR
    elif character == '?':
        return constants.YELLOW_COLOR
    elif character == '_':
        return constants.GREY_COLOR
    else:
        return constants.INCORRECT

def get_response(word):
    '''
        Gets the used response for the word.

        TODO: Automate it directly with the website
        TODO 2: Testing tool
    '''
    print(f"Please input the results (only !/?/_) or the following word:\n{word} ")
    answer = [None] * 5
    while True:
        string = input()
        print(len(string))
        good = True
        if len(string) != constants.STRING_LENGTH: 
            good = False
        else:
            for i in range(constants.STRING_LENGTH):
                answer[i] = check_character(string[i])
                if answer[i] == 0:
                    good = False
        if good == False:
            print("Wrong format. Try again:")
        else:
            return answer


