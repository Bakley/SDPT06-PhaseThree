import random

# Define the regions and countries
regions = {
    "North Africa": ["Egypt", "Libya", "Tunisia", "Algeria", "Morocco", "Mauritania"],
    "West & Mid-Central Africa": [
        "Nigeria", "Ghana", "Ivory Coast", "Senegal", "Mali", "Burkina Faso",
        "Niger", "Togo", "Benin", "Sierra Leone", "Liberia", "Guinea",
        "Gambia", "Cape Verde", "Chad", "Central African Republic"
    ],
    "East Africa": ["Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "South Sudan", "Ethiopia", "Somalia", "Djibouti"],
    "Central Africa": ["Angola", "Cameroon", "Congo", "Democratic Republic of the Congo", "Gabon", "Equatorial Guinea", "Sao Tome and Principe"],
    "Southern Africa": [
        "South Africa", "Zimbabwe", "Zambia", "Botswana", "Namibia", "Lesotho",
        "Swaziland", "Malawi", "Mozambique", "Angola", "Madagascar", "Mauritius",
        "Seychelles", "Comoros", "Eswatini", "Tanzania"
    ]
}

# Number of teams each region will contribute
slots = {
    "North Africa": 2,
    "West & Mid-Central Africa": 4,
    "East Africa": 4,
    "Central Africa": 2,
    "Southern Africa": 4
}

def select_teams(region, num_teams):
    return random.sample(region, num_teams)

# Select the teams
league_teams = {}
for region, countries in regions.items():
    num_teams = slots[region]
    selected_teams = select_teams(countries, num_teams)
    league_teams[region] = selected_teams

# Display the selected teams for the league
print("Basketball League Teams for New Africa:")
for region, teams in league_teams.items():
    print(f"{region}: {', '.join(teams)}")
