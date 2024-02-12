import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv(r"C:\Users\Admin\Data scrapping\arsenal_matches_since_2022.csv")

# Total goals scored and conceded
total_goals_scored = df["Home Goals"].sum()
total_goals_conceded = df["Away Goals"].sum()
print("Total goals scored by Arsenal:", total_goals_scored)
print("Total goals conceded by Arsenal:", total_goals_conceded)

# Example analysis: Visualize goals scored over time
plt.plot(df["Date"], df["Home Goals"], label="Home Goals")
plt.plot(df["Date"], df["Away Goals"], label="Away Goals")
plt.xlabel("Date")
plt.ylabel("Goals")
plt.title("Goals Scored by Arsenal Over Time")
plt.legend()
plt.show()

# Filter matches where Arsenal is the home team and calculate the occurrences of goals scored
home_goals = df[df["Home Team"] == "Arsenal FC"]["Home Goals"].value_counts().sort_index()

# Filter matches where Arsenal is the away team and calculate the occurrences of goals scored
away_goals = df[df["Away Team"] == "Arsenal FC"]["Away Goals"].value_counts().sort_index()

# Combine the occurrences of goals scored as both home and away team
total_goals = home_goals.add(away_goals, fill_value=0)

# Plot the number of times Arsenal scored each number of goals
plt.bar(total_goals.index, total_goals.values, color='red')
plt.xlabel('Number of Goals')
plt.ylabel('Occurrences')
plt.title('Number of Goals Scored by Arsenal')
plt.xticks(total_goals.index)
plt.grid(axis='y')
plt.savefig

arsenal_matches = df[(df["Home Team"] == "Arsenal FC") | (df["Away Team"] == "Arsenal FC")]

# Initializing a dictionary to store head-to-head results
head_to_head = {}

for index, match in arsenal_matches.iterrows():
    opponent = match["Home Team"] if match["Home Team"] != "Arsenal FC" else match["Away Team"]
    arsenal_goals = match["Home Goals"] if match["Home Team"] == "Arsenal FC" else match["Away Goals"]
    opponent_goals = match["Away Goals"] if match["Home Team"] == "Arsenal FC" else match["Home Goals"]
    
    # Update the head-to-head dictionary with the match result
    if opponent not in head_to_head:
        head_to_head[opponent] = {"Wins": 0, "Draws": 0, "Losses": 0, "Goals For": 0, "Goals Against": 0}
    
    if arsenal_goals > opponent_goals:
        head_to_head[opponent]["Wins"] += 1
    elif arsenal_goals == opponent_goals:
        head_to_head[opponent]["Draws"] += 1
    else:
        head_to_head[opponent]["Losses"] += 1
    
    head_to_head[opponent]["Goals For"] += arsenal_goals
    head_to_head[opponent]["Goals Against"] += opponent_goals

# Convert the head-to-head dictionary to a DataFrame
head_to_head_df = pd.DataFrame.from_dict(head_to_head, orient='index')

# Calculate additional metrics
head_to_head_df["Matches Played"] = head_to_head_df["Wins"] + head_to_head_df["Draws"] + head_to_head_df["Losses"]
head_to_head_df["Goal Difference"] = head_to_head_df["Goals For"] - head_to_head_df["Goals Against"]
head_to_head_df["Win Percentage"] = (head_to_head_df["Wins"] / head_to_head_df["Matches Played"]) * 100

# Sort the DataFrame by the number of matches played
head_to_head_df = head_to_head_df.sort_values(by="Matches Played", ascending=False)

# Display the head-to-head results
print(head_to_head_df.head(10))