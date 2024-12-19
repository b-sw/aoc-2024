def parseInput() -> tuple[list[str], list[str]]:
	towels, designs = open('input.txt').read().split('\n\n')

	return towels.split(', '), designs.split('\n')

def solve() -> None:
	towels, designs = parseInput()

	part1Count = 0
	part2Count = 0

	for design in designs:
		applicableTowels = [towel for towel in towels if towel in design]
		cache = {}
		combinations = dfs(design, applicableTowels, cache)

		part1Count += 1 if combinations > 0 else 0
		part2Count += combinations

	print(f'Part 1: {part1Count}')
	print(f'Part 2: {part2Count}')

def dfs(design: str, towels: list[str], cache) -> int:
	if design == '':
		return 1
	
	if design in cache:
		return cache[design]

	count = 0
	for towel in towels:
		if design.startswith(towel):
			count += dfs(design[len(towel):], towels, cache)

	cache[design] = count
	return count

solve()