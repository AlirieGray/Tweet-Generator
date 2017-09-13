import sys
import re

def histogram(source_text):
    word_frequencies = dict()
    for word in source_text:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    #for element in word_frequencies:
    #    print(element + " " + str(word_frequencies[element]))
    return word_frequencies

def normalize(text):
    pass

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

if __name__ == '__main__':
    words = []
    with open("freud.txt") as file:
        for line in file:
            for word in line.split():
                words.append(word)
    print(histogram(words))
