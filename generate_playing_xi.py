import pandas as pd
from locked_players import locks

players = pd.read_csv("player_scores.csv")

teams = players["Team"].unique()

best_xi = []

for team in teams:

    team_players = players[players["Team"] == team]

    selected = []

    # Add locked players
    if team in locks:
        selected.extend(locks[team])

    # Fill remaining by score
    remaining = team_players[
        ~team_players["Player_Name"].isin(selected)
    ].sort_values("Score",ascending=False)

    for _,row in remaining.iterrows():

        if len(selected) >= 11:
            break

        # Overseas rule
        overseas_count = players[
            (players["Player_Name"].isin(selected)) &
            (players["Overseas"]==1)
        ].shape[0]

        if row["Overseas"]==1 and overseas_count >= 4:
            continue

        selected.append(row["Player_Name"])

    for p in selected:

        best_xi.append({
            "Team":team,
            "Player":p
        })

df = pd.DataFrame(best_xi)

df.to_csv("predicted_playing_xi.csv",index=False)

print("Playing XI generated")