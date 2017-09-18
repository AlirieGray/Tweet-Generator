import sys
import re
from datetime import datetime

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

# takes in a source text in string format and returns a list of tuples
# in which the first element in each tuple is the word and the second
# element is its frequency in the source texts
def create_list(source_text):
    word_frequencies = []
    for word in source_text.split(' '):
        pass

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
    return_string = re.sub(r'[,]+', ' ', return_string)
    return_string = re.sub(r'[.]+', ' ', return_string)
    return_string = re.sub(r'[;]+', ' ', return_string)
    return_string = re.sub(r'[?]+', ' ', return_string)
    return return_string.lower()

# returns the number of unique words in the histogram
def unique_words(histogram):
    return len(histogram)

# returns the frequency of a given word in the histogram
def frequency(word, histogram):
    if(type(histogram) is dict):
        return histogram[word]
    elif(type(histogram) is list):
        pass

def write_histogram_file(hist, new_file):
    with open(new_file, 'w') as f:
        for key in hist.keys():
            f.write("%s %d \n" % (key, hist[key]))

if __name__ == '__main__':
    # testing
    start = datetime.now()
    words = read_in_file('freud.txt')
    words = normalize(words)
    histogram = (create_dict(words)) # a dictionary of word: frequency
    write_histogram_file(histogram, 'freud_histogram.txt')
    print("Time: " + str(datetime.now() - start))
    '''
    print(histogram)
    print("Unique words: " + str(unique_words(histogram)))
    print("The: " + str(frequency("the", histogram)))
    print("Pathological: " + str(frequency("pathological", histogram)))
    print("Adhesion : " + str(frequency("adhesion", histogram)))
    print("Attention : " + str(frequency("attention", histogram)))
    print("Himself : " + str(frequency("himself", histogram)))
    print("Repressed : " + str(frequency("repressed", histogram)))
    '''
