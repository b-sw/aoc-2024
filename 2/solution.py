def isOrdered(array) -> bool:
	return all(array[i] < array[i + 1] for i in range(len(array) - 1)) or all(array[i] > array[i + 1] for i in range(len(array) - 1))

def isDiffSafe(array) -> bool:
	return all(1 <= abs(array[i] - array[i + 1]) <= 3 for i in range(len(array) - 1))

def solve(allowSingleWrongLevel = False) -> int:
	safeReportsCount = 0

	for line in open('input.txt'):
		levels = [int(level) for level in line.split()]

		isSafe = isOrdered(levels) and isDiffSafe(levels)

		if isSafe:
			safeReportsCount += 1
		elif not allowSingleWrongLevel:
			continue
		else:
			for i in range(len(levels)):
				modifiedLevels = levels[:i] + levels[i + 1:]
				if isOrdered(modifiedLevels) and isDiffSafe(modifiedLevels):
					safeReportsCount += 1
					break


	return safeReportsCount

# part 1
print(solve())

# part 2
print(solve(True))