import pandas as pd

# --------------------------------
# LOAD PLAYER DATABASE
# --------------------------------
players = pd.read_csv("new_player_db_2026.csv")

# --------------------------------
# OVERSEAS PLAYER LIST
# --------------------------------
overseas_players = {
"Dewald Brevis","Jamie Overton","Noor Ahmad","Nathan Ellis","Akeal Hosein",
"Matthew Short","Matt Henry","Zak Foulkes",
"Tristan Stubbs","Mitchell Starc","Dushmantha Chameera","Ben Duckett",
"David Miller","Pathum Nissanka","Lungi Ngidi","Kyle Jamieson",
"Jos Buttler","Glenn Phillips","Kagiso Rabada","Rashid Khan",
"Jason Holder","Tom Banton","Luke Wood",
"Rovman Powell","Sunil Narine","Cameron Green","Matheesha Pathirana",
"Finn Allen","Tim Seifert","Rachin Ravindra","Blessing Muzarabani",
"Aiden Markram","Matthew Breetzke","Nicholas Pooran","Mitchell Marsh",
"Anrich Nortje","Wanindu Hasaranga","Josh Inglis",
"Ryan Rickelton","Mitchell Santner","Will Jacks","Corbin Bosch",
"Trent Boult","Allah Ghazanfar","Sherfane Rutherford","Quinton De Kock",
"Marcus Stoinis","Marco Jansen","Azmatullah Omarzai","Mitch Owen",
"Xavier Bartlett","Lockie Ferguson","Cooper Connolly","Ben Dwarshuis",
"Lhuan-dre Pretorius","Shimron Hetmyer","Jofra Archer","Kwena Maphaka",
"Nandre Burger","Sam Curran","Donovan Ferreira","Adam Milne",
"Tim David","Phil Salt","Jacob Bethell","Romario Shepherd",
"Josh Hazlewood","Nuwan Thushara","Jacob Duffy","Jordan Cox",
"Travis Head","Heinrich Klaasen","Kamindu Mendis","Brydon Carse",
"Pat Cummins","Eshan Malinga","Liam Livingstone","Jack Edwards"
}

# --------------------------------
# ADD OVERSEAS COLUMN
# --------------------------------
players["Overseas"] = players["Player_Name"].apply(
    lambda x: 1 if x in overseas_players else 0
)

# --------------------------------
# PLAYER SCORE
# --------------------------------
players["Score"] = (
    players["Power"]*0.4 +
    players["Innovation"]*0.3 +
    players["Acceleration"]*0.3
)

teams = players["Team"].unique()

best_xi = []

# --------------------------------
# GENERATE BEST XI
# --------------------------------
for team in teams:

    team_players = players[players["Team"] == team]

    overseas = team_players[team_players["Overseas"] == 1]
    indian = team_players[team_players["Overseas"] == 0]

    overseas = overseas.sort_values("Score",ascending=False).head(4)
    indian = indian.sort_values("Score",ascending=False).head(7)

    final_team = pd.concat([overseas, indian])

    # safety check
    if len(final_team) < 11:

        remaining = team_players[~team_players["Player_Name"].isin(final_team["Player_Name"])]
        remaining = remaining.sort_values("Score",ascending=False)

        needed = 11 - len(final_team)

        final_team = pd.concat([final_team, remaining.head(needed)])

    for _,row in final_team.iterrows():

        best_xi.append({
            "Team":team,
            "Player":row["Player_Name"],
            "Score":round(row["Score"],2)
        })


df = pd.DataFrame(best_xi)

df.to_csv("best_playing_xi_2026.csv",index=False)

print("Best XI generated successfully")
print(df.groupby("Team").size())