import sys

def fizzbuzz(fizz_number, buzz_number, limit):
	#game = range(1, limit+1)
	game = list(map(lambda x: str(x), range(1, limit+1)))

	for index, element in enumerate(game):
		if(index+1 % fizz_number == 0 and index+1 % buzz_number == 0):
			game[index] = "FB"
		elif(index+1 % fizz_number == 0):
			game[index] = "F"
		elif(index+1 % buzz_number == 0):
			game[index] = "B"

	return ' '.join(game)

with open(sys.argv[1]) as input_file:
	for game in input_file.readlines():
		fizz, buzz, limit = game.strip().split(' ')
		print(fizzbuzz(int(fizz), int(buzz), int(limit)))
