function trim(s)
    return (s:gsub("^%s*(.-)%s*$", "%1"))
end

function find_hidden_digits(message)
    lookup_table = {}
    letters = 'abcdefghij'
    for i=1, #letters do lookup_table[letters:sub(i,i)] = i-1 end
    for i = 0,9 do lookup_table[tostring(i)] = tostring(i) end
    
    none = true
    
    for i=1, #message do
        character = message:sub(i,i)
        if lookup_table[character] ~= nil then
            io.write(lookup_table[character])
            none = false
        end
    end
    if none then io.write('NONE') end
    io.write('\n')
end

for line in io.lines(arg[1]) do
    find_hidden_digits(trim(line))
end
