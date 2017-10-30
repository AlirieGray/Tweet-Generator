import sys
import re
import random
from operator import itemgetter
from datetime import datetime

#### UTILIY FUNCTIONS ####
## TODO: deal with empty strings in normalized list

# takes in a file name and returns a list of all words in the file
def read_in_file(filename): # TODO can normalize string in this function (?)
    words = []
    with open(filename) as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words

def normalized_list(text):
    return_string = ' '.join(text).lower()
    #return_string = re.sub(r'[\]]+', '', return_string)
    #return_string = re.sub(r'[\[]+', '', return_string)
    return_string = re.sub(r'[\(]+', '', return_string)
    return_string = re.sub(r'[\)]+', '', return_string)
    return_string = re.sub(r'[*]+', '', return_string)
    return_string = re.sub(r'[\']+', ' ', return_string)
    return_string = re.sub(r'[_*]+', '', return_string)
    return_string = re.sub(r'[\"]+', '', return_string)
    return_string = re.sub(r'[\']+', '', return_string)
    return_string = re.sub(r'[.]+', ' [STOP]', return_string)
    return_string = re.sub(r'[?]+', ' [STOP]', return_string)
    return return_string.split(' ')

# take in a histogram in dictionary format and writes a new file with each
# word and its frequency on a new line
def write_histogram_file(hist, new_file):
    with open(new_file, 'w') as f:
        for key in hist:
            f.write("%s %d \n" % (key, hist[key]))
