import sys

def unshuffle(problem):
    shuffled_sentence, order = problem.split(';')
    order = [int(x) for x in order.split(' ')]
    shuffled_sentence = shuffled_sentence.split(' ')

    sentence = shuffled_sentence[:]

    for index, element in enumerate(order):
        sentence[index] = shuffled_sentence[element - 1]

    return ' '.join(sentence)

with open(sys.argv[1]) as input_file:
    for problem in input_file.readlines():
        print(unshuffle(problem.strip()))
