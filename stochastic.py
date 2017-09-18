import histogram
import random
import operator
from datetime import datetime

freud_words = histogram.create_dict(histogram.normalize(histogram.read_in_file('freud.txt')))

# takes in a histogram and returns a random word from it
def random_word(hist):
    return random.choice(list(hist.keys()))

# returns a random word from the histogram, weighted by frequency
def random_weighted(hist):
    # first take a random sample of key/value pairs
    # and add them to a list
    words = []
    for i in range (200):
        new_word = random_word(hist)
        words.append(new_word)

    # whichever has the highest frequency in the histogram
    # (may be a tie) return that word
    current = 0
    max_word = ""
    for word in words:
        if histogram.frequency(word, hist) > current:
            current = histogram.frequency(word, hist)
            max_word = word
    return max_word

# run random_weighted many times and keep track of which word is returned
def testing(hist):
    start = datetime.now()

    output = ""
    for i in range (1000):
        output += random_weighted(hist) + " "
    new_hist = histogram.create_dict(output)

    # print the frequency of the word being output by the function
    # and the frequency of the word in the source text
    #for word in new_hist.keys():
    #    print("Word: " + word + "     Frequency output: " + str(new_hist[word] / 1000) + "      Original frequency: " + str(hist[word] / histogram.unique_words(hist)))
    #print(new_hist)

    # sort new histogram and original histogram by vales and compare

    print("Original: ")
    print(sorted(hist.items(), key=operator.itemgetter(1), reverse=True))
    print("New: ")
    print(sorted(new_hist.items(), key=operator.itemgetter(1), reverse=True))
    print("Time: " + str(datetime.now() - start))


if __name__ == '__main__':
    #print(random_word(freud_words))
    testing(freud_words)
    # print(random_weighted(freud_words))
