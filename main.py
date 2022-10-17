from cgi import test
from collections import Counter
import constants
import checker
import input
import word_operations
import string

def calculate_scoreKnuth(word, word_list):
    '''
        How many words it would eliminate worst case
    '''
    score = 0
    frv = {}
    for final in word_list:

        response = str(checker.get_response(word, final))
        
        frv[response] = frv.get(response, 0) + 1
    return len(word_list) - max(frv.values())


def main(testing = False):
    word_list = word_operations.getInitWords('answer_words.txt')
    total_words = word_list.copy()
    round = 1
    while round:
        if len(word_list) == 1:
            if testing == False:
                input.get_response(word_list[0])
                print(f"Finished in {round} rounds!")
            return round

        
        total_freq, freq = word_operations.getFrequencies(word_list)
        max_score = 0
        sel_word = "raise"
        if round > 1: 
            for word in total_words:
                score = calculate_scoreKnuth(word, word_list)
                if score > max_score:
                    max_score = score
                    sel_word = word
                elif score == max_score and word in word_list:
                    sel_word = word
        
        if testing == False:
            ans = input.get_response(sel_word)
        else:
            ans = checker.get_response(sel_word)

        filtered_wordlist = [word for word in word_list if checker.get_response(sel_word, word) == ans]
        word_list = filtered_wordlist

        if ans == [constants.GREEN_COLOR] * constants.STRING_LENGTH:
            if testing == False:
                print(f"Finished in {round} rounds!")
            return round
        
        if testing == False:
            print(filtered_wordlist)
            print(len(filtered_wordlist))
        round += 1

if __name__ == '__main__':
    main()
