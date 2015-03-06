fib_dict = {[0] = 0}
function fib(n)
    if n <= 2 then return 1 end
    return fib(n - 2) + fib(n - 1)
end

for line in io.lines(arg[1]) do
    io.write(fib(tonumber(line)) .. '\n')
end
