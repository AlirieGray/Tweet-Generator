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
    for item in prob_dict:
        range_list = []
        range_list.append(current)
        current += prob_dict[item]
        range_list.append(current)
        return_list.append([item, range_list])
    return return_list

# takes in a list of words and its associated probability range and returns
# a random word from the list, weighted by probability
def random_weighted(probs_list):
    random_probability = random.random() # [0, 1)
    for pair in probs_list:
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
