from functools import cache

initialStones = open('input.txt').read().split()

@cache
def count(stone: str, steps: int) -> int:
	if steps == 0:
		return 1
	if stone == 0:
		return count(1, steps - 1)
	string = str(stone)
	length = len(string)
	if length % 2 == 0:
		return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
	else:
		return count(int(stone) * 2024, steps - 1)	

def solve(n) -> None:
	print(sum([count(int(stone), n) for stone in initialStones]))

solve(25)
solve(75)