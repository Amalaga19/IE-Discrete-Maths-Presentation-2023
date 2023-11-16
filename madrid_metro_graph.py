import networkx as nx
import pandas as pd

# Load the modified data
data = pd.read_csv('madrid_metro_modified.csv')

# Create the graph from the modified data
G = nx.from_pandas_edgelist(data, 'v1', 'v2', ['travel_seconds', 'edge_name'], create_using=nx.DiGraph())

# Function to find the shortest path between any two stations
def find_shortest_path(source_station_name, target_station_name):
    # Find the names of the nodes in the graph that start with the source and target stations
    source_station = next((node for node in G.nodes if node.startswith(source_station_name)), None)
    target_station = next((node for node in G.nodes if node.startswith(target_station_name)), None)

    # If either station is not found in the graph, print an error message
    if source_station is None:
        print(f"Error: The station '{source_station_name}' was not found in the graph.")
        return
    if target_station is None:
        print(f"Error: The station '{target_station_name}' was not found in the graph.")
        return

    # Check if source and target stations are on the same line
    for edge in G.edges(data=True):
        if edge[0] == source_station and edge[1] == target_station:
            minutes, seconds = divmod(edge[2]['travel_seconds'], 60)
            print(f"Take line {edge[2]['edge_name']} from {source_station} to {target_station}. It will take {minutes} minutes and {seconds} seconds.")
            return

    # Find the shortest path
    path = nx.dijkstra_path(G, source_station, target_station, weight='travel_seconds')

    # Calculate the time in minutes and seconds
    time_in_seconds = nx.dijkstra_path_length(G, source_station, target_station, weight='travel_seconds')
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    # Print the shortest path
    print("The shortest route between {} and {} is {}, and it will take {} minutes and {} seconds.".format(source_station, target_station, path, minutes, seconds))

# Call the function with the names of the stations you want to find the shortest path between
find_shortest_path('PUENTE DE VALLECAS', 'ESTRELLA')
