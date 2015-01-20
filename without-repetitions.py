import sys

def solve(problem):
	last_letter = ""
	solution = ""

	for letter in problem.strip():
		if (letter != last_letter):
			solution += letter
		last_letter = letter

	return solution

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
