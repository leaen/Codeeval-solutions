function lowest_unique(line)
    numbers = {}
    for m in line:gmatch('[0-9]+') do numbers[#numbers+1] = tonumber(m) end
    
    table.sort(numbers)
   
    for k, v in pairs(numbers) do
        if numbers[k-1] ~= v and numbers[k+1] ~= v then
            result = 0
            for i=1,#line do if line:sub(i,i) == tostring(v) then result = math.ceil(i/2) end end
            return result 
       end
    end

    return 0 
end

for line in io.lines(arg[1]) do
    print(lowest_unique(line))
end
