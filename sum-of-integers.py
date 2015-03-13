import sys

def max_subarray(numbers):
    # Kadane's algorithm
    current_sum = 0
    best_sum = 0
    for e in numbers:
        if current_sum + e > 0:
            current_sum += e
        else:
            current_sum = 0
        best_sum = max(best_sum, current_sum)
    return best_sum

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            numbers = line.strip().split(',')
            numbers = list(map(int, numbers))
            
            max_sum = max_subarray(numbers)
            print(max_sum)

if __name__ == '__main__':
    main()
