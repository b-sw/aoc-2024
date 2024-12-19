import heapq

W, H = 71, 71

bytes = [line.split(',') for line in open('input.txt').read().splitlines()]

def solve() -> None:
	grid = corruptGrid(W, H, bytes[:1024])
	target = (W - 1, H - 1)
	print(dijkstraSearch((0, 0), target, grid))

	for b in range(1024, len(bytes)):
		print('b', b)
		grid = corruptGrid(W, H, bytes[:b])
		score = dijkstraSearch((0, 0), target, grid)

		if not score:
			print('No path found', b)
			break

def dijkstraSearch(start: tuple[int, int], target: tuple[int, int], grid: list[list[str]]) -> int:
	distances = { start: (0, []) }
	pq = [(0, start, [start])]
	
	while pq:
		d, pos, path = heapq.heappop(pq)

		if pos == target:
			# printGrid(grid, path)
			return d
		
		r, c = pos
		for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nr, nc = r + dr, c + dc

			if nr < 0 or nr >= H or nc < 0 or nc >= W or grid[nr][nc] == '#' or (nr, nc) in path:
				continue

			newDistance = d + 1
			neighbor = (nr, nc)

			if neighbor not in distances or newDistance < distances[neighbor][0]:
				distances[neighbor] = (newDistance, path + [neighbor])
				heapq.heappush(pq, (newDistance, neighbor, path + [neighbor]))

	return None

def printGrid(grid: list[list[str]], path: list[tuple[int, int]]) -> None:
	for r in range(H):
		for c in range(W):
			if (r, c) in path:
				print('\033[92m' + 'O' + '\033[0m', end=' ')
			else:
				print(grid[r][c], end=' ')
		print()

def corruptGrid(width: int, height: int, bytes: list) -> None:
	grid = [list('.' * width) for _ in range(height)]
	for byte in bytes:
		x, y = int(byte[0]), int(byte[1])
		grid[y][x] = '#'

	return grid

solve()