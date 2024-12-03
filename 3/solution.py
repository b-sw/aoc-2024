import re

# part 1
mulSum = 0

MUL_PATTERN = r'mul\((\d+),(\d+)\)'
DO_PATTERN = r'do\(\)'
DONT_PATTERN = r'don\'t\(\)'

for line in open('input.txt'):
	matches = re.findall(MUL_PATTERN, line)
	mulSum += sum([int(a) * int(b) for a, b in matches])

print(mulSum)


# part 2
isEnabled = True
mulSum = 0

for line in open('input.txt'):
	mulIndices = [match.start() for match in re.finditer(MUL_PATTERN, line)]
	doIndices = [match.start() for match in re.finditer(DO_PATTERN, line)]
	dontIndices = [match.start() for match in re.finditer(DONT_PATTERN, line)]

	while len(mulIndices) or len(doIndices) or len(dontIndices):
		if len(mulIndices) and (not len(doIndices) or mulIndices[0] < doIndices[0]) and (not len(dontIndices) or mulIndices[0] < dontIndices[0]):
			mulStart = mulIndices.pop(0)
			mul = re.match(MUL_PATTERN, line[mulStart:]).groups()
			mulSum += int(mul[0]) * int(mul[1]) if isEnabled else 0
		elif len(doIndices) and (not len(mulIndices) or doIndices[0] < mulIndices[0]) and (not len(dontIndices) or doIndices[0] < dontIndices[0]):
			isEnabled = True
			doIndices.pop(0)
		else:
			isEnabled = False
			dontIndices.pop(0)
	
print(mulSum)
		

