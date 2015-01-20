import sys

def decimal_to_binary(number):
	return bin(number)[2:]

with open(sys.argv[1]) as input_file:
	for number in input_file.readlines():
		print(decimal_to_binary(int(number)))
