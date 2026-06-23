from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': [],
    'E': []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs('A')

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def shortest_path(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        vertex, path = queue.popleft()

        if vertex == goal:
            return path

        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

print(shortest_path('A', 'D'))

from collections import deque

maze = [
    ['S', '.', '.'],
    ['#', '#', '.'],
    ['.', '.', 'F']
]

rows = len(maze)
cols = len(maze[0])

queue = deque([(0, 0)])
visited = {(0, 0)}

moves = [(1,0), (-1,0), (0,1), (0,-1)]

while queue:
    x, y = queue.popleft()

    if maze[x][y] == 'F':
        print("Фініш знайдено!")
        break

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if (0 <= nx < rows and
            0 <= ny < cols and
            maze[nx][ny] != '#' and
            (nx, ny) not in visited):

            visited.add((nx, ny))
            queue.append((nx, ny))