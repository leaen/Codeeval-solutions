import sys

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(int(problem.strip(), 16))
