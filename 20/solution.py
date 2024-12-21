from functools import cache

grid = [list(line) for line in open('input.txt').read().splitlines()]

def solve() -> None:
	dists = bfsFill(grid)
	count = find(dists)
	print(count)
	count2 = find2(dists)
	print(count2)

def findStartEnd(grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 'S':
				start = (row, col)
			elif grid[row][col] == 'E':
				end = (row, col)
	return start, end

def bfsFill(grid: list[list[str]]) -> int:
	start, _ = findStartEnd(grid)
	dists = [[-1]*len(grid[0]) for _ in range(len(grid))]
	dists[start[0]][start[1]] = 0
	stack = [start]

	while stack:
		r,c = stack.pop()

		for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
			if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
				continue

			if grid[nr][nc] == '#':
				continue

			if dists[nr][nc] != -1:
				continue
			
			dists[nr][nc] = dists[r][c] + 1
			stack.append((nr, nc))

	return dists

def printPath(dists: list[list[int]]) -> None:
	for row in dists:
		print(*row, sep='\t')

def find(dists: list[list[int]]) -> int:
	count = 0

	for r in range(len(dists)):
		for c in range(len(dists[0])):
			if dists[r][c] == -1: 
				continue

			for nr, nc in [(r + 2, c), (r - 2, c), (r, c + 2), (r, c - 2), (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)]:
				if nr < 0 or nc < 0 or nr >= len(dists) or nc >= len(dists[0]): 
					continue
				if dists[nr][nc] == -1: 
					continue
				if dists[r][c] < dists[nr][nc]: 
					continue
				
				if dists[r][c] - dists[nr][nc] >= 102:
					count += 1
	
	return count

def find2(dists: list[list[int]]) -> int:
	count = 0

	for r in range(len(dists)):
		for c in range(len(dists[0])):
			if dists[r][c] == -1: 
				continue

			for radius in range(2, 21):
				for dr in range(radius + 1):
					dc = radius - dr

					for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
						if nr < 0 or nc < 0 or nr >= len(dists) or nc >= len(dists[0]): 
							continue
						if dists[nr][nc] == -1: 
							continue
						
						if dists[r][c] - dists[nr][nc] >= 100 + radius:
							count += 1

	return count

solve()