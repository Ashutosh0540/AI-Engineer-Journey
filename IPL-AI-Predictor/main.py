from fastapi import FastAPI
from model import predict, predict_proba
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI()

import logging

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    return {"message": "IPL predictor API"}

@app.get("/predict")
def get_prediction(team1: str, team2: str, venue: int):

    valid_teams = ["MI", "CSK", "RCB"]

    if team1 not in valid_teams or team2 not in valid_teams:
        return {"error": "Invalid team name"}

    logging.info(f"Prediction request: {team1} vs {team2}")

    result = predict(team1, team2, venue)
    prob = predict_proba(team1, team2, venue)

    return {
        "team1": team1,
        "team2": team2,
        "predicted_winner": team1 if result == 1 else team2,
        "win_probability": round(prob * 100, 2),
        "model": "RandomForest"
    }

@app.get("/matches")
def get_matches():
    if not API_KEY:
        return {"error": "API key not found"}

    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

    try:
        res = requests.get(url)
        data = res.json()

        matches = []
        for match in data.get("data", []):
            teams = match.get("teams", [])
            if len(teams) == 2:
                matches.append({
                    "team1": teams[0],
                    "team2": teams[1]
                })

        return {"matches": matches}

    except Exception as e:
        return {"error": str(e)}