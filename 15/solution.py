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
	positionCol *= 2

	for move in moves:
		print('new position', positionRow, positionCol)
		if canMove(largeGrid, (positionRow, positionCol), MOVES[move]):
			# printGrid(largeGrid)
			print('can move', positionRow, positionCol, move)
			moveRobot(largeGrid, (positionRow, positionCol), MOVES[move])

			deltaRow, deltaCol = MOVES[move]
			positionRow, positionCol = positionRow + deltaRow, positionCol + deltaCol

	boxesGPSSum = 0
	for r in range(len(largeGrid)):
		for c in range(len(largeGrid[r])):
			if largeGrid[r][c] == '[':
				boxesGPSSum += (100 * r) + c
				# rMin = min(r, len(largeGrid) - 1 - r)
				# cMin = min(c + 1, c, len(largeGrid[r]) - 1 - c, len(largeGrid[r]) - c)
				# print('r, c', r, c, '|', rMin, cMin)
				# if rMin < cMin:
				# 	boxesGPSSum += (100 * rMin) + c
				# else:
				# 	boxesGPSSum += (100 * r) + cMin

	printGrid(largeGrid)
	print(boxesGPSSum)


def enlargeGrid(grid: list[list[str]]) -> list[list[str]]:
	newTiles = { BOX: ['[', ']'], WALL: WALL + WALL, EMPTY: EMPTY + EMPTY, '@': '@.' }
	newGrid = []

	for r in range(len(grid)):
		newRow = []
		for c in range(len(grid[r])):
			newRow += newTiles[grid[r][c]]
		newGrid.append(newRow)
	
	return newGrid

def canMove(grid: list[list[str]], position: tuple, move: tuple) -> bool:
	newPosition = (position[0] + move[0], position[1] + move[1])
	if move == (-1, 0):
		return canMoveUp(grid, newPosition)
	elif move == (1, 0):
		return canMoveDown(grid, newPosition)
	elif move == (0, -1):
		return canMoveLeft(grid, newPosition)
	elif move == (0, 1):
		return canMoveRight(grid, newPosition)
	
def canMoveUp(grid: list[list[str]], position: tuple) -> bool:
	row, col = position

	if grid[row][col] == WALL:
		return False
	if grid[row][col] == EMPTY:
		return True
	if grid[row][col] == '[':
		return canMoveUp(grid, (row - 1, col)) and canMoveUp(grid, (row - 1, col + 1))
	if grid[row][col] == ']':
		return canMoveUp(grid, (row - 1, col)) and canMoveUp(grid, (row - 1, col - 1))
	
	raise ValueError("[canMoveUp] Invalid tile", grid[row][col])

def canMoveDown(grid: list[list[str]], position: tuple) -> bool:
	row, col = position

	if grid[row][col] == WALL:
		return False
	if grid[row][col] == EMPTY:
		return True
	if grid[row][col] == '[':
		return canMoveDown(grid, (row + 1, col)) and canMoveDown(grid, (row + 1, col + 1))
	if grid[row][col] == ']':
		return canMoveDown(grid, (row + 1, col)) and canMoveDown(grid, (row + 1, col - 1))
	
	raise ValueError("[canMoveDown] Invalid tile", grid[row][col])

def canMoveLeft(grid: list[list[str]], position: tuple) -> bool:
	row, col = position

	if grid[row][col] == WALL:
		return False
	if grid[row][col] == EMPTY:
		return True
	if grid[row][col] == ']':
		return canMoveLeft(grid, (row, col - 2))
	
	raise ValueError("[canMoveLeft] Invalid tile", grid[row][col])

def canMoveRight(grid: list[list[str]], position: tuple) -> bool:
	row, col = position

	if grid[row][col] == WALL:
		return False
	if grid[row][col] == EMPTY:
		return True
	if grid[row][col] == '[':
		return canMoveRight(grid, (row, col + 2))
	
	raise ValueError("[canMoveRight] Invalid tile", grid[row][col])

def moveRobot(grid: list[list[str]], position: tuple, move: tuple) -> None:
	newPosition = (position[0] + move[0], position[1] + move[1])
	if move == (-1, 0):
		moveUp(grid, newPosition)
	elif move == (1, 0):
		moveDown(grid, newPosition)
	elif move == (0, -1):
		moveLeft(grid, newPosition)
	elif move == (0, 1):
		moveRight(grid, newPosition)

def moveUp(grid: list[list[str]], position: tuple) -> None:
	row, col = position
	print('move up', row, col)

	if grid[row][col] == '[':
		moveUp(grid, (row - 1, col + 1))
		moveUp(grid, (row - 1, col))
	if grid[row][col] == ']':
		moveUp(grid, (row - 1, col))
		moveUp(grid, (row - 1, col - 1))

	grid[row][col] = grid[row + 1][col]
	grid[row + 1][col] = '.'

def moveDown(grid: list[list[str]], position: tuple) -> None:
	row, col = position
	print('move down', row, col)

	if grid[row][col] == '[':
		moveDown(grid, (row + 1, col + 1))
		moveDown(grid, (row + 1, col))
	if grid[row][col] == ']':
		moveDown(grid, (row + 1, col))
		moveDown(grid, (row + 1, col - 1))

	grid[row][col] = grid[row - 1][col]
	grid[row - 1][col] = '.'

def moveLeft(grid: list[list[str]], position: tuple) -> None:
	row, col = position
	print('move left', row, col)

	if grid[row][col] != EMPTY:
		moveLeft(grid, (row, col - 1))

	print('moving left', row, col)
	grid[row][col] = grid[row][col + 1]
	grid[row][col + 1] = '.'

def moveRight(grid: list[list[str]], position: tuple) -> None:
	row, col = position
	print('move right', row, col)

	if grid[row][col] != EMPTY:
		moveRight(grid, (row, col + 1))

	grid[row][col] = grid[row][col - 1]
	grid[row][col - 1] = '.'

solve()
solve2()