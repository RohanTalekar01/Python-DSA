graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

visited = set()
tree = []

def dfs(vertex):
    visited.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            tree.append((vertex, neighbour))
            dfs(neighbour)

dfs(0)

print("Spanning Tree:")
for edge in tree:
    print(edge)
