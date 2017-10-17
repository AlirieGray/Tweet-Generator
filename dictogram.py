from histogram import Histogram
import util
import re
import random
from datetime import datetime
from queue import Queue

# TODO: increase probability of end-sentence token the longer the
#   generated sentence grows

class Dictogram(dict):
    def __init__(self, source_text_file, order):
        if source_text_file:
            # first, read in the file and normalize the string
            list_of_words = util.read_in_file(source_text_file)
            normal_list = util.normalized_list(list_of_words)
            Q = Queue()

            for i in range(0, order):
                Q.enqueue(normal_list[i])
            for j in range(order, len(normal_list)):
                tupleKey = Q.toTuple()
                Q.dequeue()
                next_word = normal_list[j]
                Q.enqueue(next_word)

                # add the new word to the histogram
                if not self.get(tupleKey):
                    self[tupleKey] = Histogram()
                self[tupleKey].add(next_word)

                # handle end of file
                if j == len(normal_list) - 1:
                    ls = []
                    for word in tupleKey[(1 - order):]:
                        ls.append(word)
                    ls.append(normal_list[j])
                    newKey = tuple(ls)
                    if not self.get(newKey):
                        self[newKey] = Histogram()
                    self[newKey].add("STOP")

    def generate_sentence(self, sentence_length=10):
        generated = []
        # randomly select start word and use it to determine the order
        # of the Markov chain
        # TODO: select only from words following start tokens
        start_word = random.choice(list(self.keys()))
        order = len(start_word)

        generated.append(" ".join(start_word))
        current = start_word

        while len(generated) < sentence_length:
            # if first order, we can just use the one-item tuple itself
            # as the state to look up the next word
            if order == 1:
                new_word = self.next_word(current)
                current = new_word
                if new_word == "STOP":
                    return " ".join(generated)
            # for a higher-order Markov chain, we have to determine the
            # new state using the old state and the word we just generated
            else:
                new_state = []
                for word in current[(1 - order):]:
                    new_state.append(word)
                new_word = self.next_word(current)
                if new_word[0] == "STOP":
                    return " ".join(generated)
                new_state.append(new_word[0])
                current = tuple(new_state)
            generated.append(" ".join(new_word))

        return " ".join(generated)

    def next_word(self, wordTuple):
        prev = 0
        running_total = 0
        random_integer = random.randint(1, self[wordTuple].tokens)

        for pair in self[wordTuple]:
            nextWord = pair[0]
            prob = pair[1]
            running_total += prob
            if random_integer > prev and random_integer <= running_total:
                return (nextWord,)

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
    # fish = Dictogram('fish.txt', 1)
    # fish.print_self()
    # print(fish.generate_sentence())


    mx = Dictogram('corpus.txt', 1)
    print(mx.generate_sentence())



    #
