import sys

def get_remainder(n, m):
	while n > m:
		n -= m
	return n

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		n, m = list(map(int, line.strip().split(',')))
		print(get_remainder(n, m))
