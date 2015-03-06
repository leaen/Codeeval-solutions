function distance(p1, p2)
    return math.sqrt(math.pow(p2['x']-p1['x'],2) + math.pow(p2['y']-p1['y'],2))
end

function checkSquare(p1, p2, p3, p4)
    lengths = {}
    lengths[#lengths+1] = distance(p1, p2)
    lengths[#lengths+1] = distance(p2, p3)
    lengths[#lengths+1] = distance(p3, p4)
    lengths[#lengths+1] = distance(p4, p1)
    lengths[#lengths+1] = distance(p1, p3)
    lengths[#lengths+1] = distance(p2, p4)
    
    table.sort(lengths) 

    if lengths[1] == lengths[2] and lengths[1] == lengths[3] and lengths[1] == lengths[4] and lengths[5] == lengths[6] then
        return 'true'
    else
        return 'false'
    end
end

for line in io.lines(arg[1]) do
    numbers = {}
    for m in line:gmatch('[0-9]') do numbers[#numbers+1] = m end
    p1 = {['x'] = numbers[1], ['y'] = numbers[2]}
    p2 = {['x'] = numbers[3], ['y'] = numbers[4]}
    p3 = {['x'] = numbers[5], ['y'] = numbers[6]}
    p4 = {['x'] = numbers[7], ['y'] = numbers[8]}

    print(checkSquare(p1, p2, p3, p4))
end
