import sys

def resize_line(line):
	line = line.strip()

	# If line length is ≤ 55 characters, print it without any changes.
	if len(line) <= 55:
		return line

	# If the line length is > 55 characters, change it as follows:
	# Trim the line to 40 characters.
	line = line[:40].strip()

	# Handle any trailing malformed words.

	if line[-1] != " ":
		line = list(line)
		while line[-1] != " ":
			del line[-1]

			# Handle special case.
			if len(line) == 0:
				return "... <Read More>"
		del line[-1]
		line = ''.join(line)

	# And add <Read More> to the end.
	line = line + "... <Read More>"

	return line


with open(sys.argv[1]) as input_file:
	for line in input_file.readlines():
		print(resize_line(line))
