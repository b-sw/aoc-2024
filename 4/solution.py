import time
import os
clear = lambda: os.system('clear')
# part 1

grid = [line.strip() for line in open('input.txt')]
letters = ['X', 'M', 'A', 'S']
lettersReversed = ['S', 'A', 'M', 'X']
paths = set()

def printInputWithPaths(path: set[tuple[tuple[int, int]]]) -> None:
    clear()
    flattenedCoords = set()

    for p in path:
        for coords in p:
            flattenedCoords.add(coords)

    for rowIndex, row in enumerate(grid):
        for colIndex, node in enumerate(row):
            if (rowIndex, colIndex) in flattenedCoords:
                print('\033[1;92m' + node + '\033[0m', end='')
            else:
                print(node, end='')
        print()
    time.sleep(0.2)

def findPaths(rowIndex: int, colIndex: int, dir: tuple[int, int], remaining: set[str], path: list[tuple[int, int]]) -> None:    
    char = grid[rowIndex][colIndex]
    if remaining[0] != char:
        return

    remaining.remove(char)

    if not remaining:
        global paths
        paths.add(tuple(sorted(path + [(rowIndex, colIndex)])))
        # printInputWithPaths(paths)
        return

    dx, dy = dir
    newRow, newCol = rowIndex + dx, colIndex + dy
    if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
        return
    findPaths(newRow, newCol, dir, remaining.copy(), path + [(rowIndex, colIndex)])

for rowIndex, row in enumerate(grid):
    for colIndex, node in enumerate(row):
        if node not in letters:
            continue
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            findPaths(rowIndex, colIndex, (dx, dy), letters.copy(), [])
            findPaths(rowIndex, colIndex, (dx, dy), lettersReversed.copy(), [])

print(len(paths))

xMasPaths = 0

# part 2
for rowIndex, row in enumerate(grid):
    for colIndex, node in enumerate(row):
        if node != 'A':
            continue

        if rowIndex == 0 or rowIndex == len(grid) - 1 or colIndex == 0 or colIndex == len(grid[0]) - 1:
            continue

        diagonalA, diagonalB = [(1, 1), (-1, -1)], [(1, -1), (-1, 1)]
        diagonalAChars = set([grid[rowIndex + dx][colIndex + dy] for dx, dy in diagonalA])
        diagonalBChars = set([grid[rowIndex + dx][colIndex + dy] for dx, dy in diagonalB])

        if 'M' in diagonalAChars and 'S' in diagonalAChars and 'M' in diagonalBChars and 'S' in diagonalBChars:
            xMasPaths += 1

print(xMasPaths)
