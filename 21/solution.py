numericKeypad = [
	['7', '8', '9'],
	['4', '5', '6'],
	['1', '2', '3'],
	[None, '0', 'A']
]

directionalKeypad = [
	[None, '^', 'A'],
	['<', 'v', '>']
]

def solve() -> None:
	a = shortestSequence(numericKeypad, '029A')
	print('a is', a)
	b = shortestSequence(directionalKeypad, '<A^A>^^AvvvA')
	print('b is', b)
	c = shortestSequence(directionalKeypad, '<A^A^>^AvvvA')
	print('c is', c)
	# d = shortestSequence(directionalKeypad, c)
	# print('d is', d)

def shortestSequence(keypad: list[list[str]], keys: str) -> str:
	r, c = findRC(keypad, 'A')
	seq = []
	for char in keys:
		nr, nc = findRC(keypad, char)
		pathToChar = findPath(keypad, (r, c), (nr, nc))
		seq.append(pathToChar + 'A')
		r, c = nr, nc
	return ''.join(seq)

def findRC(keypad: list[list[str]], key: str) -> tuple[int, int]:
	for r in range(len(keypad)):
		for c in range(len(keypad[r])):
			if keypad[r][c] == key:
				return r, c
			
def findPath(keypad: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> str:
	r, c = start
	er, ec = end
	path = []
	while r != er or c != ec:
		if r < er:
			path.append('v')
			r += 1
		elif r > er:
			path.append('^')
			r -= 1
		if c < ec:
			path.append('>')
			c += 1
		elif c > ec:
			path.append('<')
			c -= 1
	return ''.join(path)

solve()