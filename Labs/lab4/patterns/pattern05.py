import driver

def letter(row, col):
	if (row == 1 and col <= 0):
		return 'T'
	if (row == 2 and col <= 1):
		return 'T'
	if (row == 3 and col <= 2):
		return 'T'
	if (row == 4 and col <= 3):
		return 'T'
	if (row == 5 and col <= 4):
		return 'T'
	if (row == 6 and col <= 5):
		return 'T'
	if (row == 7 and col <= 6):
		return 'T'
	if (row == 8 and col <= 7):
		return 'T'
	if (row == 9 and col <= 8):
		return 'T'
	if (row == 10 and col <= 9):
		return 'T'
	if (row == 11 and col <= 10):
		return 'T'
	if (row == 12 and col <= 11):
		return 'T'
	if (row == 13 and col <= 12):
		return 'T'
	if (row == 14 and col <= 13):
		return 'T'
	if (row == 15 and col <= 14):
		return 'T'
	if (row == 16 and col <= 15):
		return 'T'
	if (row == 17 and col <= 16):
		return 'T'
	if (row == 18 and col <= 17):
		return 'T'
	if row == 19 and col <= 18:
		return 'T'
	else:
		return 'W'

if __name__ == '__main__':
   driver.comparePatterns(letter)