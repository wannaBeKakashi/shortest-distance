#make all important imports
import heapq


# this class will be used to represent the district on the graph
class District:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
    
    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

#this class is for creating the graph
class Graph:
    def __init__(self):
        self.districts = {}

    def add_district(self, name):
        district = District(name)
        self.districts[name] = district

    def add_edge(self, district1, district2, weight):
        self.districts[district1].add_neighbor(district2, weight)
        self.districts[district2].add_neighbor(district1, weight)

class Main:
    def __init__(self):
        # Instantiate the graph and add nodes and edges
        self.graph = Graph()
        self.graph.add_district("Mchinji")
        self.graph.add_district("Kasungu")
        self.graph.add_district("Dowa")
        self.graph.add_district("Lilongwe")
        self.graph.add_district("Dedza")
        self.graph.add_district("Ntcheu")
        self.graph.add_district("Nkhotakota")
        self.graph.add_district("Salima")
        self.graph.add_district("Ntchisi")

        self.graph.add_edge("Mchinji", "Kasungu", 141)
        self.graph.add_edge("Mchinji", "Lilongwe", 109)
        self.graph.add_edge("Kasungu", "Dowa", 117)
        self.graph.add_edge("Kasungu", "Ntchisi", 66)
        self.graph.add_edge("Dowa", "Lilongwe", 55)
        self.graph.add_edge("Dowa", "Ntchisi", 38)
        self.graph.add_edge("Nkhotakota", "Ntchisi", 66)
        self.graph.add_edge("Nkhotakota", "Salima", 112)
        self.graph.add_edge("Dowa", "Salima", 67)
        self.graph.add_edge("Salima", "Dedza", 96)
        self.graph.add_edge("Dedza", "Ntcheu", 74)
        self.graph.add_edge("Dedza", "Lilongwe", 92)

    def dijkstra(self, start):
        distances = {name: float('inf') for name in self.graph.districts}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_district = heapq.heappop(priority_queue)

            if current_distance > distances[current_district]:
                continue

            for neighbor, weight in self.graph.districts[current_district].neighbors.items():
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
            for neighbor, weight in self.graph.districts[end].neighbors.items():
                if distances[end] == distances[neighbor] + weight:
                    path.append(neighbor)
                    path_cost += weight
                    end = neighbor
                    break
        path = list(reversed(path))
        return path, path_cost

    def run(self):
        start_point = input("Enter the starting point: ")
        end_point = input("Enter the destination point: ")

        if start_point in self.graph.districts and end_point in self.graph.districts:
            shortest_path, path_cost = self.shortest_path(start_point, end_point)
            if shortest_path:
                print("Shortest path:", shortest_path)
                print("Total distance of the path (path cost):", path_cost)
            else:
                print("No path found.")
        else:
            print("Start or destination point not found in the graph.")

if __name__ == "__main__":
    main_program = Main()
    main_program.run()
