import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------

xi = pd.read_csv("predicted_playing_xi.csv")
players = pd.read_csv("player_scores.csv")
schedule = pd.read_csv("match_schedule.csv")
venues = pd.read_csv("venue_conditions.csv")

# -----------------------------
# FIX COLUMN NAMES
# -----------------------------

if "Player" in xi.columns:
    xi = xi.rename(columns={"Player": "Player_Name"})

# -----------------------------
# MERGE PLAYER DATA
# -----------------------------

merged = xi.merge(players, on="Player_Name")

# fix Team column if duplicated
if "Team_x" in merged.columns:
    merged["Team"] = merged["Team_x"]

elif "Team_y" in merged.columns:
    merged["Team"] = merged["Team_y"]

# -----------------------------
# CALCULATE TEAM STRENGTH
# -----------------------------

team_strength = merged.groupby("Team")["Score"].sum().to_dict()

# -----------------------------
# HOME GROUND ADVANTAGE
# -----------------------------

home_venues = {
"Bangalore":"Royal Challengers Bengaluru",
"Mumbai":"Mumbai Indians",
"Chennai":"Chennai Super Kings",
"Kolkata":"Kolkata Knight Riders",
"Delhi":"Delhi Capitals",
"Hyderabad":"Sunrisers Hyderabad",
"Lucknow":"Lucknow Super Giants",
"Ahmedabad":"Gujarat Titans",
"Jaipur":"Rajasthan Royals",
"Mullanpur":"Punjab Kings"
}

# -----------------------------
# MATCH PREDICTIONS
# -----------------------------

predictions = []

for _, match in schedule.iterrows():

    t1 = match["Team1"]
    t2 = match["Team2"]
    venue = match["Venue"]

    s1 = team_strength.get(t1,0)
    s2 = team_strength.get(t2,0)

    # -------------------------
    # VENUE CONDITIONS
    # -------------------------

    venue_row = venues[venues["Venue"] == venue]

    if not venue_row.empty:

        dew = venue_row.iloc[0]["DewFactor"]

        # dew advantage
        if dew > 0.6:
            s2 += 15

    # -------------------------
    # HOME ADVANTAGE
    # -------------------------

    if venue in home_venues:

        home = home_venues[venue]

        if home == t1:
            s1 += 12
        elif home == t2:
            s2 += 12

    # -------------------------
    # WIN PROBABILITY
    # -------------------------

    diff = abs(s1 - s2)

    prob = 50 + min(diff / 10, 40)

    if s1 > s2:
        winner = t1
    else:
        winner = t2

    predictions.append({
        "MatchID": match["MatchID"],
        "Team1": t1,
        "Team2": t2,
        "Venue": venue,
        "PredictedWinner": winner,
        "WinProbability": round(prob,1)
    })

# -----------------------------
# SAVE RESULTS
# -----------------------------

df = pd.DataFrame(predictions)

df.to_csv("match_predictions.csv", index=False)

print("\nMatch Predictions:\n")
print(df)