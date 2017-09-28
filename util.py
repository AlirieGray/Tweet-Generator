import sys
import re

#### UTILIY FUNCTIONS ####

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
