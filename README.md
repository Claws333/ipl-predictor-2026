<div align="center">

<img src="https://img.shields.io/badge/IPL-2026-FF6B00?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Matches-70-1D9E75?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Monte_Carlo-10K_sims-9B59B6?style=for-the-badge"/>
<img src="https://img.shields.io/badge/No_Dependencies-stdlib_only-E74C3C?style=for-the-badge"/>

# 🏏 IPL 2026 Predictor & Season Simulator

**Predicts all 70 IPL 2026 matches using pitch conditions, home advantage, dew factor, and head-to-head history.**

[Features](#-features) • [How It Works](#-how-it-works) • [Quick Start](#-quick-start) • [Scripts](#-scripts) • [Outputs](#-output-files) • [Teams](#-team-codes)

</div>

---

## ✨ Features

| | Feature | Detail |
|---|---|---|
| 🏟️ | **All 70 matches** | 67 league + Qualifier 1 + Eliminator + Final |
| 🏠 | **Home advantage** | Per-team multiplier — CSK at Chepauk = 1.14× (highest) |
| 🏏 | **Pitch type bias** | 6 pitch types with team-specific boosts |
| 💧 | **Dew factor** | High dew = chasing side +3%, Medium = +1.5% |
| 📊 | **Head-to-head history** | 28 classic rivalry win-rates baked in |
| 🎯 | **Neutral venue flag** | Finals don't apply home advantage |
| 🎲 | **Monte Carlo simulation** | Full playoff bracket simulated 10,000+ times |
| 📁 | **4 CSV outputs** | Predictions, venues, points table, title odds |

---

## ⚙️ How It Works

```
Win Probability = f(
  batting×0.35 + bowling×0.30 + allround×0.20 + form×0.15   ← team strength
  + home advantage multiplier (1.06× – 1.14×)                ← venue
  + pitch type bias (batting/spin/pace paradise)              ← conditions
  + dew factor (High +3%, Medium +1.5%)                       ← weather
  + head-to-head history nudge                                ← rivalry
)
```
> Probabilities are capped at **72/28** — no match is ever a foregone conclusion.

---

## 🚀 Quick Start

```bash
git clone https://github.com/Claws333/ipl-predictor-2026.git
cd ipl-predictor-2026

# Run everything — no pip install needed, pure Python stdlib
python run_all.py

# Higher accuracy (slower)
python run_all.py --sims 50000
```

---

## 📜 Scripts

| Script | What it does |
|---|---|
| `python run_all.py` | Runs all 3 scripts in order |
| `python scripts/predict_all_matches.py` | Prints + saves all 70 match predictions |
| `python scripts/simulate_season.py` | Monte Carlo season + playoff simulation |
| `python scripts/venue_report.py` | Detailed pitch & venue conditions report |
| `python scripts/predict_match.py` | Interactive single match predictor |

**Single match — command line:**
```bash
python scripts/predict_match.py --t1 MI --t2 CSK --venue "Wankhede Stadium, Mumbai"
python scripts/predict_match.py --t1 KKR --t2 SRH --venue "Narendra Modi Stadium, Ahmedabad" --neutral
```

---

## 📁 Output Files

| File | Description |
|---|---|
| `data/match_predictions_2026.csv` | All 70 matches — win%, winner, pitch, dew, key factors |
| `data/venue_conditions.csv` | Pitch type, avg first innings, dew, home team — 11 venues |
| `data/points_table_2026.csv` | Predicted standings with NRR, playoff%, title% |
| `data/title_probabilities.csv` | Monte Carlo title winner odds per team |

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
| `PBKS` | Punjab Kings | HPCA Stadium, Dharamsala |
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
| PCA, Mohali | 🟠 Batting-friendly | 179 | Low |
| Sawai Mansingh, Jaipur | 🟠 Batting-friendly | 176 | Low |
| Eden Gardens, Kolkata | 🟡 Balanced | 174 | Medium |
| Arun Jaitley, Delhi | 🟡 Balanced | 172 | Low |
| Ekana, Lucknow | 🟡 Balanced | 173 | Medium |
| Chidambaram, Chennai | 🟢 Spin-friendly | 168 | Medium |
| Narendra Modi, Ahmedabad | 🟢 Spin-friendly | 170 | Medium |
| HPCA, Dharamsala | 🔵 Pace-friendly | 165 | None |

---

## 🗂️ Project Structure

```
ipl-predictor-2026/
├── data/
│   ├── teams.py                      ← team strengths, venues, H2H
│   ├── schedule.py                   ← all 70 fixtures
│   ├── match_predictions_2026.csv    ← [generated]
│   ├── venue_conditions.csv          ← [generated]
│   ├── points_table_2026.csv         ← [generated]
│   └── title_probabilities.csv       ← [generated]
├── scripts/
│   ├── engine.py                     ← core prediction logic
│   ├── predict_match.py              ← single match predictor
│   ├── predict_all_matches.py        ← all 70 predictions
│   ├── simulate_season.py            ← Monte Carlo simulator
│   └── venue_report.py               ← venue pitch report
├── run_all.py                        ← master runner
└── README.md
```

---

## 📝 Notes

- Pure Python 3.8+ — no external libraries needed
- Monte Carlo seed fixed at `42` for reproducibility
- Predictions are probabilistic estimates — for learning and entertainment

---

<div align="center">
Built with 🏏 for cricket analytics fans &nbsp;|&nbsp; MIT License
<br><br>
⭐ Star the repo if you find it useful!
</div>
