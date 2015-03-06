import sys

# Dictionary used for converting between chess notation and cartesians.
coord_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

def onBoard(coord):
	# Checks if a cartesian coord is on the board.
	if coord[0] > 0 and coord[0] < 9 and coord[1] > 0 and coord[1] < 9:
		return True
	return False

def chess_to_cartesian(coord):
	# Converts from chess notation to cartesian coord.
	x = coord_dict[str(coord[0])]
	y = int(coord[1])

	return (x,y)

def cartesian_to_chess(coord):
	# Converts from cartesian coord to chess notation.
	x = coord_dict[coord[0]]
	y = str(coord[1])

	return ''.join([x, y])

def find_knight_moves(coord):
	knight_cartesian = chess_to_cartesian(coord)
	possible_moves = []

	# Possible moves for a knight.
	moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

	# Perform each move and add it's end position if valid (i.e stays on board)
	for move in moves:
		position = (knight_cartesian[0]+move[0], knight_cartesian[1]+move[1])
		if onBoard(position):
			possible_moves += (position,)

	# Convert coordinates back into chess notation.
	possible_moves = list(map(cartesian_to_chess, possible_moves))

	return sorted(possible_moves)

def main():
	with open(sys.argv[1]) as input_file:
		for coord in input_file.readlines():
			print(' '.join(find_knight_moves(coord.strip())))

if __name__ == '__main__':
	main()
