import sys
import re
from datetime import datetime
from operator import itemgetter

# takes in a file name and returns a list of all words in the file
def read_in_file(filename):
    words = []
    with open(filename) as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words

# takes in a source text in string format and returns a dictionary
# in which each key is a unique word and its value is that word's
# probability of occurring in the source text
def create_dict(source_text):
    word_frequencies = dict()
    words_list = source_text.split(' ')
    total = len(words_list)
    for word in words_list:
        # if the word has not been added to the dictionary yet, add it
        # otherwise, increment its value (frequency)
        if word not in word_frequencies:
            word_frequencies[word] = (1 / total)
        else:
            word_frequencies[word] += (1 / total)
    return word_frequencies

# takes a list of string and returns it as a
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
    return_string = re.sub(r'[.]+', '', return_string)
    return_string = re.sub(r'[;]+', '', return_string)
    return_string = re.sub(r'[?]+', '', return_string)
    return return_string.lower()

# returns the number of unique words in the histogram
def unique_words(histogram):
    return len(histogram)

# returns the probability of a given word in the histogram
def probability(word, histogram):
    if(type(histogram) is dict):
        return histogram[word]
    elif(type(histogram) is list):
        all_words = list(map(itemgetter(0), histogram))
        i = all_words.index(word)
        return histogram[i][1]

# take in a histogram in dictionary format and writes a new file with each
# word and its frequency on a new line
def write_histogram_file(hist, new_file):
    with open(new_file, 'w') as f:
        for key in hist.keys():
            f.write("%s %d \n" % (key, hist[key]))

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
