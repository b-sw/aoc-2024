def solve() -> None:
	machines = parseMachines()
	tokensSpent = 0
	tokensSpent2 = 0

	for machine in machines:
		tokensSpent += findLeastTokens(machine)
		tokensSpent2 += findLeastTokens(machine, 10000000000000)

	print(tokensSpent)
	print(tokensSpent2)

def parseMachines() -> list[tuple[int, int, int, int, int, int]]:
	machines = []

	for lines in open('input.txt').read().split('\n\n'):
		aButtonLine, bButtonLine, targetLine = lines.split('\n')
		adx, ady = parseLine(aButtonLine)
		bdx, bdy = parseLine(bButtonLine)
		targetX, targetY = parseLine(targetLine, '=')
		machines.append((adx, ady, bdx, bdy, targetX, targetY))

	return machines

def parseLine(line: str, lastDelimiter='+') -> tuple[int, int]:
	return [int(d.split(lastDelimiter)[1]) for d in line.split(': ')[1].split(', ')]

def findLeastTokens(machine: tuple[int, int, int, int, int, int], add=0) -> int:
	adx, ady, bdx, bdy, targetX, targetY = machine
	tx, ty = targetX + add, targetY + add

	i = (bdy * tx - ty * bdx) / (bdy * adx - ady * bdx)
	j = (tx - adx * i) / bdx

	if i % 1 == j % 1 == 0:
		return int(i * 3 + j)
	else:
		return 0

	
solve()