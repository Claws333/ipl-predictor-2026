"""IPL 2026 - Single Match Predictor
Usage:
    python scripts/predict_match.py
    python scripts/predict_match.py --t1 MI --t2 CSK --venue "Wankhede Stadium, Mumbai"
    python scripts/predict_match.py --t1 KKR --t2 SRH --venue "Narendra Modi Stadium, Ahmedabad" --neutral
"""
import os, sys, argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.teams import TEAMS, VENUES
from scripts.engine import predict_match, team_score

TEAM_LIST  = list(TEAMS.keys())
VENUE_LIST = list(VENUES.keys())

def print_result(t1, t2, venue, neutral=False):
    res = predict_match(t1, t2, venue, neutral)
    bar_len = 40
    filled  = round(res["w1"]/100*bar_len)
    bar     = "█"*filled + "░"*(bar_len-filled)
    print("\n" + "-"*62)
    print("  IPL 2026 MATCH PREDICTION")
    print("-"*62)
    print(f"  {TEAMS[t1]['name']}  vs  {TEAMS[t2]['name']}")
    print(f"  Venue   : {venue}")
    print(f"  Neutral : {'Yes' if neutral else 'No'}")
    print("-"*62)
    print(f"\n  {t1} [{res['w1']}%]  {bar}  [{res['w2']}%] {t2}\n")
    print(f"  Predicted winner : {res['winner']}  ({max(res['w1'],res['w2'])}%)")
    print(f"  Match margin     : {res['margin'].upper()}")
    print(f"  Pitch type       : {res['pitch_type']}")
    print(f"  Dew factor       : {res['dew_factor']}")
    print(f"  Avg 1st innings  : {res['avg_first_innings']}")
    print("\n  Key factors:")
    for fac in res["factors"]:
        print(f"    * {fac}")
    if not res["factors"]:
        print("    * Pure strength comparison - no special factors")
    print("\n  Composite team scores:")
    for t in [t1, t2]:
        print(f"    {t:<5}  {team_score(t):.2f}")
    print("-"*62 + "\n")

def interactive():
    print("\n  IPL 2026 - Single Match Predictor")
    print("  Teams:", ", ".join(TEAM_LIST))
    t1 = input("\n  Team 1 code: ").strip().upper()
    t2 = input("  Team 2 code: ").strip().upper()
    print("\n  Venues:")
    for i, v in enumerate(VENUE_LIST, 1):
        print(f"    {i:>2}. {v}")
    choice = input("\n  Venue number or name: ").strip()
    try:
        venue = VENUE_LIST[int(choice)-1]
    except (ValueError, IndexError):
        venue = choice
    neutral = input("  Neutral venue? (y/n) [n]: ").strip().lower() == "y"
    print_result(t1, t2, venue, neutral)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--t1",      type=str)
    parser.add_argument("--t2",      type=str)
    parser.add_argument("--venue",   type=str)
    parser.add_argument("--neutral", action="store_true")
    args = parser.parse_args()
    if args.t1 and args.t2 and args.venue:
        print_result(args.t1.upper(), args.t2.upper(), args.venue, args.neutral)
    else:
        interactive()
