diskMap = list(open('input.txt').read())


def solve() -> None:
	blocks = diskMapToBlocks()

	i, sum = 0, 0
	while i < len(blocks):
		if blocks[i] == '.':
			while blocks[-1] == '.':
				blocks.pop()
			blocks[i] = blocks[-1]
			blocks.pop()
		sum += i * int(blocks[i])
		i += 1
	
	print(sum)

def diskMapToBlocks() -> list:
	blocks = []
	for file in range(len(diskMap)):
		for _ in range(int(diskMap[file])):
			blocks.append((('.' if file % 2 == 1 else str(file // 2))))
	return blocks

solve()

def solve2() -> None:
	files = {} # fileId -> [position, length]
	blanks = [] # [position, length][]
	fileId = 0
	position = 0

	for i, char in enumerate(diskMap):
		xIndex = int(char)

		if i % 2 == 0:
			if xIndex == 0: raise Exception('Unexpected 0')
			files[fileId] = (position, xIndex)
			fileId += 1
		else:
			if xIndex != 0:
				blanks.append((position, xIndex))

		position += xIndex

	while fileId > 0:
		fileId -= 1
		filePosition, fileSize = files[fileId]

		for i, (blankStart, blankSize) in enumerate(blanks):
			if blankStart >= filePosition: 
				blanks = blanks[:i]
				break

			if fileSize <= blankSize:
				files[fileId] = (blankStart, fileSize)

				if fileSize == blankSize:
					blanks.pop(i)
				else:
					blanks[i] = (blankStart + fileSize, blankSize - fileSize)
				break
	
	total = 0
	for fileId, (filePosition, fileSize) in files.items():
		for xIndex in range(filePosition, filePosition + fileSize):
			total += fileId * xIndex
	print(total)

solve2()