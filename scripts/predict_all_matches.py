"""IPL 2026 - Predict all 70 matches
Usage: python scripts/predict_all_matches.py
Output: data/match_predictions_2026.csv
"""
import os, sys, csv
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.schedule import FIXTURES
from data.teams import TEAMS
from scripts.engine import predict_match

OUTPUT_FILE = os.path.join("data", "match_predictions_2026.csv")

def run():
    results = []
    print("\n" + "=" * 95)
    print(f"{'#':>3}  {'Date':<8}  {'T1':<5} {'T2':<5}  {'Venue':<42}  {'Prob':>9}  {'Winner':<5}  Margin")
    print("=" * 95)
    for f in FIXTURES:
        if "TBD" in f.get("t1","") or "TBD" in f.get("t2",""): continue
        neutral = f.get("neutral", False)
        phase   = f.get("phase", "League")
        res     = predict_match(f["t1"], f["t2"], f["venue"], neutral)
        tag     = f"  [{f['phase']}]" if "phase" in f else ""
        print(f"{f['match']:>3}  {f['date']:<8}  {f['t1']:<5} {f['t2']:<5}  "
              f"{f['venue'][:42]:<42}  "
              f"{res['w1']:>3}%-{res['w2']:<3}%  "
              f"{res['winner']:<5}  {res['margin']}{tag}")
        results.append({
            "match_no": f["match"], "date": f["date"], "phase": phase,
            "team1": f["t1"], "team2": f["t2"], "venue": f["venue"],
            "pitch_type": res["pitch_type"], "dew_factor": res["dew_factor"],
            "avg_first_inn": res["avg_first_innings"],
            "win_prob_t1": res["w1"], "win_prob_t2": res["w2"],
            "predicted_winner": res["winner"], "margin": res["margin"],
            "key_factors": " | ".join(res["factors"]),
        })
    print("=" * 95)
    print(f"\nTotal matches predicted: {len(results)}")
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader(); writer.writerows(results)
    print(f"Saved -> {OUTPUT_FILE}\n")
    return results

if __name__ == "__main__":
    run()
