function get_remainder(n, m):
    remainder = n
    while remainder > m do
        remainder = remainder - m
    end
    return remainder
end

for line in io.lines(arg[1]) do
    n = 
    m = 
    io.write(get_remainder(n, m) .. '\n')
end
