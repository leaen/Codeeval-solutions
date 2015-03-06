import sys
import itertools

def reverse_list(problem):
	array, shift = problem.split(';')
	array = array.split(',')
	shift = int(shift)
	reversed_arr = []

	for i in range(int(len(array) / shift)+1):
		start = i*shift
		end = (i+1)*shift
		reversed_arr.append(list(reversed(array[start:end])))

	reversed_arr = list(itertools.chain(*reversed_arr))

	return reversed_arr

def main():
	with open(sys.argv[1]) as input_file:
		for line in input_file.readlines():
			print(','.join(reverse_list(line.strip())))


if __name__ == '__main__':
	main()
