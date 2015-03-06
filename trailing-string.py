import sys

def solve(problem):

	sentence, trail = problem.strip().split(',')
	
	if sentence[len(sentence) - len(trail):] == trail:
		return '1'
	else:
		return '0'

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
