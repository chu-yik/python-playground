'''
from:
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
'''
from collections import deque

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)
    return path

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            path.append(v)
            queue.extend(graph[v] - visited)
    return path

print(dfs(graph, 'A'))
print(bfs(graph, 'A'))

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next is goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (v, path) = queue.popleft()
        for next in graph[v] - set(path):
            if next is goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

print(list(dfs_path(graph, 'F', 'A')))
print(list(bfs_path(graph, 'A', 'F'))) # BFS returns shortest path first
# print(bfs_path(graph, 'A', 'E'))
    

