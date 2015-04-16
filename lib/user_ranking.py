import math

def level(likes):
	base = 2
	levels = 30
	final_points = 2000
	scale = levels/math.log(final_points, base)
	level = math.floor(scale*math.log(likes, base))

	return level
