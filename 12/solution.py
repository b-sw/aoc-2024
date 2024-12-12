grid = open('input.txt').read().split('\n')
rCount, cCount = len(grid), len(grid[0])
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
		for dr, dc in dirs + [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
			nr, nc = r + dr, c + dc
			if (nr, nc) not in region:
				edgePlots.add((r, c))
				break

	vertices = set()
	for r, c in edgePlots:
		if isNonCorner((r, c), region):
			continue

		for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
			nr, nc = r + dr, c + dc
			if (nr, nc) not in region:
				vertices.add(((r + nr) / 2, (c + nc) / 2))
	
	print(len(vertices), region)
	return len(vertices)

def isNonCorner(plot: tuple[int, int], regionPlots: set[tuple[int, int]]) -> bool:
	return False
	r, c = plot
	return (r + 1, c) in regionPlots and (r - 1, c) in regionPlots or (r, c + 1) in regionPlots and (r, c - 1) in regionPlots

	
solve()
solve2()
