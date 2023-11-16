import pandas as pd

# Load the data
data = pd.read_csv('chicago_metro.csv')

# Create a new DataFrame to store the modified data
data_modified = data.copy()

# Find all the stations that connect more than one line
stations = pd.concat([data['station'], data['next_station']], ignore_index=True).unique()
connecting_stations = [station for station in stations if len(data[(data['station'] == station) | (data['next_station'] == station)]['line_color'].unique()) > 1]

# For each connecting station, modify the station name to include the line number and add a new row for each pair of lines it connects
for station in connecting_stations:
    lines = data[(data['station'] == station) | (data['next_station'] == station)]['line_color'].unique()
    for line in lines:
        # Modify the station name to include the line number
        data_modified.loc[(data_modified['station'] == station) & (data_modified['line_color'] == line), 'station'] = f"{station} ({line} line)"
        data_modified.loc[(data_modified['next_station'] == station) & (data_modified['line_color'] == line), 'next_station'] = f"{station} ({line} line)"
        # Add a new row for each pair of lines the station connects
        for other_line in lines:
            if line != other_line:
                new_row = pd.Series({
                    'station': f"{station} (LINE {line})",
                    'next_station': f"{station} (LINE {other_line})",
                    'approximate_travel_time_seconds': 450,
                    'line_color': 'CHANGE'
                })
                data_modified = pd.concat([data_modified, pd.DataFrame(new_row).T])

# Save the modified data to a new CSV file
data_modified.to_csv('chicago_metro_modified.csv', index=False)

