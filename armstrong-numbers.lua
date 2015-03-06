function isArmstrongNumber(n)
    n_str = tostring(n)
    n_digits = string.len(n_str)
    total = 0
    
    for i = 1, #n_str do
        local c = n_str:sub(i,i)
        -- print('c: ' .. c)
        local n = tonumber(c) ^ n_digits
        -- print('n: ' .. n)
        total = total + n
    end
    
    if n == total then
        return 'True'
    else
        return 'False'
    end
end

for line in io.lines(arg[1]) do
    io.write(isArmstrongNumber(tonumber(line)) .. '\n')
end
