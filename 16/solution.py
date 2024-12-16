DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
WALL = '#'
START = 'S'
END = 'E'

import heapq

def solve() -> None:
	grid = parseGrid()
	start, end = findStartEnd(grid)
	print(dijkstraSearch(start, end, grid))

def parseGrid() -> list[list[str]]:
	return [list(row) for row in open('input.txt').read().split('\n')]

def findStartEnd(grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
	start, end = None, None

	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == START:
				start = (r, c)

				if end:
					return start, end
			elif grid[r][c] == END:
				end = (r, c)

				if start:
					return start, end

	raise ValueError('Start and end not found')

def dijkstraSearch(start: tuple[int, int], target: tuple[int, int], grid: list[list[str]]) -> int:
	distances = { start: (0, []) }
	pq = [(0, start, (0, 1), [start])]
	paths = {}

	while pq:
		distance, position, dir, path = heapq.heappop(pq)

		if position == target:
			paths[distance] = paths.get(distance, []) + [path]
			continue
		
		r, c = position

		for newDir in DIRS:
			dr, dc = newDir
			nr, nc = r + dr, c + dc

			if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]) or grid[nr][nc] == WALL:
				continue

			moveCost = 1 + (0 if newDir == dir else 1000)
			newDistance = distance + moveCost
			neighbor = (nr, nc, newDir)

			if neighbor not in distances or newDistance <= distances[neighbor]:
				distances[neighbor] = newDistance
				heapq.heappush(pq, (newDistance, (nr, nc), newDir, path + [(nr, nc)]))

	if not paths:
		raise ValueError('No path found')
	
	min_distance = min(paths.keys())

	uniqueCoords = set()
	for path in paths[min_distance]:
		uniqueCoords.update(path)

	visualiseGrid(grid, uniqueCoords)

	return min_distance, len(uniqueCoords)

def visualiseGrid(grid: list[list[str]], path: set[tuple[int, int]]) -> None:
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if (r, c) in path:
				print('\033[92mO\033[0m', end='')
			else:
				print(grid[r][c], end='')
		print()
			

solve()