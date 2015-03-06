import sys

def find_first_non_repeat_char(line):
	seen_before = []
	repeated = []

	for c in line:
		if c in seen_before:
			repeated += c
		seen_before += c

	for c in line:
		if c not in repeated:
			return c

	return None

def main():
	with open(sys.argv[1]) as input_file:
		for line in input_file.readlines():
			print(find_first_non_repeat_char(line.strip()))

if __name__ == '__main__':
	main()
