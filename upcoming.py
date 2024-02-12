import requests
from datetime import datetime, timedelta
matches_url = "http://api.football-data.org/v4/matches/"
team_list_url = "http://api.football-data.org/v4/teams/"

# Set your API token
api_token = "42f8678a420b4f18bcbe614ef0b58c8e"

# Set the headers with the API token
headers = {
    "X-Auth-Token": api_token
}

# Function to fetch Arsenal's upcoming ten fixtures
def fetch_arsenal_fixtures():
    # Get today's date in the format "YYYY-MM-DD"
    today_date = datetime.today().strftime("%Y-%m-%d")
    
    # Get the date for ten days from today
    ten_days_later = (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d")

    # Define the parameters for the request
    params = {
        "status": "SCHEDULED",  # Only fetch scheduled matches
        "dateFrom": today_date,  # Matches from today onwards
        "dateTo": ten_days_later,  # Matches up to ten days from today
        "competitions": "PL",   # Premier League competition ID
    }

    # Make a GET request to the matches endpoint to get Arsenal's upcoming fixtures
    response = requests.get(matches_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Display Arsenal's upcoming fixtures
        fixtures = []
        for match in data.get("matches", []):
            home_team = match["homeTeam"]["name"]
            away_team = match["awayTeam"]["name"]
            match_date = match["utcDate"]
            
            fixtures.append((home_team, away_team, match_date))
        
        return fixtures
        print(fixtures)
    else:
        # Handle errors
        print(f"Failed to fetch Arsenal's fixtures. Status code: {response.status_code}")
        print(response.text)  # Print response text for debugging

# Function to fetch the last meeting result against each opponent
def fetch_last_meeting_result(opponent):
    # Define the parameters for the request
    params = {
        "team1": "Arsenal FC",
        "team2": opponent,
        "limit": 1  # Limit the number of matches to fetch to 1 (the last meeting)
    }
    
    # Make a GET request to the head2head endpoint to get the last meeting result
    response = requests.get(f"{matches_url}head2head", headers=headers, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the response contains matches data
        if "matches" in data:
            matches = data["matches"]
            
            # Check if there are previous matches between the teams
            if matches:
                last_meeting = matches[0]
                home_team = last_meeting["homeTeam"]["name"]
                away_team = last_meeting["awayTeam"]["name"]
                home_goals = last_meeting["score"]["fullTime"]["homeTeam"]
                away_goals = last_meeting["score"]["fullTime"]["awayTeam"]
                
                return f"{home_team} {home_goals} - {away_goals} {away_team}"
            else:
                return "No previous meeting found."
        else:
            return "No matches data found in the response."
    else:
        # Handle errors
        print("Error:", response.status_code)
        print(response.text)



# Call the function to fetch Arsenal's upcoming fixtures

fixtures = fetch_arsenal_fixtures()
if fixtures:
    print("\nArsenal's Upcoming Fixtures:")
    for fixture in fixtures:
        home_team, away_team, match_date = fixture
        print(f"{home_team} vs {away_team} - Date: {match_date}")
        
        # Fetch and display the last meeting result against the opponent
        last_meeting_result = fetch_last_meeting_result(away_team)
        print(f"Last Meeting Result against {away_team}: {last_meeting_result}")
else:
    print("Failed to fetch Arsenal's fixtures.")
