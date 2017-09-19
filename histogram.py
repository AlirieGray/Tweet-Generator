import sys
import re
from datetime import datetime
from operator import itemgetter

# takes in a file name and returns a list of all words in the file
def read_in_file(filename):
    words = []
    with open('freud.txt') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words

# takes in a source text in string format and returns a dictionary
# in which each key is a unique word and its value is that word's
# frequency in the source text
def create_dict(source_text):
    word_frequencies = dict()
    for word in source_text.split(' '):
        # if the word has not been added to the dictionary yet, add it
        # otherwise, increment its value (frequency)
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    return word_frequencies

# takes in a source text in string format and returns a list of lists
# in which the first element in each sublist is the word and the second
# element is its frequency in the source texts
def create_list(source_text):
    source = source_text.split(' ')
    word_frequencies = []
    unique = []

    for word in source:
        if word not in unique:
            word_frequencies.append([word, 1])
            unique.append(word)
        else:
            # get list of all first indexes (words)
            # find the index of the word in that list
            # it will also be the word's index in word_frequencies
            all_words = list(map(itemgetter(0), word_frequencies))
            i = all_words.index(word)
            word_frequencies[i][1] += 1
    return(word_frequencies)

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
    return_string = re.sub(r'[-]+', ' ', return_string)
    return_string = re.sub(r'[_]+', '', return_string)
    return_string = re.sub(r'[\"]+', '', return_string)
    return_string = re.sub(r'[,]+', '', return_string)
    return_string = re.sub(r'[.]+', '', return_string)
    return_string = re.sub(r'[;]+', '', return_string)
    return_string = re.sub(r'[?]+', '', return_string)
    return return_string.lower()

# returns the number of unique words in the histogram
def unique_words(histogram):
    return len(histogram)

# returns the frequency of a given word in the histogram
def frequency(word, histogram):
    if(type(histogram) is dict):
        return histogram[word]
    elif(type(histogram) is list):
        all_words = list(map(itemgetter(0), histogram))
        i = all_words.index(word)
        return histogram[i][1]

def write_histogram_file(hist, new_file):
    with open(new_file, 'w') as f:
        for key in hist.keys():
            f.write("%s %d \n" % (key, hist[key]))

if __name__ == '__main__':
    words = read_in_file('freud.txt')
    words = normalize(words)

    # testing
    start = datetime.now()
    histogram_dict = (create_dict(words)) # a dictionary of word: frequency
    print("Time to create dictionary: " + str(datetime.now() - start))
    start = datetime.now()
    print("The: " + str(frequency("the", histogram_dict)))
    print("Time to find frequency of word in dictionary: " + str(datetime.now() - start))

    start = datetime.now()
    histogram_list = (create_list(words)) # a dictionary of word: frequency
    print("Time to create list: " + str(datetime.now() - start))
    start = datetime.now()
    print("The: " + str(frequency("the", histogram_list)))
    print("Time to find frequency of word in list: " + str(datetime.now() - start))


    #write_histogram_file(histogram, 'freud_histogram.txt')
    '''
    print(histogram_dict)
    print("Unique words: " + str(unique_words(histogram)))
    print("The: " + str(frequency("the", histogram)))
    print("Pathological: " + str(frequency("pathological", histogram)))
    print("Adhesion : " + str(frequency("adhesion", histogram)))
    print("Attention : " + str(frequency("attention", histogram)))
    print("Himself : " + str(frequency("himself", histogram)))
    print("Repressed : " + str(frequency("repressed", histogram)))
    '''
