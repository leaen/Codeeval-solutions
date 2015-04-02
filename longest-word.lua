for line in io.lines(arg[1]) do
    longest_word = ''
    for word in line:gmatch('%S+') do
        if word:len() > longest_word:len() then longest_word = word end
    end
    print(longest_word)
end
