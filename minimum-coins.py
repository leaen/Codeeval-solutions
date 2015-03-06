import sys

coin_vals = [5,3,1]

def main():
    with open(sys.argv[1]) as input_file:
        for target in input_file:
            target = int(target)

            current_val = 0
            coins_used = 0
            coin_index = 0
            
            while current_val != target:
                current_val += coin_vals[coin_index]
                if current_val > target:
                    current_val -= coin_vals[coin_index]
                    coin_index += 1
                    continue
                coins_used += 1
            
            print(coins_used)

if __name__ == '__main__':
    main()
