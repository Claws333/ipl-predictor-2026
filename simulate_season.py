import pandas as pd

matches = pd.read_csv("match_predictions.csv")

points = {}

for _,row in matches.iterrows():

    t1 = row["Team1"]
    t2 = row["Team2"]
    winner = row["PredictedWinner"]

    for team in [t1,t2]:

        if team not in points:
            points[team] = 0

    points[winner] += 2

table = pd.DataFrame(points.items(),columns=["Team","Points"])

table = table.sort_values("Points",ascending=False)

print("\nPredicted IPL Points Table:\n")
print(table)

table.to_csv("points_table_prediction.csv",index=False)