import sys
import re
from datetime import datetime
from operator import itemgetter

class Histogram:
    # takes in a source text in string format and returns a dictionary
    # in which each key is a unique word and its value is that word's
    # probability of occurring in the source text
    def __init__(self, source_text_string=None):
        if source_text_string is None:
            self.probability_dictionary = dict()
        else:
            word_frequencies = dict()
            words_list = source_text_string.split(' ')
            total = len(words_list)
            for word in words_list:
                # if the word has not been added to the dictionary yet, add it
                # otherwise, increment its value (frequency)
                if word not in word_frequencies:
                    word_frequencies[word] = (1 / total)
                else:
                    word_frequencies[word] += (1 / total)
            self.probability_dictionary = word_frequencies

    # returns the number of unique words in the histogram
    def unique_words():
        return len(self.probability_dictionary)

    # returns the probability of a given word in the histogram
    def probability(word):
        all_words = list(map(itemgetter(0), self.probability_dictionary))
        i = all_words.index(word)
        return self.probability_dictionary[i][1]

    def add(word):
        if word not in self.probability_dictionary:
            self.probability_dictionary[word] = 1
        else:
            self.probability_dictionary[word] += 1


if __name__ == '__main__':
    words = read_in_file('fish.txt')
    words = normalize(words)
    # testing
    start = datetime.now()
    histogram_dict = (create_dict(words)) # a dictionary of word: frequency
    print("Time to create dictionary: " + str(datetime.now() - start))
    start = datetime.now()
    print("Fish: " + str(probability("fish", histogram_dict)))
    print("Time to find frequency of word in dictionary: " + str(datetime.now() - start))
    print(histogram_dict)
