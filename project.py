import networkx as nx
from fpdf import FPDF

# Create a Graph
G = nx.Graph()

# Add towns as nodes in the graph
towns = ["Agdangan", "Buenavista", "Catanauan", "General Luna", "Macalelon", "Mulanay", "Padre Burgos",
          "Pitogo", "San Andres", "San Francisco", "San Narciso", "Unisan", "Alabat", "Atimonan", "Calauag",
          "Guinayangan", "Gumaca", "Lopez", "Perez", "Plaridel", "Quezon", "Tagkawayan"]
for town in towns:
    G.add_node(town)

# Define edges and weights as a list of tuples
edges_and_weights = [
    ("Atimonan", "Plaridel", 11.8),
    ("Atimonan","Unisan", 27.4),
    ("Atimonan","Padre Burgos", 39),
    ("Plaridel","Unisan", 25.5),
    ("Plaridel","Gumaca", 11.3),
    ("Gumaca","Pitogo", 22.6),
    ("Gumaca","Quezon", 17.1),
    ("Gumaca","Alabat", 40),
    ("Gumaca","Perez", 55.6),
    ("Gumaca","Lopez", 19.8),
    ("Gumaca","Unisan", 33.4),
    ("Lopez","Calauag", 10.6),
    ("Lopez","Catanauan", 41.9),
    ("Lopez","Buenavista", 33),
    ("Calauag","Guinayangan", 25.7),
    ("Calauag","Tagkawayan", 52.8),
    ("Agdangan","Unisan", 9.3),
    ("Padre Burgos","Agdangan", 23.5),
    ("Unisan","Pitogo", 21.2),
    ("Pitogo","Macalelon", 24.2),
    ("Macalelon","General Luna", 20.8),
    ("General Luna","Catanauan", 26),
    ("Catanauan","Mulanay", 23.7),
    ("San Francisco","Mulanay", 25.4),
    ("San Andres","San Francisco", 18.1),
    ("San Narciso","San Andres", 40.1),
    ("Buenavista","San Narciso", 27.6),
    ("Buenavista","Catanauan", 24.9),
    ("San Narciso","Mulanay", 39.1)
]
# Add edges and weights to the graph
G.add_weighted_edges_from(edges_and_weights)

# Find the shortest path between two towns using Dijkstra's Algorithm
def find_shortest_path(G, start, end):
    return nx.dijkstra_path(G, start, end, weight='weight')

print("---------------------------------------------")
print("Quezon Province's 3rd and 4th District Towns Travel Guide")

# Input the number of towns in the itinerary from the user
num_towns = int(input("Enter the number of towns in your itinerary: "))

# Input the towns in the itinerary from the user
itinerary = []
for i in range(num_towns):
    town = input("Enter town {}: ".format(i + 1))
    while town not in towns:
        print("---------------------------------------------")
        print("Invalid town. Please enter a valid input from the following list:")
        print(', '.join(towns))
        print("---------------------------------------------")
        town = input("Enter town {}: ".format(i + 1))
    else:
        itinerary.append(town)
print("---------------------------------------------")

# Get the shortest path between all the towns in the itinerary
shortest_paths = []
for i in range(num_towns - 1):
    shortest_path = find_shortest_path(G, itinerary[i], itinerary[i + 1])
    shortest_paths.append(shortest_path)

# Total distance
sum_weights = 0
output_str = ""
print("The shortest path/s for this itinerary is/are: ")
for shortest_path in shortest_paths:
    for i in range(len(shortest_path) - 1):
        weight = G[shortest_path[i]][shortest_path[i + 1]]['weight']
        sum_weights += weight
        output_str += shortest_path[i] + " to " + shortest_path[i + 1] + " with a distance of " + str(weight) + " km\n"

format_sum_weights = format(sum_weights, '.1f')
output_str += "The total distance of the itinerary is " + format_sum_weights + " km."

print(output_str)