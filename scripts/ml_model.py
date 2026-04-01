"""
IPL 2026 - Machine Learning Prediction Model
=============================================
Trains TWO models on historical IPL data (2022-2025):
  1. Logistic Regression  — fast, interpretable, shows feature weights
  2. Random Forest        — captures non-linear patterns, more powerful

Features used per match:
  - team1_strength, team2_strength    (from our composite score)
  - team1_home                        (1 or 0)
  - t1_form, t2_form                  (recent win rate 0.0-1.0)
  - h2h_t1_pct                        (historical head-to-head %)
  - avg_first_innings                 (venue scoring avg)
  - dew_numeric                       (0=none, 1=medium, 2=high)
  - strength_diff                     (engineered: t1_score - t2_score)
  - form_diff                         (engineered: t1_form - t2_form)

Usage:
    python scripts/ml_model.py                    # train + evaluate
    python scripts/ml_model.py --predict          # train + predict all 2026 matches
"""

import os, sys, argparse, csv
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline

from data.historical_results import HISTORICAL, COLUMNS
from data.schedule import FIXTURES
from data.teams import TEAMS, VENUES
from scripts.engine import team_score, predict_match

# ─────────────────────────────────────────────────────────────────────────────
# Feature engineering
# ─────────────────────────────────────────────────────────────────────────────

DEW_MAP = {"None": 0, "Low": 0, "Medium": 1, "High": 2}

def build_features_from_row(row):
    t1, t2, venue, t1_home, t1_form, t2_form, h2h, avg_first, dew, _ = row
    s1 = team_score(t1)
    s2 = team_score(t2)
    return [
        s1,                     # team1 composite strength
        s2,                     # team2 composite strength
        s1 - s2,                # strength difference (engineered)
        float(t1_home),         # home advantage flag
        t1_form,                # team1 recent form
        t2_form,                # team2 recent form
        t1_form - t2_form,      # form difference (engineered)
        h2h / 100.0,            # head-to-head win % for team1
        avg_first / 200.0,      # normalised avg first innings score
        float(dew) / 2.0,       # normalised dew factor
    ]

def build_features_for_match(t1, t2, venue, neutral=False):
    """Build features for a live 2026 prediction (no historical result needed)."""
    s1 = team_score(t1)
    s2 = team_score(t2)
    v  = VENUES.get(venue, {})
    dew_raw = DEW_MAP.get(v.get("dew_factor", "Low"), 0)
    avg_first = v.get("avg_first", 175)

    # home flag
    t1_home = 1.0 if (not neutral and TEAMS[t1]["home"] == venue) else 0.0

    # form: use TEAM_STRENGTH form score normalised
    from data.teams import TEAM_STRENGTH
    t1_form = TEAM_STRENGTH[t1]["form"] / 100.0
    t2_form = TEAM_STRENGTH[t2]["form"] / 100.0

    # h2h
    from data.teams import HEAD_TO_HEAD
    h2h_raw = HEAD_TO_HEAD.get((t1, t2), (50, 50))[0] / 100.0

    return [
        s1, s2,
        s1 - s2,
        t1_home,
        t1_form, t2_form,
        t1_form - t2_form,
        h2h_raw,
        avg_first / 200.0,
        float(dew_raw) / 2.0,
    ]

FEATURE_NAMES = [
    "t1_strength", "t2_strength", "strength_diff",
    "t1_home", "t1_form", "t2_form", "form_diff",
    "h2h_t1_pct", "avg_first_inn_norm", "dew_norm",
]

# ─────────────────────────────────────────────────────────────────────────────
# Build dataset
# ─────────────────────────────────────────────────────────────────────────────

def build_dataset():
    X, y = [], []
    for row in HISTORICAL:
        X.append(build_features_from_row(row))
        y.append(row[-1])  # result: 1 = team1 won
    return np.array(X), np.array(y)

# ─────────────────────────────────────────────────────────────────────────────
# Train models
# ─────────────────────────────────────────────────────────────────────────────

def train_models(X, y, verbose=True):
    models = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("clf",    LogisticRegression(C=1.0, max_iter=1000, random_state=42)),
        ]),
        "Random Forest": Pipeline([
            ("scaler", StandardScaler()),
            ("clf",    RandomForestClassifier(n_estimators=200, max_depth=6,
                                              min_samples_leaf=3, random_state=42)),
        ]),
        "Gradient Boosting": Pipeline([
            ("scaler", StandardScaler()),
            ("clf",    GradientBoostingClassifier(n_estimators=150, max_depth=4,
                                                  learning_rate=0.05, random_state=42)),
        ]),
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    trained = {}

    if verbose:
        print("\n" + "="*60)
        print("  ML MODEL TRAINING & CROSS-VALIDATION")
        print("="*60)
        print(f"  Training samples : {len(X)}")
        print(f"  Features         : {len(FEATURE_NAMES)}")
        print(f"  CV folds         : 5\n")

    for name, pipe in models.items():
        scores = cross_val_score(pipe, X, y, cv=cv, scoring="accuracy")
        pipe.fit(X, y)
        trained[name] = pipe
        if verbose:
            print(f"  {name:<25}  CV Accuracy: {scores.mean():.3f} ± {scores.std():.3f}")

    if verbose:
        # Feature importance from RF
        rf_clf = trained["Random Forest"].named_steps["clf"]
        importances = rf_clf.feature_importances_
        sorted_idx  = np.argsort(importances)[::-1]
        print("\n  Random Forest — top feature importances:")
        for i in sorted_idx[:6]:
            bar = "█" * int(importances[i] * 40)
            print(f"    {FEATURE_NAMES[i]:<22}  {importances[i]:.3f}  {bar}")

        # LR coefficients
        lr_clf  = trained["Logistic Regression"].named_steps["clf"]
        coefs   = lr_clf.coef_[0]
        sorted_c = np.argsort(np.abs(coefs))[::-1]
        print("\n  Logistic Regression — top feature coefficients:")
        for i in sorted_c[:6]:
            direction = "+" if coefs[i] > 0 else "-"
            print(f"    {FEATURE_NAMES[i]:<22}  {coefs[i]:+.3f}  (favours team1 if {direction}ve)")

        print("="*60)

    return trained

# ─────────────────────────────────────────────────────────────────────────────
# Predict all 2026 matches with ML + compare to rule-based engine
# ─────────────────────────────────────────────────────────────────────────────

def predict_all_2026(trained_models, verbose=True):
    results = []

    if verbose:
        print("\n" + "="*100)
        print(f"{'#':>3}  {'Date':<8}  {'T1':<5}{'T2':<5}  "
              f"{'Rule-based':^12}  {'Log.Reg':^10}  {'Rnd.Forest':^12}  {'Grad.Boost':^12}  {'CONSENSUS':^10}")
        print("="*100)

    for f in FIXTURES:
        t1, t2 = f.get("t1"), f.get("t2")
        if not t1 or not t2 or "TBD" in t1 or "TBD" in t2:
            continue

        neutral = f.get("neutral", False)
        venue   = f["venue"]

        # Rule-based
        rb  = predict_match(t1, t2, venue, neutral)
        rb_w1, rb_winner = rb["w1"], rb["winner"]

        # ML features
        feat = np.array([build_features_for_match(t1, t2, venue, neutral)])

        ml_preds = {}
        for name, pipe in trained_models.items():
            prob  = pipe.predict_proba(feat)[0]
            # prob[1] = P(team1 wins)
            w1_ml = round(prob[1] * 100)
            w1_ml = max(28, min(72, w1_ml))
            ml_preds[name] = (w1_ml, 100 - w1_ml, t1 if w1_ml >= 50 else t2)

        # Consensus: average all 4 (rule + 3 ML)
        all_w1 = [rb_w1] + [ml_preds[n][0] for n in ml_preds]
        cons_w1 = round(sum(all_w1) / len(all_w1))
        cons_w2 = 100 - cons_w1
        cons_winner = t1 if cons_w1 >= 50 else t2

        if verbose:
            lr   = ml_preds["Logistic Regression"]
            rf   = ml_preds["Random Forest"]
            gb   = ml_preds["Gradient Boosting"]
            phase_tag = f"[{f['phase']}]" if "phase" in f else ""
            print(
                f"{f['match']:>3}  {f['date']:<8}  {t1:<5}{t2:<5}  "
                f"  {rb_w1:>3}%-{100-rb_w1:<3}%  "
                f"  {lr[0]:>3}%-{lr[1]:<3}%  "
                f"  {rf[0]:>3}%-{rf[1]:<3}%  "
                f"  {gb[0]:>3}%-{gb[1]:<3}%  "
                f"  {cons_w1:>3}%-{cons_w2}%  {cons_winner} {phase_tag}"
            )

        results.append({
            "match_no":          f["match"],
            "date":              f["date"],
            "phase":             f.get("phase", "League"),
            "team1":             t1,
            "team2":             t2,
            "venue":             venue,
            "rulebased_w1":      rb_w1,
            "rulebased_w2":      100 - rb_w1,
            "rulebased_winner":  rb_winner,
            "lr_w1":             ml_preds["Logistic Regression"][0],
            "rf_w1":             ml_preds["Random Forest"][0],
            "gb_w1":             ml_preds["Gradient Boosting"][0],
            "consensus_w1":      cons_w1,
            "consensus_w2":      cons_w2,
            "consensus_winner":  cons_winner,
        })

    if verbose:
        print("="*100)
        # Agreement check
        agree = sum(1 for r in results if r["rulebased_winner"] == r["consensus_winner"])
        print(f"\n  Rule-based vs Consensus agreement: {agree}/{len(results)} matches ({round(agree/len(results)*100)}%)")
        disagree = [r for r in results if r["rulebased_winner"] != r["consensus_winner"]]
        if disagree:
            print(f"  Matches where ML disagrees with rule-based engine:")
            for r in disagree:
                print(f"    Match {r['match_no']:>2}  {r['team1']} vs {r['team2']}  "
                      f"Rule: {r['rulebased_winner']}  ML consensus: {r['consensus_winner']}")

    return results

# ─────────────────────────────────────────────────────────────────────────────
# Save results
# ─────────────────────────────────────────────────────────────────────────────

def save_results(results):
    out = os.path.join("data", "ml_predictions_2026.csv")
    os.makedirs("data", exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=results[0].keys())
        w.writeheader()
        w.writerows(results)
    print(f"\n  ML predictions saved -> {out}\n")

# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def run(predict=True):
    X, y = build_dataset()
    trained = train_models(X, y, verbose=True)
    if predict:
        results = predict_all_2026(trained, verbose=True)
        save_results(results)
    return trained

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IPL 2026 ML Prediction Model")
    parser.add_argument("--predict", action="store_true", default=True,
                        help="Predict all 2026 matches after training")
    args = parser.parse_args()
    run(predict=args.predict)
