MOVES = { '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1) }
BOX, WALL, EMPTY = 'O', '#', '.'

def solve() -> None:
	grid, moves, position = parseInput()
	positionRow, positionCol = position

	for move in moves:
		deltaRow, deltaCol = MOVES[move]
		newRow, newCol = positionRow + deltaRow, positionCol + deltaCol

		tmpRow, tmpCol = newRow, newCol
		while grid[tmpRow][tmpCol] == BOX:
			tmpRow += deltaRow
			tmpCol += deltaCol

		if grid[tmpRow][tmpCol] != EMPTY:
			continue

		grid[positionRow][positionCol] = EMPTY
		grid[tmpRow][tmpCol] = BOX
		grid[newRow][newCol] = '@'
		positionRow, positionCol = newRow, newCol

	printGrid(grid)
	print(sumBoxesGPS(grid))

def parseInput() -> tuple:
	gridRaw, movesRaw = open('input.txt').read().split('\n\n')
	moves = ''.join(movesRaw.split('\n'))
	grid = [list(row) for row in gridRaw.split('\n')]
	
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == '@':
				start = (r, c)
				break
		else:
			continue
		break

	return grid, moves, start

def printGrid(grid: list) -> None:
	for row in grid:
		print(''.join(row))

def sumBoxesGPS(grid: list) -> int:
	boxesGPSSum = 0

	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == BOX:
				boxesGPSSum += (100 * r) + c
			
	return boxesGPSSum

def solve2() -> None:
	grid, moves, position = parseInput()
	largeGrid = enlargeGrid(grid)
	positionRow, positionCol = position

	for move in moves:
		if canMove(largeGrid, (positionRow, positionCol), MOVES[move]):
			printGrid(largeGrid)
			print('can move', positionRow, positionCol, move)
			moveRobot(largeGrid, (positionRow, positionCol), MOVES[move])

		deltaRow, deltaCol = MOVES[move]
		positionRow, positionCol = positionRow + deltaRow, positionCol + deltaCol

	printGrid(largeGrid)


def enlargeGrid(grid: list[list[str]]) -> list[list[str]]:
	newTiles = { BOX: ['[', ']'], WALL: WALL + WALL, EMPTY: EMPTY + EMPTY, '@': '@.' }
	newGrid = []

	for r in range(len(grid)):
		newRow = []
		for c in range(len(grid[r])):
			newRow += newTiles[grid[r][c]]
		newGrid.append(newRow)
	
	return newGrid

def canMove(grid: list[list[str]], position: tuple[int, int], move: tuple[int, int]) -> bool:
	positionRow, positionCol = position
	deltaRow, deltaCol = move
	newRow, newCol = positionRow + deltaRow, positionCol + deltaCol
	
	if grid[newRow][newCol] == EMPTY:
		return True
	if grid[newRow][newCol] == WALL:
		return False
	if grid[newRow][newCol] == '[':
		return canMove(grid, (newRow, newCol), move) and canMove(grid, (newRow, newCol + deltaCol), move)
	if grid[newRow][newCol] == ']':
		return canMove(grid, (newRow, newCol), move) and canMove(grid, (newRow, newCol - deltaCol), move)
	

	raise Exception('Invalid tile', grid[newRow][newCol])

def moveRobot(grid: list[list[str]], position: tuple[int, int], move: tuple[int, int]) -> None:
	positionRow, positionCol = position
	deltaRow, deltaCol = move
	newRow, newCol = positionRow + deltaRow, positionCol + deltaCol
	oldTile = grid[positionRow][positionCol]

	if grid[newRow][newCol] == EMPTY:
		grid[positionRow][positionCol] = EMPTY
		grid[newRow][newCol] = oldTile
		return
	if grid[newRow][newCol] == '[':
		moveRobot(grid, (newRow, newCol), move)
		moveRobot(grid, (newRow, newCol + deltaCol), move)
		grid[positionRow][positionCol] = EMPTY
		grid[newRow][newCol] = oldTile
		return
	if grid[newRow][newCol] == ']':
		moveRobot(grid, (newRow, newCol), move)
		moveRobot(grid, (newRow, newCol - deltaCol), move)
		grid[positionRow][positionCol] = EMPTY
		grid[newRow][newCol] = oldTile
		return

	raise Exception('Invalid tile', grid[newRow][newCol])


solve()
solve2()