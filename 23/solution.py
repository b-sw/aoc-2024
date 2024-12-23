connections = open('input.txt').read().split('\n')

def constructGraph() -> dict[str, list[str]]:
	graph = {}

	for c in connections:
		a, b = c.split('-')
		graph.setdefault(a, set()).add(b)
		graph.setdefault(b, set()).add(a)

	return graph

def solve() -> None:
	graph = constructGraph()
	
	tTriplets = set()
	for v1 in graph:
		for v2 in graph[v1]:
			for v3 in graph[v2]:
				if v3 == v1 or v1 not in graph[v3]: continue
				
				if any(v.startswith('t') for v in [v1, v2, v3]):
					tTriplets.add(tuple(sorted([v1, v2, v3])))

	print(len(tTriplets))

def isClique(vertices: set[str], graph: dict[str, set[str]]) -> bool:
	for v1 in vertices:
		for v2 in vertices:
			if v1 == v2: continue
			if v2 not in graph[v1]:
				return False
	return True

def search(vertex: str, required: set[str], graph: dict[str, set[str]], cliques: set[tuple[str]]) -> None:
	key = tuple(sorted(required))
	if key in cliques: return
	cliques.add(key)

	for neighbor in graph[vertex]:
		if neighbor in required: continue
		if not (required <= graph[neighbor]): continue

		search(neighbor, required | {neighbor}, graph, cliques)

def solve2() -> None:
	graph = constructGraph()
	cliques = set()

	for v in graph:
		search(v, {v}, graph, cliques)

	print(','.join(list(max(cliques, key=len))))
	

solve()
solve2()