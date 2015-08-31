import random

def findcurvearea(func, x, y, height, width, samplesize):
	undercurve = 0
	for i in range(samplesize):
		rx = random.random() * width + x
		ry = random.random() * height + y
		# print("{}, {}, {}".format(rx, ry, func(rx)))
		if ry < (func(rx)):
			undercurve += 1
	return float(undercurve) / float(samplesize) * height * width

def quadratic_ex(x):
	return x * x + 2 * x + 1
print(findcurvearea(quadratic_ex, -10, -10, 20, 20, 10000000))
