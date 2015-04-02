function value_in_table(t, v)
    for _, val in pairs(t) do
        if val == v then return true end
    end
    return false
end

function happy_step(n)
    total = 0
    for digit in tostring(n):gmatch('%d') do
        total = total + tonumber(digit)^2
    end
    return total
end

function is_happy(n)
    previous = {}
    while n ~= 1 do
        n = happy_step(n)
        if value_in_table(previous, n) then
            return '0'
        end
        previous[#previous+1] = n
    end
    return '1'
end

for line in io.lines(arg[1]) do
    result = is_happy(tonumber(line))
    print(result)
end
