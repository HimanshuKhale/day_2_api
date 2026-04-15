from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/score")
def score():
    return {
        "runs": 78,
        "wickets": 3,
        "overs": 12.4
    }

@app.get("/player/batter")
def batter_stats():
    return {
        "name": "Virat Kohli",
        "runs": 45,
        "balls": 31,
        "fours": 4,
        "sixes": 1,
        "strike_rate": 145.16
    }

@app.get("/player/bowler")
def bowler_stats():
    return {
        "name": "Bumrah",
        "overs": 4,
        "runs_conceded": 22,
        "wickets": 2,
        "economy": 5.5
    }

@app.get("/team/analytics")
def team_analytics():
    return {
        "team": "India",
        "matches": 5,
        "wins": 4,
        "losses": 1,
        "points": 8,
        "net_run_rate": 1.25
    }


@app.get("/tournament/summary")
def tournament_summary():
    return {
        "total_matches": 16,
        "highest_score": 212,
        "lowest_score": 94,
        "most_runs_player": "Virat Kohli",
        "most_wickets_player": "Bumrah"
    }

from pydantic import BaseModel

class MatchInput(BaseModel):
    current_score: int
    wickets_fell: int
    overs_remaining: float
    target: int

@app.post("/win-predictor")
def predict(match: MatchInput):
    runs_needed = match.target - match.score
    crr = match.score / (20 - match.overs_remaining)
    rrr = runs_needed / match.overs_remaining

    if crr > rrr:
        prediction = (crr-rrr)

    return {
        "runs_needed": runs_needed,
        "prediction": "62% chance"
    }

