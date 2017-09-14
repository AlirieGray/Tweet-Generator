import sys
import re

def histogram_dict(source_text):
    word_frequencies = dict()
    for word in source_text.split(' '):
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    #for element in word_frequencies:
    #    print(element + " " + str(word_frequencies[element]))
    return word_frequencies

def histogram_tuple(source_text):
    # each tuple in this list has a word and then its frequency
    list_of_tuples = []
    for word in source_text.split(' '):
        for word_tuple in list_of_tuples:
            if word_tuple[0] == word:
                word_tuple[1] += 1
            else:
                list_of_tuples.append((word, 1))


def normalize(text):
    return_string = ' '.join(text)
    return_string = re.sub(r'[0-9]+', '', return_string)
    return_string = re.sub(r'[\]]+', '', return_string)
    return_string = re.sub(r'[\[]+', '', return_string)
    return_string = re.sub(r'[*]+', '', return_string)
    return_string = re.sub(r'[-]+', '', return_string)
    return_string = re.sub(r'[\"]+', '', return_string)
    return return_string

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]

if __name__ == '__main__':
    words = []
    with open('freud.txt') as file:
        for line in file:
            for word in line.split():
                words.append(word)

    words = normalize(words)
    histogram = (histogram_dict(words)) # a dictionary of word: frequency
    print("The: " + frequency("The", histogram))
    print("they: " + frequency("they", histogram))
