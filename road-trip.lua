for line in io.lines(arg[1]) do
    distances = {}
    for m in line:gmatch('%d+') do distances[#distances+1] = tonumber(m) end
    table.sort(distances)

    last = 0
    result = {}
    for _, val in pairs(distances) do
        result[#result+1] = val - last
        last = val
    end
    
    print(table.concat(result, ','))
end
