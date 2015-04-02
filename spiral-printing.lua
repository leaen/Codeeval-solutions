function reverse_table(t)
    for _, v in pairs(t) do print(v) end
    local size = #t
    local result = {}

    for i,e in pairs(t) do
        result[size-i+1] = e
    end

    return result
end

function rotate_array(array)
    print('rotating array')
    print('vals')
    for k, v in pairs(array) do print(v) end
    print('end vals')
    if #array == 0 then return {} end

    result = {}
    for i=1,#array[1] do
        result[#result+1] = {}
    end

    for _, row in pairs(array) do
        for i, e in pairs(row) do
            result[i][#result[i]+1] = e
        end
    end

    for k, v in pairs(array) do print(unpack(v)) end
    return result
end

function spiral(array)
    result = {}
    while #array > 0 do
        --print('first part is: ' .. result)-- table.concat(result, ' '))
        
        --print('array:')
        for _, v in pairs(array) do print(table.concat(v, ' ')) end
        
        print('adding top row to result')
        for _, e in pairs(array[1]) do
            result[#result+1] = e
        end
        print('added top row to result')

        -- delete top row
        print('deleting top row')
        table.remove(array, 1)
        print('deleted top row')
        
        -- rotate array
        print('rotating array')
        array = rotate_array(array)
        print('rotated')
    end
    return result
end

for line in io.lines(arg[1]) do
    numbers = {}
    for m in line:gmatch('%d+') do numbers[#numbers+1] = tonumber(m) end
    
    width = numbers[1]
    height = numbers[2]

    table.remove(numbers, 1)
    table.remove(numbers, 1)

    array = {}
    for i=1,width do
        row = {}
        for j=1,height do
            row[#row+1] = numbers[((i-1)*height) + j]
        end
        array[#array+1] = row
    end
   
    result = spiral(array)
    print(table.concat(result, ' '))

    print('finished')
end
