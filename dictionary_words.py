import sys
import random

def MakeSentence(source):
    newSentence = ""
    sentenceLength = random.randint(4, 7)
    for i in range (0, sentenceLength):
        newSentence += source[random.randint(0, len(source) - 1)] + " "
    return newSentence

if __name__ == '__main__':
    words = []
    with open("/usr/share/dict/words") as file:
        for word in file:
            words.append(word.rstrip())
    print(MakeSentence(words))
