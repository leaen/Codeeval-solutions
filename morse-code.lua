lookup = { ['.-']    = 'a',
           ['-...']  = 'b',
           ['-.-.']  = 'c',
           ['-..']   = 'd',
           ['.']     = 'e',
           ['..-.']  = 'f',
           ['--.']   = 'g',
           ['....']  = 'h',
           ['..']    = 'i',
           ['.---']  = 'j',
           ['-.-']   = 'k',
           ['.-..']  = 'l',
           ['--']    = 'm',
           ['-.']    = 'n',
           ['---']   = 'o',
           ['.--.']  = 'p',
           ['--.-']  = 'q',
           ['.-.']   = 'r',
           ['...']   = 's',
           ['-']     = 't',
           ['..-']   = 'u',
           ['...-']  = 'v',
           ['.--']   = 'w',
           ['-..-']  = 'x',
           ['-.--']  = 'y',
           ['--..']  = 'z',
           ['-----'] = '0',
           ['.----'] = '1',
           ['..---'] = '2',
           ['...--'] = '3',
           ['....-'] = '4',
           ['.....'] = '5',
           ['-....'] = '6',
           ['--...'] = '7',
           ['---..'] = '8',
           ['----.'] = '9',
           ['*']    = ' ' }

function split(sString, sSeparator, nMax, bRegexp)
    assert(sSeparator ~= '')
    assert(nMax == nil or nMax >= 1)
    
    local aRecord = {}
    
    if sString:len() > 0 then
        local bPlain = not bRegexp
        nMax = nMax or -1
        
        local nField=1 nStart=1
        local nFirst,nLast = sString:find(sSeparator, nStart, bPlain)
        while nFirst and nMax ~= 0 do
            aRecord[nField] = sString:sub(nStart, nFirst-1)
            nField = nField+1
            nStart = nLast+1
            nFirst,nLast = sString:find(sSeparator, nStart, bPlain)
            nMax = nMax-1
        end
        aRecord[nField] = sString:sub(nStart)
    end
    return aRecord
end

for line in io.lines(arg[1]) do
    print('running')
    blocks = split(line, '  ')

    for i=1, #blocks  do
        print('found block')
        print('block: ' .. block)
        for word in block:gmatch('[.-]+') do
            io.write(word .. '\n')
            --io.write(lookup[section])
        end
    end
    io.write('\n')
    
    --[[
    for k, v in pairs(lookup) do
        print(string.format('replacing %s with %s', k, v))
        print(line)
        line = line:gsub(k, v)
    end
    print(line)
    --]]
end
