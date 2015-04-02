for line in io.lines(arg[1]) do
    total = 0
    for m in line:gmatch('%d') do total = total + tonumber(m) end
    print(total)
end
