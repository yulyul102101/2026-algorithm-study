from collections import deque

def bfs_shortest_path(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])

    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, [(start_x, start_y)])])

    while queue:
        x, y, path = queue.popleft()

        if x == end_x and y == end_y:
            return path

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and graph[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))

    return -1


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

print(len(bfs_shortest_path(0, 0, n - 1, m - 1, maze)))
