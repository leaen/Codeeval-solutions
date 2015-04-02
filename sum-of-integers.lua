function max_subarray(numbers)
    --for _, v in pairs(numbers) do print(v) end
    if #numbers == 0 then return 0 end

    max_ending_here = numbers[1]
    max_so_far = numbers[1]
    for i=2,#numbers do
        val = numbers[i]
        max_ending_here = math.max(max_ending_here + val, val)
        max_so_far = math.max(max_so_far, max_ending_here)
    end
    return max_so_far
end

for line in io.lines(arg[1]) do
    numbers = {}
    for m in line:gmatch('%-?%d+') do numbers[#numbers+1] = tonumber(m) end
    print(max_subarray(numbers))
end
