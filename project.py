import networkx as nx

# Create a Graph
G = nx.Graph()

# Add cities as nodes in the graph
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
for city in cities:
    G.add_node(city)

# Add edges between the cities with a weight representing the distance between the cities
G.add_edge("Delhi", "Mumbai", weight=1200)
G.add_edge("Delhi", "Kolkata", weight=800)
G.add_edge("Delhi", "Chennai", weight=1100)
G.add_edge("Mumbai", "Kolkata", weight=900)
G.add_edge("Mumbai", "Bangalore", weight=500)
G.add_edge("Kolkata", "Chennai", weight=600)
G.add_edge("Chennai", "Bangalore", weight=300)

# Find the shortest path between two cities using Dijkstra's Algorithm
def find_shortest_path(G, start, end):
    return nx.dijkstra_path(G, start, end, weight='weight')

# Input the start and end cities from the user
start_city = input("Enter start city: ")
end_city = input("Enter end city: ")

# Get the shortest path between the two cities
shortest_path = find_shortest_path(G, start_city, end_city)

# Print the shortest path
print("The shortest path between", start_city, "and", end_city, "is:")
for i in range(len(shortest_path) - 1):
    print(shortest_path[i], "to", shortest_path[i + 1], "with a distance of", G[shortest_path[i]][shortest_path[i + 1]]['weight'], "km")