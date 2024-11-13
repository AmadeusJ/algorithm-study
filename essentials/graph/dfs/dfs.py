
def dfs_recursive(graph, node, visited):
    visited[node] = True
    print('visited: ', node)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)


visited = [False] * n  # n은 그래프의 노드 수


def dfs_stack(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print('visited: ', node)

            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)

graph1 = [
    [2, 3, 4],
    [5],
    [6, 7],
    [],
    [],
    [],
    [],
]

graph2 = [
    [1, 2],
	[0, 3],
	[0, 4],
	[1, 5],
	[2, 6],
	[3],
	[4]
]
