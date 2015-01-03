import sys

fib_dict = {0: 0}
def fib(n):
	for k in range(1,n+1):
		if (k <= 2):
			f = 1
		else:
			f = fib_dict[k-1] + fib_dict[k-2]
		fib_dict[k] = f
	return fib_dict[n]

with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(fib(int(line.strip())))
