import sys
import random

def MakeSentence(corpus):
    newSentence = ""
    sentenceLength = random.randint(4, 7)
    for i in range (0, sentenceLength):
        newSentence += corpus[random.randint(0, len(corpus) - 1)] + " "
    return newSentence

if __name__ == '__main__':
    words = []
    with open("/usr/share/dict/words") as file:
        for word in file:
            words.append(word.rstrip())

    print(MakeSentence(words))
