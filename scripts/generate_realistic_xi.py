import pandas as pd

players = pd.read_csv("new_player_db_2026.csv")

# -----------------------------
# PLAYER SCORE
# -----------------------------
players["Score"] = (
    players["Power"]*0.4 +
    players["Innovation"]*0.3 +
    players["Acceleration"]*0.3
)

# -----------------------------
# OVERSEAS PLAYERS
# -----------------------------
overseas_list = {
"Dewald Brevis","Jamie Overton","Noor Ahmad","Nathan Ellis","Akeal Hosein",
"Matthew Short","Matt Henry","Zak Foulkes","Tristan Stubbs","Mitchell Starc",
"Dushmantha Chameera","Ben Duckett","David Miller","Pathum Nissanka",
"Lungi Ngidi","Kyle Jamieson","Jos Buttler","Glenn Phillips","Kagiso Rabada",
"Rashid Khan","Jason Holder","Tom Banton","Luke Wood","Rovman Powell",
"Sunil Narine","Cameron Green","Matheesha Pathirana","Finn Allen",
"Tim Seifert","Rachin Ravindra","Blessing Muzarabani","Aiden Markram",
"Matthew Breetzke","Nicholas Pooran","Mitchell Marsh","Anrich Nortje",
"Wanindu Hasaranga","Josh Inglis","Ryan Rickelton","Mitchell Santner",
"Will Jacks","Corbin Bosch","Trent Boult","Allah Ghazanfar",
"Sherfane Rutherford","Quinton De Kock","Marcus Stoinis","Marco Jansen",
"Azmatullah Omarzai","Mitch Owen","Xavier Bartlett","Lockie Ferguson",
"Cooper Connolly","Ben Dwarshuis","Lhuan-dre Pretorius","Shimron Hetmyer",
"Jofra Archer","Kwena Maphaka","Nandre Burger","Sam Curran",
"Donovan Ferreira","Adam Milne","Tim David","Phil Salt","Jacob Bethell",
"Romario Shepherd","Josh Hazlewood","Nuwan Thushara","Jacob Duffy",
"Jordan Cox","Travis Head","Heinrich Klaasen","Kamindu Mendis",
"Brydon Carse","Pat Cummins","Eshan Malinga","Liam Livingstone",
"Jack Edwards"
}

players["Overseas"] = players["Player_Name"].apply(
    lambda x: 1 if x in overseas_list else 0
)

# -----------------------------
# ROLE DETECTION
# -----------------------------
wk_list = {
"MS Dhoni","Sanju Samson","KL Rahul","Jos Buttler","Nicholas Pooran",
"Quinton De Kock","Phil Salt","Heinrich Klaasen","Rishabh Pant"
}

spin_list = {
"Rashid Khan","Noor Ahmad","Kuldeep Yadav","Yuzvendra Chahal",
"Wanindu Hasaranga","Ravindra Jadeja","Sai Kishore"
}

pace_list = {
"Jasprit Bumrah","Mohammed Shami","Mitchell Starc","Trent Boult",
"Josh Hazlewood","Pat Cummins","Jofra Archer","Nathan Ellis"
}

def detect_role(name):

    if name in wk_list:
        return "WK"
    elif name in spin_list:
        return "SPIN"
    elif name in pace_list:
        return "PACE"
    else:
        return "BAT"

players["Role"] = players["Player_Name"].apply(detect_role)

teams = players["Team"].unique()

best_xi = []

# -----------------------------
# TEAM SELECTION
# -----------------------------
for team in teams:

    team_players = players[players["Team"] == team]

    selected = pd.DataFrame()

    # 1 wicketkeeper
    wk = team_players[team_players["Role"]=="WK"].sort_values("Score",ascending=False).head(1)
    selected = pd.concat([selected,wk])

    # 1 spinner
    spin = team_players[team_players["Role"]=="SPIN"].sort_values("Score",ascending=False).head(1)
    selected = pd.concat([selected,spin])

    # 2 pacers
    pace = team_players[team_players["Role"]=="PACE"].sort_values("Score",ascending=False).head(2)
    selected = pd.concat([selected,pace])

    # remove duplicates
    selected = selected.drop_duplicates()

    # fill remaining by score
    remaining = team_players[
        ~team_players["Player_Name"].isin(selected["Player_Name"])
    ].sort_values("Score",ascending=False)

    for _,row in remaining.iterrows():

        if len(selected) >= 11:
            break

        # check overseas rule
        if row["Overseas"]==1 and selected["Overseas"].sum() >= 4:
            continue

        selected = pd.concat([selected,row.to_frame().T])

    # FINAL SAFETY FILL
    if len(selected) < 11:

        remaining = team_players[
            ~team_players["Player_Name"].isin(selected["Player_Name"])
        ].sort_values("Score",ascending=False)

        needed = 11 - len(selected)

        selected = pd.concat([selected,remaining.head(needed)])

    selected = selected.head(11)

    for _,row in selected.iterrows():

        best_xi.append({
            "Team":team,
            "Player":row["Player_Name"],
            "Role":row["Role"],
            "Score":round(row["Score"],2)
        })


df = pd.DataFrame(best_xi)

df.to_csv("best_playing_xi_realistic_2026.csv",index=False)

print("Realistic XI generated successfully")
print(df.groupby("Team").size())