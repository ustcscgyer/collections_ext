from collections import defaultdict

def topological_sort(deps):
    """
    deps = [dep1, dep2, dep3, ...]
    each dep is a tuple (prerequisite, dependence) meaning that the dep[0] is the parent node of dep[1]

    This implementation assumes acyclic graph, for cycle aware topological_sort, refer to topological_sort2.py
    """

    def dfs(v):
        visited.add(v)
        for v2 in graph[v]:
            if v2 not in visited:  dfs(v2)
        result.append(v)

    graph = defaultdict(list)
    for dep in deps:
        graph[dep[1]].append(dep[0])

    visited = set(); result = []
    for v in list(graph.keys()):
        if v not in visited: dfs(v)

    return result
