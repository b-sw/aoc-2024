lefts, rights = [], []
totalDistance = 0

# part 1
for line in open('input.txt'):
	left, right = line.split()
	lefts.append(int(left))
	rights.append(int(right))

lefts.sort()
rights.sort()

for i in range(len(lefts)):
	totalDistance += abs(lefts[i] - rights[i])

print(totalDistance)

# part 2
rightsCounts = {}
for right in rights:
	rightsCounts[right] = rightsCounts.get(right, 0) + 1

similarityScore = sum([left * rightsCounts.get(left, 0) for left in lefts])

print(similarityScore)