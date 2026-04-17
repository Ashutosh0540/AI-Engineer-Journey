import pandas as pd
from sklearn.linear_model import LogisticRegression

#loading data
df = pd.read_csv("data.csv")

#Encode teams
teams = list(set(df["team1"]).union(set(df["team2"])))
team_map={team: i for i, team in enumerate(teams)}

df["team1"] = df["team1"].map(team_map)
df["team2"] = df["team2"].map(team_map)

X = df[["team1", "team2", "venue"]]
Y = df["team1_win"]

model =LogisticRegression()
model.fit(X,Y)

#save mapping + model
def predict(team1, team2, venue):
    t1 = team_map[team1]
    t2 = team_map[team2]
    pred = model.predict([[t1,t2,venue]])
    return int(pred[0])
def predict_proba(team1, team2, venue):
    t1 = team_map[team1]
    t2 = team_map[team2]
    prob = model.predict_proba([[t1, t2, venue]])
    return prob[0][1]