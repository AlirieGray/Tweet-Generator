from histogram import Histogram
import util
import re
import random
from datetime import datetime
from queue import Queue

# TODO: increase probability of end-sentence token the longer the
#   generated sentence grows
# TODO: histogram in SecondOrderDictogram value is now a LISTogram,
#   treat it accordingly !

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
    def __init__(self, source_text_file=None, order=2):
        if source_text_file:
            # first, read in the file and normalize the string
            list_of_words = util.read_in_file(source_text_file)
            normal_list = util.normalized_list(list_of_words)

            Q = Queue()
            first = ""
            if order == 1:
                for item in normal_list:
                    Q.enqueue(item)

                    if Q.length() > 1:
                        current = Q.dequeue()
                        if not self.get(current):
                            self[current] = Histogram()
                        self[current].add(Q.peek())


            elif order == 2:
                for item in normal_list:
                    Q.enqueue(item)

                    if Q.length() > 2:
                        if first == "":
                            first = Q.dequeue()
                        else:
                            first = second
                        second = Q.dequeue()
                        window = (first, second)

                        if not self.get(window):
                            self[window] = Histogram()
                        self[window].add(Q.peek())

    def print_self(self):
        for key, value in self.items():
            print(key)
            print(value)

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

    def next_word(self, word):
        prev = 0
        running_total = 0
        random_integer = random.randint(1, self[word].tokens)

        for pair in self[word]:
            nextWord = pair[0]
            prob = pair[1]
            running_total += prob
            if random_integer > prev and random_integer <= running_total:
                return nextWord
            prev = running_total


if __name__ == '__main__':
    # start = datetime.now()
    # blue = Dictogram('blue.txt')
    # print("Time to create Dictogram: " + str(datetime.now() - start))
    # print(blue.generate_sentence(10))
    # start = datetime.now()
    # print("Time to generate 10-word sentence: " + str(datetime.now() - start))


    # test fist-order Markov chain
    # fish = Dictogram('fish.txt', 1)
    # fish.print_self()
    # print(fish.generate_sentence())

    blue = Dictogram('blue.txt', 1)

    print(blue.generate_sentence())



    #
