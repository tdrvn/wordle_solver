from functools import total_ordering
import re
from collections import Counter
import constants
import requests

def getInitWords():
    '''
        Returns all 5 letter words from words.txt.
    '''
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()

    return words

def getFrequencies(word_list):
    '''
        Given a word_list, returns all letter frequencies and letter frequencies per position.
    '''
    freq = []
    for i in range(constants.STRING_LENGTH):
        freq.append(Counter())
    total_freq = Counter()
    for word in word_list:
        for i in range(constants.STRING_LENGTH):
            freq[i].update(word[i])
            total_freq.update(word[i])
    return (total_freq, freq)


