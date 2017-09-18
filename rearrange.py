import sys
import random
import enchant

d = enchant.Dict("en_US")

def scramble(wordsList):
    newIndexes = []
    newWords = []

    while(len(newIndexes) < len(wordsList)):
        rand_index = random.randint(0, len(wordsList) - 1)
        if rand_index not in newIndexes:
            newIndexes.append(rand_index)
    for i in range(0, len(wordsList)):
        newWords.append(wordsList[newIndexes[i]])
    return newWords

def findAnagram(word):
    found = []
    for i in range(0, 30):
        str = ""
        newWord = scramble(word)
        for j in range(len(word)):
            str += newWord[j]
        if (d.check(str) and str not in found):
            print(str)
            found.append(str)

if __name__ == '__main__':
    # store command line arguments
    words = sys.argv[1::]

    # scramble words
    print("\nScrambled words: ")
    scrambledWords = scramble(words)
    for word in scrambledWords:
        print(word)

    print("\nAnagrams: ")
    findAnagram("edits")
    findAnagram("beard")
    findAnagram("lapse")
