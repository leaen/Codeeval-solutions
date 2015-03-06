import sys

def kill_people(circleinfo):
    n, m = circleinfo.split(',')
    n = int(n)
    m = int(m)
    
    people = list(range(n))
    index = 0
    dead = []
    while len(people) > 0:
        index = (index+m-1) % len(people)
        dead.append(people[index])
        del people[index]
    
    return dead

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(' '.join(map(str, kill_people(line.strip()))))

if __name__ == '__main__':
    main()
