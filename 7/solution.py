lines = open('input.txt').read().split('\n')

def solve() -> None:
	sum = 0
	sum2 = 0

	for line in lines:
		value, numbersRaw = line.split(': ')
		numbers = [int(number) for number in numbersRaw.split(' ')]
		sum += int(value) if dfs(int(value), numbers) else 0
		sum2 += int(value) if dfs2(0, int(value), numbers) else 0

	print(sum)
	print(sum2)


def dfs(target: int, nums: list[int]) -> bool:
	if len(nums) == 1:
		return target == nums[0]
	
	return target % nums[-1] == 0 and dfs(target // nums[-1], nums[:-1]) or target > nums[-1] and dfs(target - nums[-1], nums[:-1])

def dfs2(current: int, target: int, nums: list[int]) -> bool:
	if len(nums) == 0:
		return current == target
	
	if current > target:
		return False
	
	return dfs2(current * nums[0], target, nums[1:]) or dfs2(current + nums[0], target, nums[1:]) or dfs2(int(str(current) + str(nums[0])), target, nums[1:])

solve()