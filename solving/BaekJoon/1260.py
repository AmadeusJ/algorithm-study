"""
https://www.acmicpc.net/problem/1260
"""
from collections import deque, defaultdict      #XXX

n, m, start = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)] # XXX

graph = defaultdict(list)       # XXX : 간선의 정보가 주어졌기 때문에 직접 그래프를 만들어줘야함

for u, v in edges:      # XXX
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def dfs_stack(graph, start):
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True

    while stack:
        neighbor = stack.pop()
        print(neighbor, end=' ')
        for neighbor in reversed(graph[neighbor]):    # 뒤에서 부터 봐야하니까 'reversed'
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[neighbor] = True


def bfs(graph, start):
    visited = [False] * (n + 1)
    
    queue = deque([start])  # XXX
    visited[start] = True   # XXX

    while queue:
        neighbor = queue.popleft()
        print(neighbor, end=' ')
        for neighbor in graph[neighbor]:    # XXX
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


visited = [False] * (n + 1)

dfs(graph, start, visited)
bfs(graph, start)