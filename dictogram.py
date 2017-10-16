from histogram import Histogram
import util
import re
import random
from datetime import datetime
from queue import Queue

# TODO: increase probability of end-sentence token the longer the
#   generated sentence grows

"""
class Dictogram(dict):
    def __init__(self, source_text_file=None):
        self.start_words = []
        self.end_words = []

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
                    # instead of this:
                    # put a [START] and [STOP] token in the normalized list itself
                    # and then when we get stop, we can just break
                    # and we'll have a chance of not ending even if we get a word
                    # that sometimes ends a sentence, if it also sometimes doesn't
                    # end a sentence
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

    def print_self(self):
        for key, value in self.items():
            print(key)
            print(value)

    def generate_sentence(self, sentence_length):
        # pick a random start word
        generated = []
        start = ''
        while start == '':
            start = random.choice(self.start_words)
        current_word = start
        generated.append(start.title())
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
"""

class Dictogram(dict):
    def __init__(self, source_text_file, order):
        if source_text_file:
            # first, read in the file and normalize the string
            list_of_words = util.read_in_file(source_text_file)
            normal_list = util.normalized_list(list_of_words)
            Q = Queue()

            for i in range(0, order):
                Q.enqueue(normal_list[i])
            for j in range(order, len(normal_list) - 1):
                tupleKey = Q.toTuple()
                Q.dequeue()
                next_word = normal_list[j]
                Q.enqueue(next_word)

                # add the new word to the histogram
                if not self.get(tupleKey):
                    self[tupleKey] = Histogram()
                self[tupleKey].add(next_word)

    def generate_sentence(self, sentence_length=10):
        generated = []
        # randomly select start word
        start_word = random.choice(list(self.keys()))
        # TODO: select only from words following start tokens
        generated.append(start_word)
        current = start_word
        while len(generated) < sentence_length:
            new_word = self.next_word(current)
            generated.append(new_word)
            current = new_word
        return " ".join(generated)

    def next_word(self, wordTuple):
        order = len(wordTuple)
        prev = 0
        running_total = 0
        random_integer = random.randint(1, self[wordTuple].tokens)

        for pair in self[wordTuple]:
            nextWord = pair[0]
            prob = pair[1]
            running_total += prob
            if random_integer > prev and random_integer <= running_total:
                # if first order, then we can just look up the next word
                # based on only the word selected
                if order == 1:
                    return (nextWord,)
                # otherwise, create a tuple based on the state

            prev = running_total

    def print_self(self):
        for key, value in self.items():
            print(key)
            print(value)


if __name__ == '__main__':
    # start = datetime.now()
    # blue = Dictogram('blue.txt')
    # print("Time to create Dictogram: " + str(datetime.now() - start))
    # print(blue.generate_sentence(10))
    # start = datetime.now()
    # print("Time to generate 10-word sentence: " + str(datetime.now() - start))


    # test fist-order Markov chain
    fish = Dictogram('fish.txt', 1)
    fish.print_self()
    print(fish.generate_sentence())

    #blue = Dictogram('blue.txt', 1)

    #print(blue.generate_sentence())



    #
