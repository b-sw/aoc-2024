grid = open('input.txt').read().split('\n')
grid = [[int(cell) for cell in row] for row in grid]

def solve() -> None:
	trailheadsScore = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				trailheadsScore += dfs(i, j)

	print(trailheadsScore)

def dfs(r: int, c: int, unique=True) -> int:
	visited = set()
	stack = [(r, c)]
	score = 0

	while stack:
		row, col = stack.pop()
		visited.add((row, col))

		if grid[row][col] == 9:
			score += 1
			continue

		for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nr, nc = row + dr, col + dc
			if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]): continue
			if (nr, nc) in visited and unique: continue
			if grid[nr][nc] - grid[row][col] != 1: continue

			stack.append((nr, nc))

	return score

def solve2() -> None:
	trailheadsScore = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				trailheadsScore += dfs(i, j, False)

	print(trailheadsScore)

solve()
solve2()