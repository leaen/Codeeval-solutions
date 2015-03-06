import sys
import string

def unshuffle(problem):
	shuffled_sentence, order = problem.split(';')
	order = list(map(lambda x: int(x), order.split(' ')))
	shuffled_sentence = shuffled_sentence.split(' ')

	sentence = shuffled_sentence[:]

	for index, element in enumerate(order):
		sentence[index] = shuffled_sentence[element - 1]
	
	return ' '.join(sentence)
	#return str(' '.join(sentence))

with open(sys.argv[1]) as input_file:
	for problem in input_file.readlines():
		print(unshuffle(problem.strip()))
