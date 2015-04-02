for line in io.lines(arg[1]) do
    numbers = {}
    for m in line:gmatch('%d+') do numbers[#numbers+1] = tonumber(m) end
    numbers[3] = numbers[2]
    while numbers[1] > numbers[3] do
        numbers[3] = numbers[3] + numbers[2]
    end
    print(numbers[3])
end
