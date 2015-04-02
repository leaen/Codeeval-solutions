import sys

def rotate_array(array):
    if array == []:
        return array

    result = []
    for i in range(len(array[0])):
        result.append([])

    for row in array:
        for i, e in enumerate(reversed(row)):
            result[i].append(e)
    
    return result

def spiral(array):
    result = []
    while len(array) > 0:
        # print top row and delete top row
        for e in array[0]:
            result.append(e)
        del array[0]
        array = rotate_array(array)
    
    return result

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            width, height, data = line.strip().split(';')
            width = int(width)
            height = int(height)
            data = data.split()

            array = []

            for i in range(width):
                row = []
                for j in range(height):
                    row.append(data[i*height + j])
                array.append(row)

            print(' '.join(spiral(array)))

if __name__ == '__main__':
    main()
