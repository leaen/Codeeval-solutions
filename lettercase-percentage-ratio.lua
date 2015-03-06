function solve(line)
    lowercase = 0
    for _ in line:gmatch('[a-z]') do lowercase = lowercase + 1 end
    uppercase = 0
    for _ in line:gmatch('[A-Z]') do uppercase = uppercase + 1 end
    
    print('lowercase: %f uppercase: %f', lowercase * 100 / line:len(), (uppercase * 100 / line:len()))
    -- return ('lowercase: ' .. lowercase .. ' uppercase: ' .. uppercase .. '\n')

end

for line in io.lines(arg[1]) do
    solve(line)
end
