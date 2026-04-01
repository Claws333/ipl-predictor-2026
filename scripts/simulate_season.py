"""IPL 2026 - Monte Carlo Season Simulator
Usage:
    python scripts/simulate_season.py
    python scripts/simulate_season.py --sims 50000
"""
import os, sys, csv, random, argparse
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.schedule import FIXTURES
from data.teams import TEAMS
from scripts.engine import predict_match

def simulate_one_season(rng):
    wins = defaultdict(int); losses = defaultdict(int); nrr = defaultdict(float)
    league = [f for f in FIXTURES if "phase" not in f]
    for f in league:
        res = predict_match(f["t1"], f["t2"], f["venue"], f.get("neutral", False))
        if rng.uniform(0, 100) < res["w1"]:
            winner, loser = f["t1"], f["t2"]
            nrr[f["t1"]] += rng.uniform(0.1, 0.8); nrr[f["t2"]] -= rng.uniform(0.1, 0.8)
        else:
            winner, loser = f["t2"], f["t1"]
            nrr[f["t2"]] += rng.uniform(0.1, 0.8); nrr[f["t1"]] -= rng.uniform(0.1, 0.8)
        wins[winner] += 1; losses[loser] += 1
    return wins, losses, nrr

def simulate_playoffs(top4, rng):
    neutral_venue = "Narendra Modi Stadium, Ahmedabad"
    q1  = predict_match(top4[0], top4[1], neutral_venue, neutral=True)
    q1w = top4[0] if rng.uniform(0,100) < q1["w1"] else top4[1]
    q1l = top4[1] if q1w == top4[0] else top4[0]
    el  = predict_match(top4[2], top4[3], neutral_venue, neutral=True)
    elw = top4[2] if rng.uniform(0,100) < el["w1"] else top4[3]
    q2  = predict_match(q1l, elw, neutral_venue, neutral=True)
    fin2 = q1l if rng.uniform(0,100) < q2["w1"] else elw
    final = predict_match(q1w, fin2, neutral_venue, neutral=True)
    return q1w if rng.uniform(0,100) < final["w1"] else fin2

def run(n_sims=10_000):
    print(f"\nRunning {n_sims:,} Monte Carlo simulations...\n")
    title_wins = defaultdict(int); cum_pts = defaultdict(int)
    cum_nrr = defaultdict(float); playoff_apps = defaultdict(int)
    rng = random.Random(42)
    for i in range(n_sims):
        wins, losses, nrr = simulate_one_season(rng)
        standings = sorted(TEAMS.keys(), key=lambda t: (wins[t]*2, nrr[t]), reverse=True)
        top4 = standings[:4]
        for t in top4: playoff_apps[t] += 1
        for t in TEAMS: cum_pts[t] += wins[t]*2; cum_nrr[t] += nrr[t]
        title_wins[simulate_playoffs(top4, rng)] += 1
        if (i+1) % (n_sims//5) == 0:
            print(f"  {i+1:,} / {n_sims:,} done...")

    table = []
    for t in TEAMS:
        avg_pts = cum_pts[t]/n_sims; avg_w = avg_pts/2
        table.append({
            "team": t, "name": TEAMS[t]["name"],
            "avg_wins": round(avg_w,1), "avg_losses": round(14-avg_w,1),
            "avg_points": round(avg_pts,1), "avg_nrr": round(cum_nrr[t]/n_sims,3),
            "playoff_pct": round(playoff_apps[t]/n_sims*100,1),
            "title_pct": round(title_wins[t]/n_sims*100,1),
        })
    table.sort(key=lambda r: r["avg_points"], reverse=True)

    print("\n" + "=" * 78)
    print(f"{'#':<3} {'Team':<5} {'Name':<28} {'Pts':>5} {'W':>4} {'NRR':>6}  {'Playoff%':>8}  {'Title%':>6}")
    print("=" * 78)
    for i, r in enumerate(table, 1):
        bracket = "[Q]" if r["playoff_pct"] >= 50 else "   "
        print(f"{i:<3} {r['team']:<5} {r['name']:<28} {r['avg_points']:>5} "
              f"{r['avg_wins']:>4} {r['avg_nrr']:>+6.2f}  "
              f"{r['playoff_pct']:>7}%  {r['title_pct']:>5}%  {bracket}")
    print("=" * 78)

    print("\nTitle probabilities:")
    for t, w in sorted(title_wins.items(), key=lambda x: x[1], reverse=True)[:6]:
        pct = round(w/n_sims*100,1); bar = "█" * int(pct/2)
        print(f"  {t:<5}  {pct:>5}%  {bar}")

    os.makedirs("data", exist_ok=True)
    pts_file = os.path.join("data","points_table_2026.csv")
    with open(pts_file,"w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=table[0].keys()); w.writeheader(); w.writerows(table)
    ttl_file = os.path.join("data","title_probabilities.csv")
    with open(ttl_file,"w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["team","name","title_wins","title_pct"])
        w.writeheader()
        for t, tw in sorted(title_wins.items(), key=lambda x: x[1], reverse=True):
            w.writerow({"team":t,"name":TEAMS[t]["name"],"title_wins":tw,"title_pct":round(tw/n_sims*100,1)})
    print(f"\nPoints table  -> {pts_file}")
    print(f"Title probs   -> {ttl_file}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sims", type=int, default=10_000)
    args = parser.parse_args()
    run(args.sims)
