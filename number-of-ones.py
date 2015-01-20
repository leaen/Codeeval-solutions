import sys

def decimal_to_binary(number):
	return bin(number)[2:]

def count_ones(number):
	bin_string = decimal_to_binary(number)
	return bin_string.count('1')

with open(sys.argv[1]) as input_file:
	for number in input_file.readlines():
		print(count_ones(int(number)))
