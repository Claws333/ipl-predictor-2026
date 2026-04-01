"""IPL 2026 - Venue & Pitch Conditions Report
Usage: python scripts/venue_report.py
"""
import os, sys, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.teams import VENUES, TEAMS
from data.schedule import FIXTURES

OUTPUT_FILE = os.path.join("data", "venue_conditions.csv")

def run():
    print("\n" + "=" * 70)
    print("  IPL 2026 - VENUE & PITCH CONDITIONS REPORT")
    print("=" * 70)
    rows = []
    for venue, v in VENUES.items():
        ms = [f for f in FIXTURES if f["venue"] == venue]
        home_team = next((t for t, info in TEAMS.items() if info["home"] == venue), "-")
        bias_teams = ", ".join(f"{t} (+{round((m-1)*100)}%)" for t, m in v.get("pitch_bias", {}).items())
        print(f"\n  {venue}")
        print(f"    Pitch type   : {v['pitch_type']}")
        print(f"    Avg 1st inn  : {v['avg_first']}")
        print(f"    Dew factor   : {v['dew_factor']}")
        print(f"    Home favour  : {v['home_favor']}")
        print(f"    Home team    : {home_team}")
        print(f"    Pitch bias   : {bias_teams if bias_teams else 'None'}")
        print(f"    Matches 2026 : {len(ms)}")
        print(f"    Notes        : {v['notes']}")
        rows.append({"venue": venue, "city": v["city"], "pitch_type": v["pitch_type"],
                     "avg_first_inn": v["avg_first"], "dew_factor": v["dew_factor"],
                     "home_favor": v["home_favor"], "home_team": home_team,
                     "pitch_bias": bias_teams, "matches_2026": len(ms), "notes": v["notes"]})
    print("\n" + "=" * 70)
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    print(f"\nVenue report saved -> {OUTPUT_FILE}\n")

if __name__ == "__main__":
    run()
