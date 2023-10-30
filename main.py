#make all important imports
import heapq


# this class will be used to represent the district on the graph
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
    
    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].add_neighbor(node2, weight)
        self.nodes[node2].add_neighbor(node1, weight)

    def dijkstra(self, start):
        distances = {name: float('inf') for name in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node].neighbors.items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def shortest_path(self, start, end):
        distances = self.dijkstra(start)
        path = [end]
        path_cost = 0  # Initialize the path cost
        while end != start:
            for neighbor, weight in self.nodes[end].neighbors.items():
                if distances[end] == distances[neighbor] + weight:
                    path.append(neighbor)
                    path_cost += weight
                    end = neighbor
                    break
        path = list(reversed(path))
        return path, path_cost

# Instantiate the graph and add nodes and edges 
g = Graph()
g.add_node("Mchinji")
g.add_node("Kasungu")
g.add_node("Dowa")
g.add_node("Lilongwe")
g.add_node("Dedza")
g.add_node("Ntcheu")
g.add_node("Nkhotakota")
g.add_node("Salima")
g.add_node("Ntchisi")


g.add_edge("Mchinji", "Kasungu", 141)
g.add_edge("Mchinji", "Lilongwe", 109)
g.add_edge("Kasungu", "Dowa", 117)
g.add_edge("Kasungu", "Ntchisi", 66)
g.add_edge("Dowa", "Lilongwe", 55)

g.add_edge("Dowa", "Ntchisi", 38)
g.add_edge("Nkhotakota", "Ntchisi", 66)
g.add_edge("Dowa", "Salima", 67)
g.add_edge("Salima", "Dedza", 96)
g.add_edge("Dedza", "Ntcheu", 74)
g.add_edge("Dedza", "Lilongwe", 92)



# Prompt the for start and end points
start_point = input("Enter the starting point: ")
end_point = input("Enter the destination point: ")

# Check if the input points exist in the graph
if start_point in g.nodes and end_point in g.nodes:
    shortest_path, path_cost = g.shortest_path(start_point, end_point)
    if shortest_path:
        print("Shortest path:", shortest_path)
        print("total distance of the path (path cost):", path_cost)
    else:
        print("No path found.")
else:
    print("Start or destination point not found in the graph.")
