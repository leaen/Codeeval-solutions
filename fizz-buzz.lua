function fizzbuzz(f, b, n) 
    elements = {}
    for i=1,n do
        if i % f == 0 and i % b == 0 then
            elements[#elements+1] = "FB" 
        end
        if i % f == 0 and i % b ~= 0 then
            elements[#elements+1] = "F" 
        end
        if i % f ~= 0 and i % b == 0 then
            elements[#elements+1] = "B"  
        end
        if i % f ~= 0 and i % b ~= 0 then
            elements[#elements+1] = tostring(i)
        end
    end
    return table.concat(elements, ' ')
end

for line in io.lines(arg[1]) do
    values = {}
    for m in line:gmatch('%d+') do values[#values+1] = tonumber(m) end
    print(fizzbuzz(unpack(values)))
end
