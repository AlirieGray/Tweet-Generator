import histogram
import random
from operator import itemgetter
from datetime import datetime

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
