import time
import os

clear = lambda: os.system('clear')

def solve() -> None:
	xMax, yMax = 101, 103
	robots = getRobots()
	
	for _ in range(6587):
		for i, (x, y, dx, dy) in enumerate(robots):
			nx, ny = (x + dx) % xMax, (y + dy) % yMax
			robots[i] = (nx, ny, dx, dy)
	printRobots(robots, xMax, yMax)
	print(multiplyQuadrants(robots, xMax, yMax))


def solve2() -> None:
	xMax, yMax = 101, 103
	robots = getRobots()
	lowestEntropy = float('inf')
	lowestEntropyTime = None

	for s in range(xMax * yMax):
		if s % 100 == 0:
			print(s, lowestEntropy)
		for i, (x, y, dx, dy) in enumerate(robots):
			nx, ny = (x + dx) % xMax, (y + dy) % yMax
			robots[i] = (nx, ny, dx, dy)
		
		newEntropy = entropy(robots)
		if newEntropy < lowestEntropy:
			lowestEntropy = newEntropy
			lowestEntropyTime = s
			print('new lowest entropy:', lowestEntropy, 'at', lowestEntropyTime)


def getRobots() -> list:
	robots = []

	for line in open('input.txt').read().split('\n'):
		p, v = [p.split('=')[1].split(',') for p in line.split(' ')]
		robots.append((int(p[0]), int(p[1]), int(v[0]), int(v[1])))

	return robots

def printRobots(robots: list, xMax: int, yMax: int) -> None:
	grid = [['.' for _ in range(xMax)] for _ in range(yMax)]

	for x, y, _, _ in robots:
		grid[y][x] = '#'

	for row in grid:
		print(''.join(row))

def multiplyQuadrants(robots: list, xMax: int, yMax: int) -> int:
	quadrants = [0, 0, 0, 0]

	for x, y, _, _ in robots:
		q = getQuadrant(x, y, xMax, yMax)
		if q is not None:
			quadrants[q] += 1

	return quadrants[0] * quadrants[2] * quadrants[1] * quadrants[3]

def getQuadrant(x: int, y: int, xMax: int, yMax: int) -> int:
	if x == xMax // 2 or y == yMax // 2:

		return None
	
	if x < xMax // 2:
		return 1 if y < yMax // 2 else 2
	else:
		return 0 if y < yMax // 2 else 3
	
def entropy(robots: list) -> int:
	entropy = 0
	
	for robot in robots:
		rx, ry, _, _ = robot
		neighbors = 0
		
		for otherRobot in robots:
			nx, ny, _, _ = otherRobot
			if abs(rx - nx) <= 1 and abs(ry - ny) <= 1:
				neighbors += 1
		
		entropy += (8 - neighbors)

	return entropy

solve()
solve2()