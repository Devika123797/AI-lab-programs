import heapq

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f  

def heuristic(a, b):
    return abs(ord(a) - ord(b))

def a_star(start, goal, graph):
    open_list = []
    closed_list = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.name == goal:
            path = []
            total_cost = current_node.g  
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1], total_cost 

        closed_list.add(current_node.name)

        for neighbor, cost in graph.get(current_node.name, []):
            if neighbor in closed_list:
                continue
            
            g = current_node.g + cost
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g, h)
            neighbor_node.parent = current_node

            if not any(node.name == neighbor and node.f <= neighbor_node.f for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None, 0  
graph = {
    'a': [('b', 1), ('c', 4)],
    'b': [('a', 1), ('d', 2), ('e', 5)],
    'c': [('a', 4), ('f', 1)],
    'd': [('b', 2), ('g', 2)],
    'e': [('b', 5)],
    'f': [('c', 1), ('g', 3)],
    'g': [('f', 3), ('d', 0)]
}

start = 'a'
goal = 'g'
path, total_cost = a_star(start, goal, graph)

print("Path from start node to goal:", path)
print("Total cost of the path:", total_cost)
