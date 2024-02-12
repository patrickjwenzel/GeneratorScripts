# I like to see if I can make a word out of the three letters on a license plate
# or if I can't, if there's any words that exist
import re
import sys
from english_words import get_english_words_set

if len(sys.argv) < 2 or len(sys.argv) > 3:
    raise Exception('Incorrect number of arguments, need three letters and one guessing word (optional)')
elif len(sys.argv[1]) != 3:
    raise Exception('First argument must only contain three letters')

guessWord = sys.argv[2].lower() if len(sys.argv) == 3 else None
scrabbleValues = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

def getNewArgs(args):
    if len(args[0]) > 1 and len(args[1]) > 1 and len(args[2]) > 1:
        raise Exception('First three arguments must be singular letters')

    for arg in args:
        if re.search('[^a-zA-Z]', arg):
            raise Exception('All arguments must only be/contain letters')

    return [letter.lower() for letter in args[0:3]]

def getRegEx(args):
    r = '.*'
    string = r + args[0] + r + args[1] + r + args[2] + r

    return string

def validCharCounts(args, word):
    a1 = word.count(args[0])
    a2 = word.count(args[1])
    a3 = word.count(args[2])

    return a1 == 1 and a2 == 1 and a3 == 1

def getWordValue(word):
    keys = list(scrabbleValues.keys())
    score = 0
    for char in word:
        for key in keys:
            if char.upper() in scrabbleValues[key]:
                score += key
                break

    return score

def printWords(wordsArg):
    remainingWords = len(wordsArg) % 5
    i = 0
    while i < (len(wordsArg) - remainingWords - 4):
        s = ''
        z = 0
        while z < 5:
            s += wordsArg[i + z] + ('\t\t' if z < 4 else '\n')
            z += 1

        print(s)
        i += 5

    i = len(wordsArg) - remainingWords
    s = ''
    while i < len(wordsArg):
        s += wordsArg[i] + '\t\t' if i < len(wordsArg) else ''
        i += 1

    print(s)

words = list(get_english_words_set(['web2'], lower=True))
sargs = sys.argv[1]

args = getNewArgs([sargs[0], sargs[1], sargs[2], 'None' if len(sys.argv) != 3 else sys.argv[2]])
regex = getRegEx(args)

foundWords = list(filter(lambda word: re.match(regex, word) and validCharCounts(args, word), words))
wordList = {}

for word in foundWords:
    try:
        wordList[len(word)].append(word)
    except:
        wordList[len(word)] = [word]

for key in wordList.keys():
    wordList[key].sort()

keys = list(wordList.keys())
keys.sort()

for key in keys:
    print(str(key) + ' letter words:')
    printWords(wordList[key])
    print()
    print()


if guessWord != None:
    isFound = guessWord in foundWords
    status = ' is a valid word' if isFound else ' is NOT a valid word'
    score = getWordValue(guessWord) if isFound else None
    print(guessWord + status)
    if score:
        print('This word would have gotten a score of: ' + str(score))