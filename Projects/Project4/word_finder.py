# Project 4 - Word Search
# Author: Nathan Diekema
# Instructor: Padlipsky
from funcs import *

puzzle = get_puzzle()
words = get_words()
#Print puzzle
print_puzzle(puzzle)

foundWords = []
horizontal = search_horizontal(puzzle,words)
vertical = search_vertical(puzzle,words)
diagonal = search_diagonal(puzzle,words)



for i in vertical:
    foundWords.append(i)
for i in horizontal:
    foundWords.append(i)
for i in diagonal:
    foundWords.append(i)
#finds all words in puzzle

newList = []
newFoundWords = []
for currentWords in foundWords:
    newFoundWords.append(currentWords[0])

for current in words:
    for lists in foundWords:
         if lists[0] == current:
            newList.append(lists)
            continue

    if (current not in newFoundWords): #means never was found
        newList.append([current])
        

#REORGANIZING LIST
newList = []
found = True
for current in range(len(words)): #for each given word
    for lists in foundWords:    #for each list in found words
        if lists[0] == words[current]:
            newList.append(lists)
    if len(newList) == 0:
            newList.append([words[current]])
    else:
        if newList[-1][0] != words[current]:
            newList.append([words[current]])

for word in newList:
    if len(word) > 1:
        print(word[0] + ": " + word[1] + " row: " + str(word[2]) + " column: " + str(word[3]))
    else:
        print(word[0] + ": word not found")