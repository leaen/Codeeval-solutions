import sys

def find_sums(numbers, target):
    pairs = []

    for number in numbers:
        # We don't need to go past target/2, all the pairs would've been found by now.
        if number > target / 2:
            break

        if target-number in numbers:
            # Cool we found a pair
            # Check edge case where number is half of target
            if number // 2 == target:
                if numbers.count(number) < 2:
                    continue

            pairs.append([number, target-number])
    return pairs

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            numbers, target = line.strip().split(';')
            numbers = list(map(int, numbers.split(',')))
            target = int(target)

            pairs = find_sums(numbers, target)
            pairs = [','.join(map(str, x)) for x in pairs]

            if pairs:
                print(';'.join(pairs))
            else:
                print('NULL')

if __name__ == '__main__':
    main()
