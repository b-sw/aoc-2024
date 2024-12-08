grid = [list(line) for line in open('input.txt').read().split('\n')]

rowsCount = len(grid)
colsCount = len(grid[0])

antennas = {}
antinodesCoords = set()

for r in range(rowsCount):
	for c in range(colsCount):
		antenna = grid[r][c]
		if antenna != '.':
			antennas[antenna] = antennas.get(antenna, []) + [(r, c)]


def solve() -> None:
	for _, coords in antennas.items():
		createAntennaAntinodes(coords, getAntinodes)

	printAntinodes()
	print(len(antinodesCoords))

def createAntennaAntinodes(coords: list[tuple[int, int]], getAntinodesFn) -> None:
	for i, (r, c) in enumerate(coords):
		otherAntennasCoords = coords[i + 1:]
		for (rp, cp) in otherAntennasCoords:
			antinodes = getAntinodesFn((r, c), (rp, cp))
			for antinode in antinodes:
				global antinodesCoords
				antinodesCoords.add(antinode)
			

def getAntinodes(coordsA: tuple[int, int], coordsB: tuple[int, int]) -> list[tuple[int, int]]:
	x, y = coordsA
	xp, yp = coordsB

	antinodes = []

	for antinode in [(x + (x - xp), y + (y - yp)), (xp + (xp - x), yp + (yp - y))]:
		if isWithinGrid(antinode):
			antinodes.append(antinode)

	return antinodes

def isWithinGrid(coords: tuple[int, int]) -> bool:
	x, y = coords
	return x >= 0 and x < rowsCount and y >= 0 and y < colsCount

def printAntinodes() -> None:
	for r in range(rowsCount):
		for c in range(colsCount):
			if (r ,c) in antinodesCoords:
				print('\033[1;92m' + '#' + '\033[0m', end='')
			else:
				print(grid[r][c], end='')
		print()

solve()

# part 2 

def solve2() -> None:
	for _, coords in antennas.items():
		createAntennaAntinodes(coords, getAntinodes2)

	printAntinodes()
	print(len(antinodesCoords))


def getAntinodes2(coordsA: tuple[int, int], coordsB: tuple[int, int]) -> list[tuple[int, int]]:
	return [coordsA, coordsB] + interpolateCoords(coordsA, coordsB) + interpolateCoords(coordsB, coordsA)

def interpolateCoords(coordsA: tuple[int, int], coordsB: tuple[int, int]) -> list[tuple[int, int]]:
	x, y = coordsA
	xp, yp = coordsB
	antinodes = []

	ax, ay = x + (x - xp), y + (y - yp)
	i = 1
	while isWithinGrid((ax, ay)):
		antinodes.append((ax, ay))
		i += 1
		ax, ay = x + i * (x - xp), y + i * (y - yp)

	return antinodes

solve2()