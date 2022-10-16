from cgi import test
from collections import Counter
from pdb import post_mortem
import constants
import checker
import input
import word_operations
import string
import random

class Restrictions:

    pos_letters = []
    green_restrictions = {}
    yellow_restrictions = {}

    def __init__(self) -> None:

        self.pos_letters.clear()
        self.green_restrictions.clear()
        self.yellow_restrictions.clear()

        for i in range(constants.STRING_LENGTH):
            self.pos_letters.append({x for x in string.ascii_lowercase})


    def add_restriction(self, word, response):
        #green
        added_green = {}
        for i in range(constants.STRING_LENGTH):
            c = word[i]
            if response[i] == constants.GREEN_COLOR:
                self.green_restrictions[i] = c
                self.pos_letters[i].clear()
                self.pos_letters[i].add(c)
                added_green[i] = c
                if c in self.yellow_restrictions and i in self.yellow_restrictions[c]:
                    self.yellow_restrictions[c].clear()

        #yellow
        for i in range(constants.STRING_LENGTH):
            c = word[i]
            if response[i] == constants.YELLOW_COLOR:
                if c in self.green_restrictions.values():
                    if c not in added_green.values():
                        continue

                if c not in self.yellow_restrictions:
                    self.yellow_restrictions[c] = {x for x in range(constants.STRING_LENGTH) if x not in self.green_restrictions and c in self.pos_letters[x]}

                if c in self.yellow_restrictions:
                    if i in self.yellow_restrictions[c]:
                        self.yellow_restrictions[c].remove(i)
        
        #grey
        for i in range(constants.STRING_LENGTH):
            c = word[i]
            if response[i] == constants.GREY_COLOR:
                if c in self.pos_letters[i]:
                    self.pos_letters[i].remove(c)
                
                if c in self.yellow_restrictions:
                    #in yellow, can only delete this, as others were already checked or possible
                    if i in self.yellow_restrictions[c]:
                       self.yellow_restrictions[c].remove(i)
                else:
                    # not in yellow, can delete everything
                    for i2 in range(constants.STRING_LENGTH):
                        if self.green_restrictions.get(i2, 0) != c: 
                            if c in self.pos_letters[i2]:
                                self.pos_letters[i2].remove(c)

    
    def check_restriction(self, word):
        for i in range(constants.STRING_LENGTH):
            if word[i] not in self.pos_letters[i]:
                return False
        for letter, indices in self.yellow_restrictions.items():
            if len(indices) != 0:
                ok = False
                for i in indices:
                    if word[i] == letter:
                        ok = True
                if ok == False:
                    return False
        return True

def entropy(x):
    return x * ( 1 - x)

def calculate_scoreFreq(word, total_freq, pos_freq):
    '''
        Calculates the score of its entropy 
    '''
    score = 0 
    used_letter = set()
    for i in range(constants.STRING_LENGTH):
        c = word[i]
        cscore = entropy(pos_freq)
        score += cscore
    return score

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
    restrictions = Restrictions()
    word_list = word_operations.getInitWords()
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

        if ans == [constants.GREEN_COLOR] * constants.STRING_LENGTH:
            if testing == False:
                print(f"Finished in {round} rounds!")
            return round
        
        restrictions.add_restriction(sel_word, ans)
        if testing == False:
            print(restrictions.pos_letters)
            print(restrictions.green_restrictions)
            print(restrictions.yellow_restrictions)

        filtered_wordlist = [word for word in word_list if restrictions.check_restriction(word)]
        word_list = filtered_wordlist
        if testing == False:
            print(filtered_wordlist)
            print(len(filtered_wordlist))
        round += 1

if __name__ == '__main__':
    main()
