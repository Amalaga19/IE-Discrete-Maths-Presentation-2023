import networkx as nx
import pandas as pd

# Load the modified data
data = pd.read_csv('Insert file here')

# Create the graph from the modified data
G = nx.from_pandas_edgelist(data, 'Station1', 'Station2', ['travel_seconds', 'line_name'], create_using=nx.DiGraph())

# Function to find the shortest path between any two stations
def find_shortest_path(source_station_name, target_station_name):
    # Find the names of the nodes in the graph that start with the source and target stations
    source_station = next((node for node in G.nodes if node.startswith(source_station_name)), None)
    target_station = next((node for node in G.nodes if node.startswith(target_station_name)), None)
    # Find the shortest path
    path = nx.dijkstra_path(G, source_station, target_station, weight='travel_seconds')
    # Calculate the time in minutes and seconds
    time_in_seconds = nx.dijkstra_path_length(G, source_station, target_station, weight='travel_seconds')
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    # Print the shortest path
    print("The shortest route between {} and {} is {}, and it will take {} minutes and {} seconds.".format(source_station, target_station, path, minutes, seconds))

# Call the function with the names of the stations you want to find the shortest path between
find_shortest_path('STATION 1', 'STATION 2')




















