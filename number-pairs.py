#incomplete

import sys

def solve(problem):

	arr, test_sum = problem.strip().split(';')
	test_sum = int(test_sum)
	arr = list(map(int, arr.strip().split(',')))
	pairs = []
	last_i = 0

	print(arr)
	print(test_sum)

	for i in arr:
		if i + last_i == test_sum:
			pairs += [[last_i, i]]
		else:
			pass
		last_i = i

	print(pairs)

	if len(pairs) > 0:
		return ';'.join(list(map(lambda x: '{},{}'.format(*x), pairs)))
	else:
		return 'NULL'

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(solve(problem))
