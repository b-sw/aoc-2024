import time
import os
clear = lambda: os.system('clear')

grid = open('input.txt').read().split('\n')
position = (0, 0)
direction = { 'v': (1, 0), '>': (0, 1), '<': (0, -1), '^': (-1, 0) }

def findStart() -> None:
	for rowIndex, row in enumerate(grid):
		for colIndex, cell in enumerate(row):
			if cell not in ['v', '>', '<', '^']:
				continue
			global position, direction
			position = (rowIndex, colIndex)
			direction = direction[cell]

def outOfBounds(position: tuple[int, int]) -> bool:
	return position[0] < 0 or position[0] >= len(grid) or position[1] < 0 or position[1] >= len(grid[0])

def isObstacle(position: tuple[int, int]) -> bool:
	return grid[position[0]][position[1]] == '#'

def printVisitedGrid() -> None:
	clear()
	for rowIndex, row in enumerate(grid):
		for colIndex, cell in enumerate(row):
			if (rowIndex, colIndex) in visited:
				print('\033[1;92mX\033[0m', end='')
			else:
				print(cell, end='')
		print()

# part 1
findStart()
visited: set[(int, int)] = set()
while True:
	visited.add(position)
	# time.sleep(0.05)
	# printVisitedGrid()
	nextPosition = (position[0] + direction[0], position[1] + direction[1])

	if outOfBounds(nextPosition):
		break

	if isObstacle(nextPosition): # turn right
		direction = (direction[1], -direction[0])
		nextPosition = (position[0] + direction[0], position[1] + direction[1])

	position = nextPosition

print(len(visited))
