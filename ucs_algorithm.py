import heapq
def uniform_cost_search(graph ,start, goal):
    priority_queue = [(0,start,[])]
    visited =set()
    while priority_queue:
        cost ,node,path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == goal:
            return cost,path
        for neighbor, edge_cost in graph.get(node,[]):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path))
    return float ('inf'),[]
graph={
    "A":[("B",4),("C",3)],
    "B":[("F",5),("E",12)],
    "C":[("E",10),("D",7)],
    "D":[("E",2)],
    "E":[("Z",5)],
    "F":[("Z",16)]
}
start_node="A"
goal_node="Z"
cost ,path =uniform_cost_search(graph,start_node,goal_node)
print(f"least_cost path from {start_node}to {goal_node}: {path}")
print(f"Total_cost:{cost}")
