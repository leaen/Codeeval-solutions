import sys

def is_palindrome(number):
	if (''.join(reversed(str(number))) == str(number)):
		return True
	return False

def solve(number):
	loops = 0
	while(is_palindrome(number) != True):
		number = int(number) + int(str(number)[::-1])
		loops += 1
	return "{0} {1}".format(loops, number)

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
