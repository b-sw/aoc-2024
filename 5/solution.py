rulesRaw, printsRaw = open('input.txt').read().split('\n\n')

rules = [rule.split('|') for rule in rulesRaw.split('\n')]
prints = [print.split(',') for print in printsRaw.split('\n')]
orderingRules = {}
for rule in rules:
	orderingRules[rule[0]] = orderingRules.get(rule[0], []) + [rule[1]]

# part 1

validPrintsIndices = []

for pagesPrintIndex, pagesPrint in enumerate(prints):
	previousPages = set()
	isValid = True

	for page in pagesPrint:
		if page in orderingRules and any([previousPage in orderingRules[page] for previousPage in previousPages]):
			isValid = False
			break

		previousPages.add(page)

	if isValid:
		validPrintsIndices.append(pagesPrintIndex)

validPrints = [prints[i] for i in validPrintsIndices]
middleIndicesSum = sum([int(pagesPrint[len(pagesPrint) // 2]) for pagesPrint in validPrints])
print(middleIndicesSum)

# part 2
from functools import cmp_to_key

invalidPrints = [prints[i] for i in range(len(prints)) if i not in validPrintsIndices]

def customComparator(pageA: str, pageB: str) -> int:
	return (-1 if pageB in orderingRules.get(pageA, []) else 0) + (1 if pageA in orderingRules.get(pageB, []) else 0)

sortedInvalidPrints = [sorted(invalidPrint, key=cmp_to_key(customComparator)) for invalidPrint in invalidPrints]

middleIndicesSum = sum([int(pagesPrint[len(pagesPrint) // 2]) for pagesPrint in sortedInvalidPrints])
print(middleIndicesSum)