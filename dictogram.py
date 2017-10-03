from histogram import Histogram
import util
import re
import random
from datetime import datetime

## current issues: gets stuck in loop, repeats sentences directly from source ##

class Dictogram(dict):
    def __init__(self, source_text_file=None):
        self.start_words = []
        self.end_words = []
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if source_text_file:
            # first, read in the file and normalize the string
            list_of_words = util.read_in_file(source_text_file)
            normal_list = util.normalized_list(list_of_words)
            dictogram = dict()

            # loop through every word in the source text, storing its index as i
            for i, word in enumerate(normal_list):
                # if the word hasn't been added to the dictogram yet, then add it
                # as a key, and make its value an empty histogram
                if word not in dictogram:
                    dictogram[word] = Histogram()
                if (i < len(normal_list) - 1):
                    if word.endswith(".") and word not in self.end_words:
                        #word = re.sub(r'[.]+', '', word)
                        self.end_words.append(word)
                        self.start_words.append(normal_list[i + 1])
                    # if the word that occurs after the current word in the list
                    # is not already in the dictogram under the current word's
                    # histogram, then add it to the current word's histrogram
                    # and make its value 1
                    if normal_list[i + 1] not in dictogram[word].keys():
                        dictogram[word][normal_list[i + 1]] = 1
                        # otherwise, increment its value in the current word's histogram
                    else:
                        dictogram[word][normal_list[i + 1]] += 1
            return_ranges = dict()
            for key, value in dictogram.items():
                self[key] = util.create_ranges_list(value)

    def print_self():
        for key, value in self.items():
            print(key)
            print(list(value.keys()))

    def generate_sentence(self, sentence_length):
        # pick a random start word
        generated = []
        start = ''
        while start == '':
            start = random.choice(self.start_words)
        current_word = start
        generated.append(start)
        while (len(generated) < sentence_length):
            # randomly pick a word from the words that follow the current word
            next_word = ''
            while next_word == '':
                next_word = util.random_weighted(self[current_word])
            generated.append(next_word)
            current_word = next_word
            #if next_word in self.end_words:
            #    break
        return(" ".join(generated))

if __name__ == '__main__':
    start = datetime.now()
    blue = Dictogram('blue.txt')
    print("Time to create Dictogram: " + str(datetime.now() - start))
    print(blue.generate_sentence(10))
    start = datetime.now()
    print("Time to generate 10-word sentence: " + str(datetime.now() - start))
