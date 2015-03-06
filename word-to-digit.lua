lookup = { ['zero']  = '0',
           ['one']   = '1',
           ['two']   = '2',
           ['three'] = '3',
           ['four']  = '4',
           ['five']  = '5',
           ['six']   = '6',
           ['seven'] = '7',
           ['eight'] = '8',
           ['nine']  = '9',
           ['\n']    = '',
           [';']     = '' }

for line in io.lines(arg[1]) do
    for k, v in pairs(lookup) do line = line:gsub(k, v) end
    print(line)
end
