import requests
from datetime import datetime

# Define the API endpoints
competitions_url = "http://api.football-data.org/v4/competitions/"
matches_url = "http://api.football-data.org/v4/matches/"

# Set your API token
api_token = "42f8678a420b4f18bcbe614ef0b58c8e"

# Set the headers with the API token
headers = {
    "X-Auth-Token": api_token
}

# Function to fetch today's matches
def fetch_today_matches():
    # Get today's date in the format "YYYY-MM-DD"
    today_date = datetime.today().strftime("%Y-%m-%d")

    # Make a GET request to the competitions endpoint to get competition IDs
    response = requests.get(competitions_url, headers=headers)
    competition_ids = []

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract competition IDs
        competition_ids = [competition["id"] for competition in data["competitions"]]
    else:
        # Handle errors
        print("Error:", response.status_code)

    # Make a GET request to the matches endpoint
    response = requests.get(matches_url, headers=headers, params={"date": today_date})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Display today's matches
        print("Today's Matches:")
        for match in data["matches"]:
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            competition_id = match["competition"]["id"]
            
            # Check if the match is from one of the competitions we retrieved earlier
            if competition_id in competition_ids:
                print(f"{home_team} vs {away_team}")
    else:
        # Handle errors
        print("Error:", response.status_code)

# Call the function to fetch and display today's matches
fetch_today_matches()
