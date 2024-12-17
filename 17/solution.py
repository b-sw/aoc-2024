A, B, C = 'A', 'B', 'C'

def parseInput():
	registersRaw, instructionsRaw = open("input.txt").read().split("\n\n")
	registers = {}
	instructions = []

	for rRaw in registersRaw.splitlines():
		_, rName, rValue = rRaw.split(' ')
		registers[rName[:-1]] = int(rValue)

	instructions = [int(i) for i in instructionsRaw.split(' ')[1].split(',')]

	return registers, instructions

def solve() -> None:
	registers, inputValues = parseInput()
	
	i = 0

	while i < len(inputValues):
		i = executeInstruction(inputValues[i], inputValues[i + 1], registers, i)
			

def executeInstruction(opcode: int, operand: int, registers: map, currentPointer: int) -> int:
	if opcode == 0: # adv
		registers[A] = registers[A] // 2 ** comboOperand(operand, registers)
	elif opcode == 1: # bxl
		registers[B] = registers[B] ^ operand
	elif opcode == 2: # bst
		registers[B] = comboOperand(operand, registers) % 8
	elif opcode == 3: # jnz
		if registers[A] == 0: return currentPointer + 2
		return operand
		# return 0
	elif opcode == 4: # bxc
		registers[B] = registers[B] ^ registers[C]
	elif opcode == 5: # out
		print(comboOperand(operand, registers) % 8, end=',')
	elif opcode == 6: # bdv
		registers[B] = registers[A] // 2 ** comboOperand(operand, registers)
	elif opcode == 7: # cdv
		registers[C] = registers[A] // 2 ** comboOperand(operand, registers)

	return currentPointer + 2
		

def comboOperand(operand: int, registers: map) -> int:
	if operand < 4: return operand
	if operand == 4: return registers[A]
	if operand == 5: return registers[B]
	if operand == 6: return registers[C]

	raise ValueError("Invalid operand", operand)

solve()