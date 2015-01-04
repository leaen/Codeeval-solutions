import sys

def map_fizzbuzz(number, fizz_number, buzz_number):
	if (number%fizz_number==0 and number%buzz_number==0):
		return "FB"
	if (number%fizz_number==0):
		return "F"
	if (number%buzz_number==0):
		return "B"
	return str(number)

def fizzbuzz(fizz_number, buzz_number, limit):
	# Map map function with lambda to a range array.
	solution = map(lambda x: map_fizzbuzz(x, fizz_number, buzz_number), range(1,limit+1))

	return ' '.join(list(solution))

with open(sys.argv[1]) as input_file:
	for game in input_file.readlines():
		fizz, buzz, limit = game.strip().split(' ')
		print(fizzbuzz(int(fizz), int(buzz), int(limit)))
