# Project 4 - Word Search
# Author: Nathan Diekema
# Instructor: Padlipsky
import math


def get_puzzle():
    puzzle = input()
    puzzle = [puzzle[i:i+10] for i in range(0, 100, 10)]
    return puzzle

def get_words():
    words = input()
    words = words.split(' ')
    return words

def print_puzzle(puzzle):
    print("Puzzle:\n")
    for i in puzzle:
        print(i)
    print()

def search_vertical(puzzle,words):
    found = []
    row = 0
    col = 0
    x = 0
    while x < 10:
        column = [puzzle[0][x], puzzle[1][x], puzzle[2][x], puzzle[3][x], puzzle[4][x], puzzle[5][x], puzzle[6][x], puzzle[7][x], puzzle[8][x], puzzle[9][x]] 
        column = ''.join(column)
        reverseCol = column[::-1]
        for k in words:
            if k in column:
                col = x
                row = column.find(k)
                templist = []
                templist.append(k)
                templist.append("(DOWN)")
                templist.append(row)
                templist.append(col)
                found.append(templist)

            if k in reverseCol:
                col = x
                row = math.fabs(reverseCol.find(k) - 9)
                templist = []
                templist.append(k)
                templist.append("(UP)")
                templist.append(int(row))
                templist.append(col)
                found.append(templist)
        x += 1
    return found

def search_horizontal(puzzle, words):
    found = []
    row = 0
    col = 0
    for p in puzzle:    #p is specific row in puzzle
        reverseP = p[::-1]
        for k in words:
            if k in p:
                col = p.find(k)
                row = puzzle.index(p)
                templist = []
                templist.append(k)
                templist.append("(FORWARD)")
                templist.append(row)
                templist.append(col)
                found.append(templist)

            if k in reverseP:
                col = math.fabs(reverseP.find(k) - 9)
                row = puzzle.index(p) 
                templist = []
                templist.append(k)
                templist.append("(BACKWARD)")
                templist.append(row)
                templist.append(int(col))
                found.append(templist)
    return found

def search_diagonal(puzzle,words):
    found = []
    diagonal = []
    readList = []
    #LOWER HALF
    for valRow in range(len(puzzle)):
        row = valRow
        for col in range(len(puzzle) - valRow):
            templist = []     
            templist.append(puzzle[row][col])
            templist.append(row)
            templist.append(col)
            diagonal.append(templist)
            row += 1
    #UPPER HALF
    for valCol in range(1,10):
        col = valCol
        for row in (range(len(puzzle) - valCol)):
            templist = []
            templist.append(puzzle[row][col])
            templist.append(row)
            templist.append(col)
            diagonal.append(templist)
            col += 1

    for pos in diagonal:
        readList.append(pos[0])
    read = ''.join(readList)
    for k in words:
        if k in read:
            index = read.find(k)
            row = diagonal[index][1]
            col = diagonal[index][2]
            templist = []
            templist.append(k)
            templist.append("(DIAGONAL)")
            templist.append(row)
            templist.append(col)
            found.append(templist)
    return found
