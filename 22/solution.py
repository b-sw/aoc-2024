secrets = [int(secret) for secret in open('input.txt').read().splitlines()]

def solve() -> None:
	vals = [secret for secret in secrets]

	for _ in range(2000):
		for i in range(len(secrets)):
			vals[i] = evolveSecret(vals[i])

	print(sum(vals))

def evolveSecret(secret: int) -> int:
	newSecret = ((secret << 6) ^ secret) & ((1 << 24) - 1)
	newSecret = ((newSecret >> 5) ^ newSecret) & ((1 << 24) - 1)
	return ((newSecret << 11) ^ newSecret) & ((1 << 24) - 1)

def solve2() -> None:
	vals = [secret for secret in secrets]
	sequences = {}

	for secret in range(len(secrets)):
		bananas = []
		recentChanges = []
		localSequences = {}
		for round in range(2000):
			ns = evolveSecret(vals[secret])
			nb = ns % 10
			
			if round > 0: recentChanges.append(nb - bananas[-1])
			if round > 3: 
				key = tuple(recentChanges[-4:])
				localSequences[key] = localSequences.get(key, nb)

			vals[secret] = ns
			bananas += [nb]

		for key in localSequences.keys():
			sequences[key] = sequences.get(key, 0) + localSequences[key]

	sequences = sorted(sequences.items(), key=lambda x: x[1], reverse=True)
	print(sequences[0][1])

solve()
solve2()