import sys
import re
from datetime import datetime
from operator import itemgetter

class Histogram(dict):
    # takes in a source text in string format and returns a dictionary
    # in which each key is a unique word and its value is that word's
    # probability of occurring in the source text
    def __init__(self, source_text_string=None):
        if source_text_string:
            words_list = source_text_string.split(' ')
            total = len(words_list)
            for word in words_list:
                # if the word has not been added to the dictionary yet, add it
                # otherwise, increment its value (frequency)
                if word not in self:
                    self[word] = (1 / total)
                else:
                    self[word] += (1 / total)

    # returns the probability of a given word in the histogram
    def probability(word):
        all_words = list(map(itemgetter(0), self))
        i = all_words.index(word)
        return self[i][1]

    def add(word):
        if word not in self:
            self[word] = 1
        else:
            self[word] += 1

if __name__ == '__main__':
    # calculate time to create a histogram
    start = datetime.now()
    test_hist = Histogram('blue.txt')
    print("Time: " + str(datetime.now() - start))
