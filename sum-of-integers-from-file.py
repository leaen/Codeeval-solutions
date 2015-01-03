import sys

total = 0

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		total += int(line.strip())

print(total)
