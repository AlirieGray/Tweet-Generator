from histogram import Histogram
import util
import random
from Queue import Queue

class Dictogram(dict):
    def __init__(self, source_text_file, order=1):
        self.order = order
        self.start_words = []
        if source_text_file:
            # first, read in the file and normalize the string
            list_of_words = util.read_in_file(source_text_file)
            normal_list = util.normalized_list(list_of_words)
            q = Queue()
            start_sentence = True

            # then loop through the remaining words
            for j in range(order, len(normal_list)):
                if q.length() != order:
                    q.enqueue(normal_list[j])
                    continue

                tuple_key = q.toTuple()

                if start_sentence:
                    start_sentence = False
                    self.start_words.append(tuple_key)

                q.dequeue()
                next_word = normal_list[j]

                q.enqueue(next_word)

                # add the new word to the histogram
                if not self.get(tuple_key):
                    self[tuple_key] = Histogram()
                self[tuple_key].add(next_word)

                if next_word == "[STOP]":
                    q = Queue()
                    start_sentence = True
                    continue

                # handle end of file
                if j == len(normal_list) - 1:
                    ls = []
                    for word in tuple_key[(1 - order):]:
                        ls.append(word)
                    ls.append(normal_list[j])
                    newKey = tuple(ls)
                    if not self.get(newKey):
                        self[newKey] = Histogram()
                    self[newKey].add("[STOP]")
                    return

    def generate_sentence(self, sentence_length=30):
        generated = []
        # randomly select start word and use it to determine the order
        # of the Markov chain
        order = self.order
        start_word = random.choice(self.start_words)

        generated.append(" ".join(start_word))
        current = start_word
        length_so_far = 0

        while len(generated) < sentence_length:
            # as the sentence grows longer, increase the probability of
            # the stop token appearing
            if length_so_far > 10:
                if self[current].__contains__("[STOP]"):
                    self[current].increment_frequency("[STOP]", 2)
            if length_so_far > 15:
                if self[current].__contains__("[STOP]"):
                    self[current].increment_frequency("[STOP]", 5)

            # if first order, we can just use the one-item tuple itself
            # as the state to look up the next word
            if order == 1:
                new_word = self.next_word(current)
                current = new_word
                if new_word[0] == "[STOP]":
                    # sentence formatting
                    generated[0] = generated[0].title()
                    return " ".join(generated) + "."
            # for a higher-order Markov chain, we have to determine the
            # new state using the old state and the word we just generated
            else:
                new_state = []
                for word in current[(1 - order):]:
                    new_state.append(word)
                new_word = self.next_word(current)
                if new_word[0] == "[STOP]":
                    # sentence formatting
                    generated[0] = generated[0].title()
                    if new_word.endswith("!") or new_word.endswith("?"):
                        return " ".join(generated)
                    else:
                        return " ".join(generated) + "."
                new_state.append(new_word[0])
                current = tuple(new_state)

            length_so_far += 1
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
            print("key: " + str(key))
            print("histogram: " + str(value))


if __name__ == '__main__':


    # test fist-order Markov chain
    # fish = Dictogram('fish.txt')
    # fish.print_self()
    # print("start words: " + str(fish.start_words))
    # print(fish.generate_sentence())


    mx = Dictogram('corpus.txt')
    print(mx.generate_sentence())
    #print(mx.start_words)


    #
