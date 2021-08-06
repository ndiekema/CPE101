import driver

def letter(row, col):
	if (row == 0 or row == 6) and (col == 0 or col == 6):
		return 'X'
	elif (row == 1 or row == 5) and (col == 1 or col == 5):
		return 'X'
	elif (row == 2 or row == 4) and (col == 2 or col == 4):
		return 'X'
	elif (row == 3) and (col == 3):
		return 'X'
	else:
		return 'O'

if __name__ == '__main__':
   driver.comparePatterns(letter)