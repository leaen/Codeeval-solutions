import sys

with open(sys.argv[1]) as input_file:
	for line in input_file:
		# Reverse string and print it.
		print(' '.join(reversed(list(line.strip().split(' ')))))
