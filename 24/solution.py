def solve() -> None:
	wires, gates = parseInput()

	for gate in gates:
		output(gate, wires, gates)

	binaryValue = int(''.join([str(wires[wire]) for wire in sorted(gates, reverse=True) if wire.startswith('z')]), 2)
	print(binaryValue)

def parseInput():
	initialWiresRaw, initialGatesRaw = [part.split('\n') for part in open('input.txt').read().split('\n\n')]

	wires = {}
	for w in initialWiresRaw:
		name, value = w.split(': ')
		wires[name] = int(value)

	gates = {}
	for g in initialGatesRaw:
		operation, outputWire = g.split(' -> ')
		a, operator, b = operation.split(' ')
		gates[outputWire] = (a, b, operator)

	return wires, gates

def output(gate: str, wires: dict[str, int], gates: dict[str, tuple[str, str, str]]) -> int:
	a, b, operator = gates[gate]
	aValue = wires[a] if a in wires else output(a, wires, gates)
	bValue = wires[b] if b in wires else output(b, wires, gates)

	if operator == 'AND':
		wires[gate] = aValue & bValue
	elif operator == 'OR':
		wires[gate] = aValue | bValue
	elif operator == 'XOR':
		wires[gate] = aValue ^ bValue

	return wires[gate]

solve()