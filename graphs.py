def bfs(graph, node):
    # Review this function, there's a problem
    from collections import deque
    
    visited = set()
    queue = deque()
    visited.add(node)
    queue.append(node)
    while len(queue) > 0:
        v = queue.popleft()
        print(v, end=' ')
        for adj in graph[v]:
            if adj not in visited:
                visited.add(adj)
                queue.append(node)

def dfs(graph, node, visited=set()):
    visited.add(node)
    print(node, end=' ')
    for adj in graph[node]:
        if adj not in visited:
            dfs(graph, adj, visited)

def dijkstra(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0
    path = []

    for _ in range(n):
        next = find_min_util(distances, path)
        path.append(next)
        for adj, dist in enumerate(graph[next]):
            if dist != 0 and adj not in path and distances[adj] > distances[next] + dist:
                distances[adj] = distances[next] + dist

    for elt in path:
        print(elt, end=' ')
    
def prim(graph, n):
    mst = set()
    keys = [float('inf')] * n
    parent = [None] * n

    keys[0] = 0
    parent[0] = -1

    for _ in range(n):
        next = find_min_util(keys, mst)
        mst.add(next)
        for adj, dist in enumerate(graph[next]):
            if dist != 0 and adj not in mst and dist < keys[adj]:
                keys[adj] = dist
                parent[adj] = next

    for elt in mst:
        print(elt, end=' ')

def find_min_util(vals, st):        
    min_val = float('inf')
    for node, val in enumerate(vals):
        if node not in st and val < min_val:
            min_val = val
            min_node = node
    return min_node

graph = {
    1: [2],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3, 5],
    5: [4],
    }

weighted = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

print("bfs output:")
bfs(graph, 4)
print("\ndfs output:")
dfs(graph, 5)
print("\ndijkstra output:")
dijkstra(weighted, 0, len(weighted))
print("prim's output:")
prim(weighted, len(weighted))
