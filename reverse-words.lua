for line in io.lines(arg[1]) do
    words = {}
    for word in line:gmatch('%S+') do words[#words+1] = word end
    result = words[#words]
    for i=1,#words-1 do
        result = result .. ' ' ..  words[#words-i]
    end
    print(result)
end
