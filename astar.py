import heapq
# This program finds shortest path using A* search algorithm
# Manhattan distance
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    visited = set()
    parent = {}
    cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)
        visited.add(current)

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx = current[0] + dx
            ny = current[1] + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0 and (nx, ny) not in visited:

                    new_cost = cost[current] + 1

                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost
                        f = new_cost + h((nx, ny), goal)

                        heapq.heappush(pq, (f, (nx, ny)))
                        parent[(nx, ny)] = current

    print("Path not found using A*")



try:
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")

    i = 0
    r, c = map(int, lines[i].split())
    i += 1

    grid = []
    for _ in range(r):
        grid.append(list(map(int, lines[i].split())))
        i += 1

    sr, sc = map(int, lines[i].split())
    i += 1

    tr, tc = map(int, lines[i].split())

    astar(grid, (sr, sc), (tr, tc))

except:
    print("Input format error")
