import sys
import re

def remove_chars(sentence, bad_chars):
	return re.sub('[' + bad_chars + ']', '', sentence)

def remove_chars2(sentence, bad_chars):
	for char in bad_chars:
		sentence = sentence.replace(char, '')
	return sentence

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		
		sentence, bad_chars = problem.strip().split(',')
		bad_chars = bad_chars.strip()

		print(remove_chars(sentence, bad_chars))
