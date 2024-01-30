# I like to see if I can make a word out of the three letters on a license plate
# or if I can't, if there's any words that exist
import re
import sys
from english_words import get_english_words_set

if len(sys.argv) < 4 or len(sys.argv) > 5:
    raise Exception('Incorrect number of arguments, need three letters and one guessing word (optional)')

guessWord = sys.argv[4].lower() if len(sys.argv) == 5 else None
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

words = list(get_english_words_set(['web2'], lower=True))

args = getNewArgs(sys.argv[1:])
regex = getRegEx(args)

foundWords = list(filter(lambda word: re.match(regex, word) and validCharCounts(args, word), words))
foundWords.sort()

print(foundWords)

if guessWord != None:
    isFound = guessWord in foundWords
    status = ' is a valid word' if isFound else ' is NOT a valid word'
    score = getWordValue(guessWord) if isFound else None
    print(guessWord + status)
    if score:
        print('This word would have gotten a score of: ' + str(score))