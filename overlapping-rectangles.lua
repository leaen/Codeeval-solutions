for line in io.lines(arg[1]) do
    coords = {}
    for m in line:gmatch('%-?%d+') do coords[#coords+1] = tonumber(m) end
    square1 = {['upperleft'] = {['x'] = coords[1], ['y'] = coords[2]}, ['lowerright'] = {['x'] = coords[3], ['y'] = coords[4]}}
    square2 = {['upperleft'] = {['x'] = coords[5], ['y'] = coords[6]}, ['lowerright'] = {['x'] = coords[7], ['y'] = coords[8]}}
   
    -- ! ( P2.y < P3.y || P1.y > P4.y || P2.x < P3.x || P1.x > P4.x )
    -- ra.topx > rb.botx || ra.botx < rb.topx || ra.topy > rb.boty || ra.boty < rb.topy

    if square1['lowerright']['y'] > square2['upperleft']['y'] or square1['upperleft']['y'] < square2['lowerright']['y'] or square1['lowerright']['x'] < square2['upperleft']['x'] or square1['upperleft']['x'] > square2['lowerright']['x'] then
        print('False')
    else
        print('True')
    end
    --[[
    if square1['lowerright']['x'] > square2['upperleft']['x'] and square1['lowerright']['y'] < square2['upperleft']['y'] then
        print('True')
    else
        print('False')
    end
    --]]
    --for k, v in pairs(coords) do print(k, v) end
end
