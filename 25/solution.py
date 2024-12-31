def getLocksAndKeys():
	rawGrids = open('input.txt').read().split('\n\n')

	locks = []
	keys = []

	for grid in rawGrids:
		lines = [list(line) for line in grid.split('\n')]
		rotated = list(list(row) for row in zip(*lines[::-1]))
		pinHeights = [line.count('#') - 1 for line in rotated]
		print(pinHeights)

		if rotated[0][-1] == '#':
			locks.append(pinHeights)
		else:
			keys.append(pinHeights)

	return locks, keys

def solve():
	locks, keys = getLocksAndKeys()
	
	count = 0
	for lock in locks:
		for key in keys:
			sum = [a + b for a, b in zip(lock, key)]
			count += 1 if all(sum[i] < 6 for i in range(len(sum))) else 0
	print(count)

solve()