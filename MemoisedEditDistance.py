import time

def memoizedDistance(x, y, memo=None):
    
    if memo is None: memo = {}
    if len(x) == 0: return len(y)
    if len(y) == 0: return len(x)
    if (len(x), len(y)) in memo:
        return memo[(len(x), len(y))]
    if x[-1] == y[-1]:
        return memoizedDistance(x[:-1], y[:-1], memo)
    substitution = memoizedDistance(x[:-1], y[:-1], memo) + 1
    deletion = memoizedDistance(x[:-1], y, memo) + 1
    insertion = memoizedDistance(x, y[:-1], memo) + 1
    ans = min(substitution, deletion, insertion)
    memo[(len(x), len(y))] = ans
    return ans

def distanceOfAllWordsToTheUserInput(userInput, words):
    distancedList = []
    for word in words:
        distancedList.append(memoizedDistance(userInput, word))
    
    return distancedList

def spelt():
    f = open ("dictionary.txt") #open a txt file containing the words
    contents = f.read ()
    words = contents.split("\n")
    userInput = raw_input (" spell check : ")
    startTime = time.time()

    #the operations for combining scores of the words (distances) and the words
    distancedWordList = distanceOfAllWordsToTheUserInput(userInput,words)
    zippedList = zip(distancedWordList, words)
    sortedZippedList = sorted(zippedList, key=lambda tup: tup[0])

    #is the word in dictionary? initially false. determined in the loop
    isItCorrect = False

    #looks if 0 score (best match) exists in the zipped array and if it does changes the isItCorrect boolean
    for i in range(len(sortedZippedList)):
        if (0 in sortedZippedList[i]):
            isItCorrect = True

    if (isItCorrect):
        print("Correct") 
    else:
        print("Suggested Alternatives:")
        for i in range(10):
            score, word = sortedZippedList[i]
            print(word)  

    endTime = time.time()
    print "The elapsed time executing blah , blah , blah was ", endTime - startTime


def main():
    
    spelt()


if __name__ == '__main__': main()