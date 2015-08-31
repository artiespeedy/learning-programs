function findpi(samplesize)
	pointsinside = 0
	for i = 0, samplesize, 1 do
		pointx = math.random()
		pointy = math.random()
		dist = math.sqrt(pointx * pointx + pointy * pointy)
		if 1 > dist then
			pointsinside = pointsinside + 1
		end
	end

	return 4 * pointsinside / samplesize
end

print(findpi(100000000))
