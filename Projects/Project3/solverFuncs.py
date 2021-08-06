# Project 3 - Calcudoku
# Author: Nathan Diekema
# Instructor: Padlipsky

def get_cages():
    cageNumber = int(input("Number of cages: "))

    cages = []
    x = 0
    while x < cageNumber:
       cages.append(input("Cage number " + str(x) + ": ").split(" "))
       cages[x] = [int(i) for i in cages[x]]
       x += 1

    return cages
    
def check_rows_valid(puzzle):
    i = 0
    valid = True

    while i < 5:
        if puzzle[i].count(1) > 1:
            valid = False
            break
        if puzzle[i].count(2) > 1:
            valid = False
            break
        if puzzle[i].count(3) > 1:
            valid = False
            break
        if puzzle[i].count(4) > 1:
            valid = False
            break
        if puzzle[i].count(5) > 1:
            valid = False
            break
        i += 1

    if valid == True:
        return True
    else:
        return False


def check_columns_valid(puzzle):
    x = 0
    five = [1,2,3,4,5]
    valid = True
    while x < 5:
        column = [puzzle[0][x], puzzle[1][x], puzzle[2][x], puzzle[3][x], puzzle[4][x]]
        for i in five:
           if column.count(i) > 1:
              valid = False
              break
              
        x += 1

    if valid == True:
        return True
    else:
        return False

def check_cages_valid(puzzle,cages):
    x = 0
    while x < len(cages):
        k = cages[x]
        total = k[0]
        sumCage = 0
        cageVal = []
        k = k[2:]
        for i in k:
            row = i // 5
            col =  i % 5
            sumCage += puzzle[row][col]
            cageVal.append(puzzle[row][col])

        if sumCage > total:
            valid = False
            break
        elif sumCage >= total and cageVal.count(0) > 0:
            valid = False
            break
        elif cageVal.count(0) == 0 and sumCage != total:
            valid = False
            break
        else:
            valid = True
        
        x += 1

    if valid == True:
        return True
    else:
        return False


def check_valid(puzzle,cages):
    if check_columns_valid(puzzle) == True and check_rows_valid(puzzle) == True and check_cages_valid(puzzle, cages) == True:
        return True
    else:
        return False

