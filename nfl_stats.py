#!./venv/bin/python
"""
        open the csv file called "nfl_offensive_stats.csv" and read in
        the csv data from the file.  The data is then stored in a list
        of dictionaries.
"""

# Import modules
import csv

# Create a list to hold the dictionaries
nfl_stats = []

# Open the file and read in the data
with open('nfl_offensive_stats.csv', 'r') as csvfile:
    # Create a reader object
    reader = csv.DictReader(csvfile)
    # Loop through the file and add the data to the list
    for row in reader:
        nfl_stats.append(row)
"""
the 3rd column in data is player position, the fourth column 
is the player, and the 8th column is the passing yards. 
For each player whose position in column 3 is "QB", 
determine the sum of yards from column 8 and print the 
player's name and total passing yards to the console.
"""
# Initialize the total passing yards
total_passing_yards = 0
# Loop through the list of dictionaries
for player in nfl_stats:
    # If the player is a QB
    if player['Pos'] == 'QB':
        # Add the passing yards to the total
        total_passing_yards += int(player['Yds'])
        # Print the player's name and passing yards
        print(player['Player'], player['Yds'])
# Print the total passing yards
print(total_passing_yards)

"""
the 3rd column in data is player position, the fourth column 
is the player, and the 8th column is the passing yards. 
For each player whose position in column 3 is "QB", 
determine the sum of yards from column 8 and print the 
player's name and total passing yards to the console.
"""
# Initialize the total passing yards
total_passing_yards = 0
# Loop through the list of dictionaries
for player in nfl_stats:
    # If the player is a QB
    if player['Pos'] == 'QB':
        # Add the passing yards to the total
        total_passing_yards += int(player['Yds'])
        # Print the player's name and passing yards
        print(player['Player'], player['Yds'])
# Print the total passing yards
print(total_passing_yards)

"""
the 3rd column in data is player position, the fourth column 
is the player, and the 8th column is the passing yards. 
For each player whose position in column 3 is "QB", 
determine the sum of yards from column 8 and print the 
player's name and total passing yards to the console.
"""
# Initialize the total passing yards
total_passing_yards = 0
# Loop through the list of dictionaries
for player in nfl_stats:
    # If the player is a QB
    if player['Pos'] == 'QB':
        # Add the passing yards to the total
        total_passing_yards += int(player['Yds'])
        # Print the player's name and passing yards
        print(player['Player'], player['Yds'])
# Print the total passing yards
print(total_passing_yards)

"""
the 3rd column in data is player position, the fourth column
"""

