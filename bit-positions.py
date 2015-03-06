import sys

def solve(problem):
	number, i1, i2 = problem.split(',')
	number = bin(int(number))[2:][::-1]
	i1 = int(i1)
	i2 = int(i2)

	if number[i1-1] == number[i2-1]:
		return 'true'
	else:
		return 'false'

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
