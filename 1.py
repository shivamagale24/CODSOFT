
# Undirected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ---------------- DFS using Recursion ----------------

visited_dfs = []

def dfs(node):

    if node not in visited_dfs:

        print(node, end=' ')
        visited_dfs.append(node)

        for i in graph[node]:
            dfs(i)


# ---------------- BFS using Queue (NO recursion) ----------------

visited_bfs = []
queue = ['A']

def bfs():

    while queue:

        node = queue.pop(0)

        if node not in visited_bfs:

            print(node, end=' ')
            visited_bfs.append(node)

            for i in graph[node]:
                queue.append(i)


# ---------------- Start DFS ----------------

print("DFS Traversal:")
dfs('A')

print("\n")

# ---------------- Start BFS ----------------

print("BFS Traversal:")
bfs()
