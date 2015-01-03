import sys
from functools import reduce

def happy_step(n):
	n_str = str(n)
	total = 0
	for digit in n_str:
		total += (int(digit)**2)
	return total

def check_happy_number(problem):
	previous = []
	while (problem != 1):
		problem = happy_step(problem)
		if (problem in previous):
			return False
		previous += (problem,)
	return True

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		if (check_happy_number(int(problem.strip()))):
			print(1)
		else:
			print(0)
