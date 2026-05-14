import heapq

class Node:
    def __init__(self, name, g, h, parent=None):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


def a_star(graph, start, goal, heuristic):
    open_list = []
    closed_list = set()

    start_node = Node(start, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            return reconstruct_path(current)

        closed_list.add(current.name)

        for neighbor, cost in graph[current.name]:
            if neighbor in closed_list:
                continue

            g = current.g + cost
            h = heuristic[neighbor]
            neighbor_node = Node(neighbor, g, h, current)

            heapq.heappush(open_list, neighbor_node)

    return None


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]


# Example Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 6, 'B': 4, 'C': 4,
    'D': 2, 'E': 2, 'F': 1,
    'G': 0
}

path = a_star(graph, 'A', 'G', heuristic)
print("Path:", path)