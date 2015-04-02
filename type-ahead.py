import sys
from collections import Counter

story = ['mary', 'had', 'a', 'little', 'lamb', 'its', 'fleece', 'was', 'white', 'as', 'snow', 'and', 'everywhere', 'that', 'mary', 'went', 'the', 'lamb', 'was', 'sure', 'to', 'go', 'it', 'followed', 'her', 'to', 'school', 'one', 'day', 'which', 'was', 'against', 'the', 'rule', 'it', 'made', 'the', 'children', 'laugh', 'and', 'play', 'to', 'see', 'a', 'lamb', 'at', 'school', 'and', 'so', 'the', 'teacher', 'turned', 'it', 'out', 'but', 'still', 'it', 'lingered', 'near', 'and', 'waited', 'patiently', 'about', 'till', 'mary', 'did', 'appear', 'why', 'does', 'the', 'lamb', 'love', 'mary', 'so', 'the', 'eager', 'children', 'cry', 'why', 'mary', 'loves', 'the', 'lamb', 'you', 'know', 'the', 'teacher', 'did', 'reply']

def get_ngram(target_word, words):
    matches = {}
    for i, word in enumerate(story):
        if word == target_word:
            # Cool get next n words
            match = []
            for index in range(i+1, i+words+1):
                try:
                    match.append(story[index])
                except IndexError:
                    # Skip this index
                    continue
            
            if match not in matches:
                matches[match]

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            words, start = line.strip().split(',')
            words = int(words)
            

if __name__ == '__main__':
    main()
