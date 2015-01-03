import sys

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		if (int(problem.strip()) % 2 == 0):
			print(1)
		else:
			print(0)
