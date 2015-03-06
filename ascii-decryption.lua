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

function compare(t, fn)
    if #t == 0 then return nil, nil end
    local key, value = 1, t[1]
    for i = 2, #t do
        if fn(value, t[i]) then
            key, value = i, t[i]
        end
    end
    return value
end

function decrypt(phrase)
    -- Split into numbers by space delimiter, then scrap the
    -- first four values which aren't needed.
    sentence = split(phrase, ' ')
    for i = 1,4 do table.remove(sentence, 1) end
    
    -- Change everything into integers.
    for k, v in pairs(sentence) do sentence[k] = tonumber(v) end
    
    -- Get minimum value (the space character) and with it
    -- calculate the ascii offset.
    minimum_val = compare(sentence, function(a,b) return a > b end)
    offset = 32 - minimum_val 
    
    -- Go through and using the offset convert each number
    -- back into it's ascii character.
    plaintext = ''
    for i=1, #sentence do
        plaintext = plaintext .. string.char(sentence[i] + offset) 
    end
    
    return plaintext
end

for line in io.lines(arg[1]) do
    print(decrypt(line))
end
