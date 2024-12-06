grid = [list(row) for row in open('input.txt').read().split('\n')]
rowsCount = len(grid)
colsCount = len(grid[0])

for r in range(rowsCount):
	for c in range(colsCount):
		if grid[r][c] == '^':
			break
	else:
		continue
	break

originalPath = set()

def loop(grid, r, c, originalPath=None):
	dr, dc = -1, 0
	seen = set()

	while True:
		if originalPath is not None:
			originalPath.add((r, c))
		seen.add((r, c, dr, dc))

		if r + dr < 0 or r + dr >= rowsCount or c + dc < 0 or c + dc >= colsCount: # guard exits grid
			break

		if grid[r + dr][c + dc] == '#': # change direction
			dr, dc = dc, -dr
		else:
			r, c = r + dr, c + dc

		# part 2
		if (r, c, dr, dc) in seen:
			return True

	# part 1
	# print(len(seen))

# part 1
loop(grid, r, c, originalPath)

# part 2

count = 0

for rr, cc in originalPath:
	if grid[rr][cc] != '.':
			continue
	grid[rr][cc] = '#'

	if loop(grid, r, c):
		count += 1
	grid[rr][cc] = '.'

print(count)