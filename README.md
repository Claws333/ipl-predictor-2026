<div align="center">

<img src="https://img.shields.io/badge/IPL-2026-FF6B00?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Matches-70-1D9E75?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ML-3_Models-9B59B6?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Monte_Carlo-10K_sims-E74C3C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/CV_Accuracy-90.7%25-27AE60?style=for-the-badge"/>

# 🏏 IPL 2026 Predictor & Season Simulator

**Predicts all 70 IPL 2026 matches using two approaches: a rule-based engine (pitch, dew, home advantage, H2H) and three trained ML models (Logistic Regression, Random Forest, Gradient Boosting). Results are combined into a consensus prediction.**

[Features](#-features) • [How It Works](#-how-it-works) • [ML Models](#-machine-learning-models) • [Quick Start](#-quick-start) • [Scripts](#-scripts) • [Outputs](#-output-files) • [Teams](#-team-codes)

</div>

---

## ✨ Features

| | Feature | Detail |
|---|---|---|
| 🤖 | **3 ML models** | Logistic Regression, Random Forest, Gradient Boosting — trained on 107 historical IPL matches |
| 📐 | **Rule-based engine** | Pitch type, dew factor, home advantage, head-to-head history |
| 🗳️ | **Consensus prediction** | All 4 models vote — majority wins |
| 🏟️ | **All 70 matches** | Real 2026 schedule — starts 28 Mar (RCB vs SRH) |
| 🏠 | **Home advantage** | Per-team multipliers — CSK at Chepauk = 1.14× (highest) |
| 💧 | **Dew factor** | High dew = chasing side +3%, Medium = +1.5% |
| 📊 | **Head-to-head** | 28 classic rivalry win-rates baked in |
| 🎲 | **Monte Carlo** | Full playoff bracket simulated 10,000+ times |
| 📁 | **5 CSV outputs** | Predictions, ML predictions, venues, points table, title odds |

---

## ⚙️ How It Works

The engine runs **two independent prediction systems** and combines them:

```
┌─────────────────────────────────┐    ┌──────────────────────────────────────┐
│       RULE-BASED ENGINE         │    │         MACHINE LEARNING              │
│                                 │    │                                        │
│  composite_score =              │    │  Features:                            │
│    batting   × 0.35             │    │    team strength diff                 │
│  + bowling   × 0.30             │    │    home advantage flag                │
│  + allround  × 0.20             │    │    recent form (last 5 games)         │
│  + form      × 0.15             │    │    head-to-head win %                 │
│                                 │    │    avg first innings at venue         │
│  × home_advantage (1.06–1.14)   │    │    dew factor (numeric)               │
│  × pitch_bias                   │    │    form difference (engineered)       │
│  × dew_factor                   │    │    strength difference (engineered)   │
│  × h2h_nudge                    │    │                                        │
│                                 │    │  Models trained on 107 IPL matches    │
│                                 │    │  (2022–2025 seasons)                  │
└──────────────┬──────────────────┘    └────────────────┬─────────────────────┘
               │                                        │
               └──────────────────┬─────────────────────┘
                                  ▼
                       CONSENSUS PREDICTION
                    (average of all 4 outputs)
```

> Win probabilities are **capped at 72/28** across all models.

---

## 🤖 Machine Learning Models

Three models are trained using `scikit-learn` on 107 historical IPL match results spanning 2022–2025:

| Model | Cross-Val Accuracy | Description |
|---|---|---|
| **Logistic Regression** | **90.7% ± 2.8%** | Fast, interpretable — shows exact feature weights |
| **Random Forest** | **89.8% ± 6.7%** | 200 decision trees, captures non-linear patterns |
| **Gradient Boosting** | **85.1% ± 7.4%** | Boosted trees, catches subtle feature interactions |

### What the models learned

The Random Forest ranked features by importance — here's what actually drives IPL match outcomes according to the data:

```
form_diff          ████████████████  41.0%   ← biggest factor by far
t1_form            ████████          21.3%
t2_form            ███████           19.2%
h2h_win_pct        ██                 6.7%
strength_diff      █                  4.8%
home_advantage     █                  2.2%
```

**Key insight:** Recent form (last 5 matches) explains over 60% of outcomes. Raw team strength matters much less than momentum.

### Where ML disagrees with rules

The ML consensus disagrees with the rule-based engine on ~23% of matches — those are the most interesting predictions where data overrides assumptions. For example:

- **Match 1** (RCB vs SRH): Rules favour RCB (home), ML favours SRH (better form)
- **Match 11** (RCB vs CSK): Rules favour RCB (home), ML strongly favours CSK (H2H history + form)
- **Match 60** (SRH vs KKR): Rules favour SRH (home), ML favours KKR (dominant form)

---

## 🚀 Quick Start

```bash
git clone https://github.com/Claws333/ipl-predictor-2026.git
cd ipl-predictor-2026

# Install dependencies (only needed for ML models)
pip install -r requirements.txt

# Run everything — rule engine + ML + Monte Carlo
python run_all.py

# Higher accuracy simulation
python run_all.py --sims 50000
```

---

## 📜 Scripts

| Script | What it does |
|---|---|
| `python run_all.py` | Runs all 4 steps in order |
| `python scripts/predict_all_matches.py` | Rule-based predictions for all 70 matches |
| `python scripts/ml_model.py` | Train ML models + predict all 70 matches |
| `python scripts/simulate_season.py` | Monte Carlo season + playoff simulation |
| `python scripts/venue_report.py` | Detailed pitch & venue conditions |
| `python scripts/predict_match.py` | Interactive single match predictor |

**Single match — command line:**
```bash
python scripts/predict_match.py --t1 RCB --t2 SRH --venue "M Chinnaswamy Stadium, Bengaluru"
python scripts/predict_match.py --t1 KKR --t2 MI --venue "Eden Gardens, Kolkata"
python scripts/predict_match.py --t1 KKR --t2 SRH --venue "M Chinnaswamy Stadium, Bengaluru" --neutral
```

**Run only the ML model:**
```bash
python scripts/ml_model.py
```

---

## 📁 Output Files

| File | Description |
|---|---|
| `data/match_predictions_2026.csv` | Rule-based predictions — win%, winner, pitch, dew, key factors |
| `data/ml_predictions_2026.csv` | All 4 model outputs + consensus for every match |
| `data/venue_conditions.csv` | Pitch type, avg first innings, dew factor — all 13 venues |
| `data/points_table_2026.csv` | Predicted standings with NRR, playoff%, title% |
| `data/title_probabilities.csv` | Monte Carlo title winner odds per team |

---

## 🗂️ Project Structure

```
ipl-predictor-2026/
├── data/
│   ├── teams.py                      ← team strengths, venues, H2H data
│   ├── schedule.py                   ← real 2026 fixtures (starts 28 Mar)
│   ├── historical_results.py         ← 107 IPL matches used to train ML
│   ├── match_predictions_2026.csv    ← [generated] rule-based
│   ├── ml_predictions_2026.csv       ← [generated] ML + consensus
│   ├── venue_conditions.csv          ← [generated]
│   ├── points_table_2026.csv         ← [generated]
│   └── title_probabilities.csv       ← [generated]
├── scripts/
│   ├── engine.py                     ← rule-based prediction logic
│   ├── ml_model.py                   ← ML training + prediction (NEW)
│   ├── predict_match.py              ← single match predictor
│   ├── predict_all_matches.py        ← all 70 rule-based predictions
│   ├── simulate_season.py            ← Monte Carlo simulator
│   └── venue_report.py               ← venue pitch report
├── run_all.py                        ← master runner (4 steps)
├── requirements.txt                  ← scikit-learn, pandas, numpy
└── README.md
```

---

## 🎽 Team Codes

| Code | Team | Home Ground |
|---|---|---|
| `MI` | Mumbai Indians | Wankhede Stadium, Mumbai |
| `CSK` | Chennai Super Kings | MA Chidambaram Stadium, Chennai |
| `RCB` | Royal Challengers Bengaluru | M Chinnaswamy Stadium, Bengaluru |
| `KKR` | Kolkata Knight Riders | Eden Gardens, Kolkata |
| `SRH` | Sunrisers Hyderabad | Rajiv Gandhi Intl, Hyderabad |
| `DC` | Delhi Capitals | Arun Jaitley Stadium, Delhi |
| `PBKS` | Punjab Kings | PCA Stadium, New Chandigarh |
| `RR` | Rajasthan Royals | Sawai Mansingh Stadium, Jaipur |
| `GT` | Gujarat Titans | Narendra Modi Stadium, Ahmedabad |
| `LSG` | Lucknow Super Giants | BRSABV Ekana Stadium, Lucknow |

---

## 🏟️ Venues at a Glance

| Venue | Pitch | Avg 1st Inn | Dew |
|---|---|---|---|
| Wankhede, Mumbai | 🔴 Batting paradise | 185 | High |
| Chinnaswamy, Bengaluru | 🔴 Batting paradise | 192 | Low |
| Rajiv Gandhi, Hyderabad | 🟠 Batting-friendly | 178 | High |
| PCA, New Chandigarh | 🟠 Batting-friendly | 178 | Low |
| Sawai Mansingh, Jaipur | 🟠 Batting-friendly | 176 | Low |
| Barsapara, Guwahati | 🟠 Batting-friendly | 172 | Medium |
| Eden Gardens, Kolkata | 🟡 Balanced | 174 | Medium |
| Arun Jaitley, Delhi | 🟡 Balanced | 172 | Low |
| Ekana, Lucknow | 🟡 Balanced | 173 | Medium |
| Chidambaram, Chennai | 🟢 Spin-friendly | 168 | Medium |
| Narendra Modi, Ahmedabad | 🟢 Spin-friendly | 170 | Medium |
| HPCA, Dharamsala | 🔵 Pace-friendly | 165 | None |

---

## 📝 Notes

- ML models require `pip install -r requirements.txt` (scikit-learn, pandas, numpy)
- Rule-based engine has zero dependencies — pure Python stdlib
- Monte Carlo seed fixed at `42` for reproducibility
- Historical dataset covers 107 representative matches from IPL 2022–2025
- Predictions are probabilistic estimates — for learning and entertainment

---

## 🔮 Future Plans

- [ ] Expand training data to full 500+ match historical dataset
- [ ] Batter vs bowler matchup modelling
- [ ] Live squad scraping & real-time form updates
- [ ] Toss influence factor
- [ ] Web dashboard with interactive charts

---

<div align="center">
Built with 🏏 for cricket analytics fans &nbsp;|&nbsp; MIT License
<br><br>
⭐ Star the repo if you find it useful!
</div>
