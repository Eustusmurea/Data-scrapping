import requests
import pandas as pd
from datetime import datetime

 # Define the API endpoint
url = "https://api.football-data.org/v2/teams/57/matches"  

 # 57 is the ID for Arsenal

headers = {
        "X-Auth-Token": "42f8678a420b4f18bcbe614ef0b58c8e" 
    }
today_date = datetime.today().strftime("%Y-%m-%d")
    
# Specify parameters to filter matches - the API limits to <750 days
params = {
        "dateFrom": "2022-08-08",
        "dateTo": today_date,  
        "status": "FINISHED"
    }

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Display or analyze the filtered matches
        matches_since_2022 = data["matches"]

        match_data = []

        # Populate the list with the match data
        for match in matches_since_2022:
            date = match["utcDate"]
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            home_goals = match["score"]["fullTime"]["homeTeam"]
            away_goals = match["score"]["fullTime"]["awayTeam"]

            match_data.append({"Date": date, "Home Team": home_team, "Away Team": away_team, "Home Goals": home_goals, "Away Goals": away_goals})

        # Create a DataFrame from the match data list
        df = pd.DataFrame(match_data)
# Save DataFrame to a CSV file
df.to_csv('matches_since_2022.csv', index=False)
