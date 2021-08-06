# Project 3 - Calcudoku
# Author: Nathan Diekema
# Instructor: Padlipsky
from solverFuncs import *

#Initialize puzzle[] 
puzzle = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
cages = get_cages()
checks = 0
backtracks = 0
puzzleCell = 0

while puzzleCell <= 24:
   row = puzzleCell // 5 
   col = puzzleCell % 5
   puzzle[row][col] += 1
   checks += 1
   check = check_valid(puzzle, cages)
   while check == False:
      puzzle[row][col] += 1
      while puzzle[row][col] > 5:
         puzzle[row][col] = 0
         puzzleCell -= 1
         backtracks += 1
         row = puzzleCell // 5
         col = puzzleCell % 5
         puzzle[row][col] += 1
      check = check_valid(puzzle, cages)
      checks += 1
   puzzleCell += 1

print("\n---Solution---\n")
i = 0
while i < 5:
   for x in puzzle[i][0:]:
      val = str(x)
      print(val, end = ' ')
   print()
   i += 1
print("\nchecks: " + str(checks) + " backtracks: " + str(backtracks))
