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
        # add beginning of the range to the ranges sublist
        range_list.append(current)
        # add the probability of the current word to get the end of the range
        current += prob_dict[word]
        # then add the end of the range as the second element in the ranges sublist
        range_list.append(current)
        # add a sublist with the word and its probability range
        return_list.append([word, range_list])
    return return_list

# takes in a list of words and its associated probability range and returns
# a random word from the list, weighted by probability
def random_weighted(probs_dict):
    random_probability = random.random()
    #TODO explain loop
    for pair in probs_dict: # TODO variable for pair[1]
        if random_probability >= pair[1][0] and random_probability < pair[1][1]:
            return pair[0]

# run random_weighted many times and keep track of which word is returned
def testing(hist):
    reps = 1000
    start = datetime.now()
    output = []
    for i in range (reps):
        output.append(random_weighted(hist))
    new_hist = histogram.create_dict(" ".join(output))
    print(new_hist)
    print("Time: " + str(datetime.now() - start))


if __name__ == '__main__':
    normalized_string = (histogram.normalize(histogram.read_in_file('fish.txt')))
    fish_words = histogram.create_dict(normalized_string)
    #print(fish_words)
    fish_probs = create_ranges_list(fish_words)
    print(fish_probs)
    testing(fish_probs)
