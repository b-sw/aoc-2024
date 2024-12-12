grid = open('input.txt').read().split('\n')
rCount, cCount = len(grid), len(grid[0])
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
diagonalDirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def solve() -> None:
	regions = getRegions()
	printColoredRegions(regions)

	fencingPrice = sum([len(region) * perimeter(region) for region in regions])
	print(fencingPrice)

def perimeter(region: list[tuple[int, int]]) -> int:
	perimeter = 0
	for r, c in region:
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if (nr, nc) not in region:
				perimeter += 1
	return perimeter

def getRegions() -> list[list[tuple[int, int]]]:
	regions: list[list[tuple[int, int]]] = []
	visited = set()

	for r in range(rCount):
		for c in range(cCount):
			if (r, c) in visited:
				continue
			plots = dfs(r, c, visited)
			regions.append(plots)

	return regions
	

def dfs(r: int, c: int, visited: set[tuple[int, int]]) -> list[tuple[int, int]]:
	stack = [(r, c)]
	plots = []

	while stack:
		r, c = stack.pop()

		if (r, c) in visited:
			continue

		plots.append((r, c))
		visited.add((r, c))

		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if 0 <= nr < rCount and 0 <= nc < cCount and grid[nr][nc] == grid[r][c]:
				stack.append((nr, nc))

	return plots

def printColoredRegions(regions: list[list[tuple[int, int]]]) -> None:
	colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[98m']
	for r in range(rCount):
		for c in range(cCount):
			for i, region in enumerate(regions):
				if (r, c) in region:
					print(colors[i % len(colors)] + grid[r][c], end='')
					break
		print('\033[0m')

def solve2() -> None:
	regions = getRegions()

	bulkDiscountPrice = sum([len(region) * sides(region) for region in regions])
	print(bulkDiscountPrice)

def sides(region: list[tuple[int, int]]) -> int:
	edgePlots = set()

	for r, c in region:
		for dr, dc in dirs:
			nr, nc = r + dr, c + dc
			if (nr, nc) not in region:
				edgePlots.add((r, c))
				break

	edges = set()

	for r, c in edgePlots:
		for dr, dc in [(0, 1), (0, -1)]:
			nc = c + dc
			if (r, nc) not in region:
				edges.add((r, (c + nc) / 2))
		for dr, dc in [(1, 0), (-1, 0)]:
			nr = r + dr
			if (nr, c) not in region:
				edges.add(((r + nr) / 2, c))
	
	vertices = set()

	for r, c in edgePlots:
		for dr, dc in diagonalDirs:
			nr, nc = r + dr, c + dc
			vertices.add(((r + nr) / 2, (c + nc) / 2))

	total = 0
	for vertex in vertices:
		edgesDirs = [[(-0.5, 0), (0, -0.5)], [(0, -0.5), (0.5, 0)], [(0.5, 0), (0, 0.5)], [(0, 0.5), (-0.5, 0)]]

		vertexMatches = 0
		for edgesDir in edgesDirs:
			edgeD1, edgeD2 = edgesDir
			isCorner = True
			cornerCount = 0
			for dr, dc in [edgeD1, edgeD2]:
				nr, nc = vertex[0] + dr, vertex[1] + dc
				if (nr, nc) not in edges:
					isCorner = False
					break
			if vertex == (2.5, 2.5):
				print('vertex', vertex, isCorner, cornerCount)
			if isCorner:
				vertexMatches += 1
		total += 2 if vertexMatches > 2 else vertexMatches

	return total
	
solve()
solve2()
