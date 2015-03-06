import sys

vocab =  ' !"#$%&\'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
vocab_dict = dict(zip(vocab, range(len(vocab))))

def gronsfeld_decipher(ciphertext, key):
    plaintext = ''
    
    for i, letter in enumerate(ciphertext):
        step_key = key[i%len(key)]
        plaintext += vocab[vocab_dict[letter] - int(step_key)]

    return plaintext
    

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file:
            key, ciphertext = problem.strip().split(';', 1)
            print(gronsfeld_decipher(ciphertext, key))

if __name__ == '__main__':
    main()
