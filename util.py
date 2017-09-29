import sys
import re
import histogram
import random
from operator import itemgetter
from datetime import datetime

#### UTILIY FUNCTIONS ####
## TODO: deal with empty strings in normalized string

# takes in a file name and returns a list of all words in the file
def read_in_file(filename): # TODO can normalize string in this function
    words = []
    with open(filename) as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words

# takes a list of strings and returns it as a
# lower-case string with digits and special characters removed
def normalize(text):
    return_string = ' '.join(text)
    return_string = re.sub(r'[0-9]+', '', return_string)
    return_string = re.sub(r'[\]]+', '', return_string)
    return_string = re.sub(r'[\[]+', '', return_string)
    return_string = re.sub(r'[\(]+', '', return_string)
    return_string = re.sub(r'[\)]+', '', return_string)
    return_string = re.sub(r'[*]+', '', return_string)
    return_string = re.sub(r'[\']+', ' ', return_string)
    return_string = re.sub(r'[_*]+', '', return_string)
    return_string = re.sub(r'[\"]+', '', return_string)
    return_string = re.sub(r'[,]+', '', return_string)
    #return_string = re.sub(r'[.]+', '', return_string)
    return_string = re.sub(r'[;]+', '', return_string)
    return_string = re.sub(r'[?]+', '', return_string)
    return return_string.lower()

def normalized_list(text):
    return_string = ' '.join(text)
    return_string = re.sub(r'[0-9]+', '', return_string)
    return_string = re.sub(r'[\]]+', '', return_string)
    return_string = re.sub(r'[\[]+', '', return_string)
    return_string = re.sub(r'[\(]+', '', return_string)
    return_string = re.sub(r'[\)]+', '', return_string)
    return_string = re.sub(r'[*]+', '', return_string)
    return_string = re.sub(r'[\']+', ' ', return_string)
    return_string = re.sub(r'[_*]+', '', return_string)
    return_string = re.sub(r'[\"]+', '', return_string)
    return_string = re.sub(r'[,]+', '', return_string)
    #return_string = re.sub(r'[.]+', '', return_string)
    return_string = re.sub(r'[;]+', '', return_string)
    return_string = re.sub(r'[?]+', '', return_string)
    return return_string.lower().split(' ')

# take in a histogram in dictionary format and writes a new file with each
# word and its frequency on a new line
def write_histogram_file(hist, new_file):
    with open(new_file, 'w') as f:
        for key in hist.probability_dictionary.keys():
            f.write("%s %d \n" % (key, hist.probability_dictionary[key]))

# takes in a probability dictionary and returns a structure
# in which every item is a list with two elements:
# first a word, and then a list with the start and end numbers of
# that word's "range" on the number line, based on its probability
def create_ranges_list(prob_dict):
    return_list = []
    current = 0
    for word in prob_dict:
        range_list = []
        # calculate the beginning and end of each word's probability range
        range_list.append(current)
        current += prob_dict[word]
        range_list.append(current)
        # add a sublist with the word and its probability range
        return_list.append([word, range_list])
    return return_list

# takes in a list of words and its associated probability range and returns
# a random word from the list, weighted by probability
def random_weighted(probs_dict):
    # get a random float between 0 and 1
    random_prob = random.random()
    for pair in probs_dict:
        prob_range = pair[1]
        # iterate through the probability dictionary until we reach a word
        # whose probability range contains the randomly generated float
        # and then return that word
        if random_prob >= prob_range[0] and random_prob < prob_range[1]:
            return pair[0]
