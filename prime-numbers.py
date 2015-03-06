import sys
import math

def is_prime(n):
	
	for i in range(2, int(math.floor(math.sqrt(n))) + 1):
		if n%i == 0:
			return False
	return True

def find_primes_under(n):

	primes = []

	for i in range(2, n):
		if is_prime(i):
			primes += (i,)
		else:
			pass
	
	primes = map(str, primes)
	
	return ','.join(primes)

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(find_primes_under(int(line)))
