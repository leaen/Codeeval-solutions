function compress(seq)
    if #seq == 0 then return '' end
    
    last_num = seq[1]
    cur_num_count = 0
    result = {}
    for _, val in pairs(seq) do
        if val ~= last_num then
            if cur_num_count > 0 then
                result[#result+1] = cur_num_count
                result[#result+1] = last_num
                last_num = val
                cur_num_count = 0
            end
        end 
        cur_num_count = cur_num_count + 1
    end
    result[#result+1] = cur_num_count
    result[#result+1] = last_num
    return result
end

for line in io.lines(arg[1]) do
    numbers = {}
    for m in line:gmatch('%d+') do numbers[#numbers+1] = tonumber(m) end
    print(table.concat(compress(numbers), ' '))
end
