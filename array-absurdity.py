import sys

def solve(problem):
	arr = problem.split(';')[1].split(',')
	checked = []

	for i in arr:
		if i in checked:
			return i
		else:
			checked += (i,)

	return '0'

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
