from collections import defaultdict

def topological_sort2(deps):
    """
    deps = [dep1, dep2, dep3, ...]
    each dep is a tuple (prerequisite, dependence) meaning that the dep[0] is the parent node of dep[1]

    This implementation is similar to topological_sort.py, but will detect cycles and return []
    """

    def dfs(v):
        visited.add(v)
        stack.add(v)
        for v2 in graph[v]:
            assert v2 not in stack
            if v2 not in visited:  dfs(v2)
        stack.remove(v)
        result.append(v)

    graph = defaultdict(list)
    for dep in deps:
        graph[dep[1]].append(dep[0])

    visited = set(); result = []; stack = set()
    for v in list(graph.keys()):
        try:
            if v not in visited: dfs(v)
        except:
            return []

    return result
