import sys
import math

def play(game):
	game = game.strip().split(' ')
	
	upper_bound = int(game[0])
	lower_bound = 0

	game = game[1:]

	print(game)

	pointer = lower_bound + math.ceil((upper_bound-lower_bound) / 2)

	for instruction in game:
		print('pointer {0}, upper_bound {1}, lower_bound {2}'.format(pointer, upper_bound, lower_bound))

		if instruction == 'Yay!':
			break

		elif instruction == 'Lower':
			upper_bound = pointer

		elif instruction == 'Higher':
			lower_bound = pointer
			
		else:
			Exception("Unrecognized command, {0}".format(instruction))

		pointer = lower_bound + math.ceil((upper_bound-lower_bound) / 2)

	return pointer

with open(sys.argv[1]) as input_file:
	for game in input_file.readlines():
		print(play(game))
