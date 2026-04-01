"""IPL 2026 - Master Runner
Runs all scripts in order and produces every output CSV.

Usage:
    python run_all.py
    python run_all.py --sims 50000
"""
import sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sims", type=int, default=10_000)
    args = parser.parse_args()

    print("\n" + "█"*60)
    print("  IPL 2026 PREDICTOR - FULL PIPELINE")
    print("█"*60)

    print("\n[1/3] Venue & pitch conditions report...")
    from scripts.venue_report import run as venue_run
    venue_run()

    print("[2/3] Predicting all 70 matches...")
    from scripts.predict_all_matches import run as predict_run
    predict_run()

    print(f"[3/4] Monte Carlo simulation ({args.sims:,} iterations)...")

    from scripts.simulate_season import run as sim_run
    sim_run(args.sims)

    print("[4/4] Running ML models (Logistic Regression + Random Forest + Gradient Boosting)...")
    from scripts.ml_model import run as ml_run
    ml_run(predict=True)

    print("█"*60)
    print("  DONE - output files in /data/")
    print("  * data/venue_conditions.csv")
    print("  * data/match_predictions_2026.csv")
    print("  * data/points_table_2026.csv")
    print("  * data/title_probabilities.csv")
    print("█"*60 + "\n")

if __name__ == "__main__":
    main()
