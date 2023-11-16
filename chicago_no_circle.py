import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_weighted_edges_from([
    ("Linden", "Central", 120),
    ("Central", "Noyes", 90),
    ("Noyes", "Foster", 90),
    ("Foster", "Davies", 90),
    ("Davies", "Dempster", 90),
    ("Dempster", "Main", 90),
    ("Main", "South Boulevard", 90),
    ("South Boulevard", "Howard", 180),
    ("Howard", "Wilson", 600),
    ("Wilson", "Belmont", 420),
    ("Dempster-Skokie", "Oakton-Skokie", 120),
    ("Oakton-Skokie", "Howard", 840),
    ("Howard", "Jarvis", 120),
    ("Jarvis", "Morse", 90),
    ("Morse", "Loyola", 120),
    ("Loyola", "Granville", 180),
    ("Granville", "Thorndale", 90),
    ("Thorndale", "Bryn Mawr", 60),
    ("Bryn Mawr", "Berwyn", 90),
    ("Berwyn", "Argyle", 90),
    ("Argyle", "Lawrence", 60),
    ("Lawrence", "Wilson", 60),
    ("Wilson", "Sheridan", 180),
    ("Sheridan", "Addison", 120),
    ("Addison", "Belmont", 120),
    ("Belmont", "Fullerton", 180),
    ("Fullerton", "North/Clybourn", 120),
    ("North/Clybourn", "Clark/Division", 180),
    ("Clark/Division", "Chicago_Red", 180),
    ("Chicago_Red", "Grand_Red", 60),
    ("Grand_Red", "Lake", 120),
    ("Lake", "Monroe_Red", 90),
    ("Monroe_Red", "Jackson", 90),
    ("Jackson", "Harrison", 60),
    ("Harrison", "Roosevelt", 90),
    ("Roosevelt", "Cermak-Chinatown", 180),
    ("Cermak-Chinatown", "Sox-35th", 180),
    ("Sox-35th", "47th", 180),
    ("47th", "Garfield", 120),
    ("Garfield", "63rd", 120),
    ("63rd", "69th", 120),
    ("69th", "79th", 120),
    ("79th", "87th", 120),
    ("87th", "95th/Dan Ryan", 180),
    ("O'Hare", "Rosemont", 300),
    ("Rosemont", "Cumberland", 120),
    ("Cumberland", "Harlem_Blue1", 180),
    ("Harlem_Blue1", "Jefferson Park", 300),
    ("Jefferson Park", "Montrose", 120),
    ("Montrose", "Irving Park", 120),
    ("Irving Park", "Addison_Blue", 120),
    ("Addison_Blue", "Belmont_Blue", 120),
    ("Belmont_Blue", "Logan Square", 120),
    ("Logan Square", "California_Blue", 120),
    ("California_Blue", "Western_Blue1", 120),
    ("Western_Blue1", "Damen", 120),
    ("Damen", "Division", 120),
    ("Division", "Chicago_Blue", 120),
    ("Chicago_Blue", "Grand_Blue", 120),
    ("Grand_Blue", "Clark/Lake", 120),
    ("Clark/Lake", "Washington", 120),
    ("Washington", "Monroe_Blue", 60),
    ("Monroe_Blue", "Jackson", 60),
    ("Jackson", "LaSalle", 60),
    ("LaSalle", "Clinton", 60),
    ("Clinton", "UIC-Halsted", 180),
    ("UIC-Halsted", "Racine", 120),
    ("Racine", "Illinois Medical District", 180),
    ("Illinois Medical District", "Western_Blue2", 180),
    ("Western_Blue2", "Kedzie-Homan", 240),
    ("Kedzie-Homan", "Pulaski_Blue", 240),
    ("Pulaski_Blue", "Cicero_Blue", 180),
    ("Cicero_Blue", "Austin_Blue", 360),
    ("Austin_Blue", "Oak Park_Blue", 120),
    ("Oak Park_Blue", "Harlem_Blue2", 240),
    ("Harlem_Blue2", "Forest Park", 180),
    ("Harlem/Lake", "Oak Park_Green", 120),
    ("Oak Park_Green", "Ridgeland", 90),
    ("Ridgeland", "Austin_Green", 90),
    ("Austin_Green", "Central", 90),
    ("Central", "Laramie", 90),
    ("Laramie", "Cicero_Green", 120),
    ("Cicero_Green", "Pulaski_Green", 120),
    ("Pulaski_Green", "Conservatory-Central Park Drive", 120),
    ("Conservatory-Central Park Drive", "Kedzie_Green", 120),
    ("Kedzie_Green", "California_Green", 120),
    ("California_Green", "Ashland", 240),
    ("Clinton", "Clark/Lake", 120),
    ("Clark/Lake", "State/Lake", 60),
    ("State/Lake", "Washington/Wabash", 60),
    ("Washington/Wabash", "Adams/Wabash", 60),
    ("Adams/Wabash", "Roosevelt", 240),
    ("Roosevelt", "Cermak-McCormick Place", 180),
    ("Cermak-McCormick Place", "35-Bronzeville-IIT", 240),
    ("35-Bronzeville-IIT", "Indiana", 180),
    ("Indiana", "43rd", 120),
    ("43rd", "47th_Green", 90),
    ("47th_Green", "51st", 90),
    ("51st", "Garfield_Green", 120),
    ("Garfield_Green", "Halsted_Green", 360),
    ("Garfield_Green", "King Drive", 240),
    ("King Drive", "Cottage Grove", 120),
    ("Halsted_Green", "Ashland/63rd", 180),
    ("Kimball", "Kedzie_Brown", 120),
    ("Kedzie_Brown", "Francisco", 90),
    ("Francisco", "Rockwell", 90),
    ("Rockwell", "Western_Brown", 90),
    ("Western_Brown", "Damen_Brown", 90),
    ("Damen_Brown", "Montrose_Brown", 60),
    ("Montrose_Brown", "Irving Park_Brown", 60),
    ("Irving Park_Brown", "Addison_Brown", 60),
    ("Addison_Brown", "Paulina", 180),
    ("Paulina", "Southport", 60),
    ("Southport", "Belmont", 120),
    ("Belmont", "Wellington", 90),
    ("Wellington", "Diversey", 90),
    ("Diversey", "Fullerton", 120),
    ("Fullerton", "Armitage", 60),
    ("Armitage", "Sedgwick", 240),
    ("Sedgwick", "Chicago_Brown", 240),
    ("Chicago_Brown", "Merchandise Mart", 120),
    ("Merchandise Mart", "Washington/Wells", 120),
    ("Merchandise Mart", "Clark/Lake", 90),
    ("Washington/Wells", "Quincy", 60),
    ("Quincy", "LaSalle/Van Buren", 120),
    ("LaSalle/Van Buren", "Harold Washington Library", 90),
    ("Harold Washington Library", "Adams/Wabash", 60),
    ("Adams/Wabash", "Washington/Wabash", 60),
    ("Washington/Wabash", "State/Lake", 120),
    ("State/Lake", "Clark/Lake", 90),
    ("Clark/Lake", "Merchandise Mart", 120),
    ("54th/Cermak", "Cicero", 120),
    ("Cicero", "Kostner", 120),
    ("Kostner", "Pulaski_Pink", 90),
    ("Pulaski_Pink", "Central Park", 90),
    ("Central Park", "Kedzie_Pink", 60),
    ("Kedzie_Pink", "California_Pink", 60),
    ("California_Pink", "Western_Pink", 90),
    ("Western_Pink", "Damen_Pink", 90),
    ("Damen_Pink", "18th", 120),
    ("18th", "Polk", 180),
    ("Polk", "Ashland", 180),
    ("Ashland", "Morgan", 120),
    ("Morgan", "Clinton", 120),
    ("Clinton", "Clark/Lake", 120),
    ("Clark/Lake", "State/Lake", 90),
    ("State/Lake", "Washington/Wabash", 90),
    ("Washington/Wabash", "Adams/Wabash", 90),
    ("Adams/Wabash", "Harold Washington Library", 90),
    ("Harold Washington Library", "LaSalle/Van Buren", 30),
    ("LaSalle/Van Buren", "Quincy", 90),
    ("Quincy", "Washington/Wells", 60),
    ("Washington Wells", "Clinton", 180),
    ("Midway", "Pulaski_Orange", 120),
    ("Pulaski_Orange", "Kedzie_Orange", 180),
    ("Kedzie_Orange", "Western_Orange", 120),
    ("Western_Orange", "35th/Archer", 240),
    ("35th/Archer", "Ashland_Orange", 120),
    ("Ashland_Orange", "Halsted", 180),
    ("Halsted", "Roosevelt", 300),
    ("Roosevelt", "Harold Washington Library-State/Van Buren", 180),
    ("Harold Washington Library-State/Van Buren", "LaSalle/Van Buren", 60),
    ("LaSalle/Van Buren", "Quincy", 60),
    ("Quincy", "Washington/Wells", 90),
    ("Washington/Wells", "Clark/Lake", 120),
    ("Clark/Lake", "State/Lake", 60),
    ("State/Lake", "Washington/Wabash", 120),
    ("Washington/Wabash", "Adams/Wabash", 60),
    ("Adams/Wabash", "Roosevelt", 180)
    ])


# Draw the graph
nx.draw(G, with_labels=True)
# plt.show()

def find_shortest_path(start, end):
    shortest_path = nx.dijkstra_path(G, start, end)
    total_time = nx.dijkstra_path_length(G, start, end)
    print(f"The shortest path from {start} to {end} is: {shortest_path}")
    print(f"The total travel time is: {total_time//60} minutes and {total_time%60} seconds")
    return total_time

#find_shortest_path("Kedzie-Homan", "Kostner")
#find_shortest_path("Rockwell", "Cicero_Green")

# Example usage
#print(find_shortest_path('Howard', 'Kostner'),
#find_shortest_path("LaSalle/Van Buren", "Western_Blue1"),
#find_shortest_path("Western_Pink", "Cermak-Chinatown"),
#find_shortest_path("Garfield", "Belmont"),
#find_shortest_path("Roosevelt", "Cicero_Green"),
#find_shortest_path("Kedzie_Orange", "Clark/Lake"),
#find_shortest_path("Western_Blue1", "Ashland/63rd"),
#find_shortest_path("Merchandise Mart", "Kedzie_Orange"),
#find_shortest_path("Western_Pink", "Roosevelt"),
#find_shortest_path("47th_Green", "Belmont"),
#find_shortest_path("Western_Blue1", "LaSalle/Van Buren"))
