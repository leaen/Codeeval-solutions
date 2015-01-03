import sys

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(' '.join(word[0].title()+word[1:]
               for word in line.strip().split(' ')))
