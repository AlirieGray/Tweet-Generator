import histogram
import random
import operator
from datetime import datetime

# takes in a histogram and returns a random word from it
def random_word(hist):
    return random.choice(list(hist.keys()))

# returns a random word from the histogram, weighted by frequency
def random_weighted_one(hist):
    # first take a random sample of key/value pairs
    # and add them to a list
    words = []
    for i in range (3):
        new_word = random_word(hist)
        words.append(new_word)

    # whichever has the highest frequency/probability in the histogram
    # (may be a tie) return that word
    current = 0
    max_word = ""
    '''
    for word in words:
        if histogram.frequency(word, hist) > current:
            current = histogram.frequency(word, hist)
            max_word = word
    '''
    # alternatively
    probs = probability_dictionary(hist)
    for word in words:
        if probs[word] > current:
            current = probs[word]
            max_word = word
    return max_word

def random_weighted_two(hist):
    pass


# takes in a histogram dictionary and returns a dictionary in which
# the key is the word and the value is its probability in the text
def probability_dictionary(hist):
    # total words in source text (add up all frequencies)
    total = 0
    return_dict = dict()
    for freq in hist.values():
        total += freq
    for word in hist.keys():
        return_dict[word] = hist[word] / total
    return return_dict

# run random_weighted many times and keep track of which word is returned
def testing(hist):
    reps = 1000
    start = datetime.now()
    probs = probability_dictionary(hist)
    print(probs)

    # testing method two
    output = []
    for i in range (reps):
        output.append(random_weighted_two(hist))
    new_hist = histogram.create_dict(" ".join(output))
    print(new_hist)

    # print the frequency of the word being output by the function
    # and the frequency of the word in the source text
    # for word in new_hist.keys():
    #    print("Word: " + word + "     Frequency output: " + str(new_hist[word] / 1000) + "      Original frequency: " + str(hist[word] / histogram.unique_words(hist)))
    # print(new_hist)

    # sort new histogram and original histogram by vales and compare

    # print("Original: ")
    # original_hist = (sorted(hist.items(), key=operator.itemgetter(1), reverse=True))
    # print("New: ")
    # words_generated_histogram = (sorted(new_hist.items(), key=operator.itemgetter(1), reverse=True))
    for word in new_hist.keys():
        print(word)
        print("Generated: " + str(new_hist[word] / reps))
        print("Original:  " + str(probs[word]))
        print()
    print("Time: " + str(datetime.now() - start))

if __name__ == '__main__':
    normalized_string = (histogram.normalize(histogram.read_in_file('fish.txt')))
    fish_words = histogram.create_dict(normalized_string)
    testing(fish_words)
