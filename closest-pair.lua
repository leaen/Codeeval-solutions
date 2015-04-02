function round(num, idp)
    local mult = 10^(idp or 0)
    return math.floor(num * mult + 0.5) / mult
end

function distance(x1, x2, y1, y2)
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
end

points = {}

for line in io.lines(arg[1]) do
    local numbers = {}
    for m in line:gmatch('%d+') do numbers[#numbers+1] = tonumber(m) end
    if #numbers == 2 then
        point = {['x']=numbers[1], ['y']=numbers[2]}
        points[#points+1] = point
    end
end

shortest_distance = distance(points[1]['x'], points[2]['x'], points[1]['y'], points[2]['y'])

for i=1,#points do
    for j=1,#points do
        if i ~= j then
            p1 = points[i]
            p2 = points[j]
            shortest_distance = math.min(shortest_distance, distance(p1['x'], p2['x'], p1['y'], p2['y']))
        end
    end
end

print(string.format("%.3f", tostring(1.3339)))
print(string.format("%.4f", round(shortest_distance, 4)))
