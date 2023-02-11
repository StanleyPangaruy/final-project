import networkx as nx

# Create a Graph
G = nx.Graph()

# Add towns as nodes in the graph
towns = ["Agdangan", "Buenavista", "Catanauan", "General Luna", "Macalelon", "Mulanay", "Padre Burgos",
          "Pitogo", "San Andres", "San Francisco", "San Narciso", "Unisan", "Alabat", "Atimonan", "Calauag",
          "Guinayangan", "Gumaca", "Lopez", "Perez", "Plaridel", "Quezon", "Tagkawayan"]
for town in towns:
    G.add_node(town)

# Add edges between the towns with a weight representing the distance between the towns
G.add_edge("Atimonan", "Plaridel", weight=11.8)
G.add_edge("Atimonan","Unisan", weight=27.4)
G.add_edge("Atimonan","Padre Burgos", weight=39)
G.add_edge("Plaridel","Unisan", weight=25.5)
G.add_edge("Plaridel","Gumaca", weight=11.3)
G.add_edge("Gumaca","Pitogo", weight=22.6)
G.add_edge("Gumaca","Quezon", weight=17.1)
G.add_edge("Gumaca","Alabat", weight=40)
G.add_edge("Gumaca","Perez", weight=55.6)
G.add_edge("Gumaca","Lopez", weight=19.8)
G.add_edge("Gumaca","Unisan", weight=33.4)
G.add_edge("Lopez","Calauag", weight=10.6)
G.add_edge("Lopez","Catanauan", weight=41.9)
G.add_edge("Lopez","Buenavista", weight=33)
G.add_edge("Calauag","Guinayangan", weight=25.7)
G.add_edge("Calauag","Tagkawayan", weight=52.8)
G.add_edge("Agdangan","Unisan", weight=9.3)
G.add_edge("Padre Burgos","Agdangan", weight=23.5)
G.add_edge("Unisan","Pitogo", weight=21.2)
G.add_edge("Pitogo","Macalelon", weight=24.2)
G.add_edge("Macalelon","General Luna", weight=20.8)
G.add_edge("General Luna","Catanauan", weight=26)
G.add_edge("Catanauan","Mulanay", weight=23.7)
G.add_edge("San Francisco","Mulanay", weight=25.4)
G.add_edge("San Andres","San Francisco", weight=18.1)
G.add_edge("San Narciso","San Andres", weight=40.1)
G.add_edge("Buenavista","San Narciso", weight=27.6)
G.add_edge("Buenavista","Catanauan", weight=24.9)
G.add_edge("San Narciso","Mulanay", weight=39.1)

# Find the shortest path between two towns using Dijkstra's Algorithm
def find_shortest_path(G, start, end):
    return nx.dijkstra_path(G, start, end, weight='weight')

print("---------------------------------------------")
print("Quezon Province's 3rd and 4th District Travel Guide")
# Input the start and end towns from the user
start_city = input("Enter starting town: ")
end_city = input("Enter destination: ")
print("---------------------------------------------")
# Get the shortest path between the two towns
shortest_path = find_shortest_path(G, start_city, end_city)

#total distance
sum_weights = 0
print("The shortest path between", start_city, "and", end_city, "is:")
for i in range(len(shortest_path) - 1):
    weight = G[shortest_path[i]][shortest_path[i + 1]]['weight']
    sum_weights += weight
    print(shortest_path[i], "to", shortest_path[i + 1], "with a distance of", weight, "km")
format_sum_weights = format(sum_weights, '.1f')
print("The total distance of the shortest path is", format_sum_weights, "km.")