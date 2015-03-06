import sys

def find_longest_word(line):
	line = sorted(line.strip().split(' '), key=lambda x: len(x), reverse=True)
	return line[0]

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(find_longest_word(line))
