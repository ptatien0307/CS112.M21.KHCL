from sys import stdin

INF = float('inf')

def input_data():
    global vertices, edges
    global start, finish

    vertices, edges, start, finish = map(int, stdin.readline().split())

    global a  # adjacent matrix
    a = [[INF for col in range(vertices + 1)] for row in range(vertices + 1)]
    for i in range(edges):
        u, v, len = map(int, stdin.readline().split())
        a[u][v] = len
        a[v][u] = len


def init():
    # a vertex is visited or not
    global visited
    visited = [False for _ in range(vertices + 1)]

    # d[v] is the minimum distance from start to v
    global d  # distance
    d = [INF for _ in range(vertices + 1)]
    d[start] = 0

    # trace[v] = u means that u is followed by v, or we have to travel from u to v
    # tracing for output path
    global trace
    trace = [0 for _ in range(vertices + 1)]


def min_distance():
    min_d = INF
    min_index = 0

    for v in range(1, vertices + 1):
        if not visited[v]:
            if d[v] < min_d:
                min_d = d[v]
                min_index = v
    return min_index


def dijkstra():
    init()

    while True:
        # find the vertex which has minimum distance from start for next travel from it
        u = min_distance()

        # cannot travel anymore or reach the finish
        if u == 0 or u == finish: break

        visited[u] = True

        for v in range(1, vertices + 1):
            if not visited[v]:
                if d[u] + a[u][v] < d[v]:
                    d[v] = d[u] + a[u][v]  # update the minimum distance
                    trace[v] = u  # for output path

if __name__ == '__main__':
    input_data()
    dijkstra()
    if d[finish] == INF:
        print(-1)
    else:
        print(d[finish])