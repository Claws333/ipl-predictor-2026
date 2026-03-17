# IPL 2026 Predictor & Season Simulator 🏏

A data-driven IPL prediction engine that simulates matches and seasons using player stats, team composition, venue conditions, and probabilistic modeling.

Currently in **alpha phase** — focused on the early part of IPL 2026 (post-mega auction, March–April 2026).

---

## What This Project Does

- Predicts IPL match winners  
- Calculates realistic win probabilities  
- Generates balanced playing XIs  
- Simulates points tables and title probabilities  
- Runs Monte Carlo simulations for season outcomes  

---

## How It Works

1. **Player Scoring**  
   Each player receives a composite score:  

   Score = 0.35 × Power + 0.25 × Innovation + 0.20 × Acceleration + 2 × Form + 10 × StarterWeight

- Power: hitting ability  
- Innovation: shot variety / creativity  
- Acceleration: scoring rate under pressure  
- Form: recent performance weight  
- StarterWeight: likelihood to be in playing XI  

2. **Playing XI Generation**  
- Select best players per role  
- Enforce IPL rules: max 4 overseas players  
- Prioritize core / retained players  
- Balance batting, bowling, all-rounders  

3. **Match Prediction**  
- Team strength = sum of selected players' scores  
- Apply adjustments:  
  - Venue conditions  
  - Dew factor  
  - Home advantage  
- Output: win percentage for each team  

4. **Season Simulation**  
- Predict match-by-match results  
- Generate projected points table  
- Run multiple Monte Carlo iterations  
- Estimate title / playoff probabilities  

---

## Example Output

**Sample Match Predictions**  
- RCB vs SRH → RCB win probability: 53%  
- MI vs KKR → KKR win probability: 52%  
- CSK vs GT → CSK win probability: 58%  

**Sample Simulated Points Table (after 4 matches)**  

| Rank | Team                  | Played | Won | Lost | Points | NRR    |
|------|-----------------------|--------|-----|------|--------|--------|
| 1    | Kolkata Knight Riders | 4      | 4   | 0    | 8      | +1.45  |
| 2    | Mumbai Indians        | 4      | 3   | 1    | 6      | +0.82  |
| 3    | Chennai Super Kings   | 4      | 3   | 1    | 6      | +0.65  |
| 4    | Gujarat Titans        | 4      | 2   | 2    | 4      | -0.12  |
| ...  | ...                   | ...    | ... | ...  | ...    | ...    |

---

## Project Structure

(Current alpha layout – files mostly in root)

├── 2026_first_phase/
│   ├── data/                          # (or root files)
│   │   ├── best_playing_xi_2026.csv          # Best-score variant output
│   │   ├── best_playing_xi_realistic_2026.csv # Realistic XI output
│   │   ├── match_predictions.csv             # Predicted winners/probabilities
│   │   ├── match_schedule.csv                # IPL 2026 fixtures (phase 1)
│   │   ├── new_player_db_2026.csv            # 2026 player database
│   │   ├── player_scores.csv                 # Rated players with Role/Overseas/Form
│   │   ├── points_table_prediction.csv       # Projected points table
│   │   ├── predicted_playing_xi.csv          # Generated XIs
│   │   └── venue_conditions.csv              # Dew/pitch/home advantage
│   └── scripts/
│       ├── generate_best_xi.py               # Score-based XI generator
│       ├── generate_playing_xi.py            # Main realistic generator
│       ├── generate_realistic_xi.py          # Form/random variant
│       ├── ipl_squad_scraper.py              # Squad fetch/update (optional)
│       ├── locked_players.py                 # Retained/locked players
│       ├── predict_match.py                  # Match prediction logic
│       └── simulate_season.py                # Season simulation (Monte Carlo ready)
└── README.md                                 # This file
text

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Claws333/ipl-predictor-2026.git
cd ipl-predictor-2026

# 2. Install dependencies
pip install pandas numpy

# 3. (Optional) Update squads / player data
python ipl_squad_scraper.py

# 4. Calculate player scores
python calculate_player_scores.py

# 5. Generate playing XIs
python generate_playing_xi.py          # or generate_realistic_xi.py

# 6. Predict one match (edit teams inside script if needed)
python predict_match.py

# 7. Simulate the phase / season
python simulate_season.py

All output CSVs are saved in the root folder.

## Limitations (Alpha Phase)

- Simplified player metrics (no detailed batter-bowler matchups yet)  
- Partial schedule used (full 84-match simulation planned)  
- No live / real-time data integration  
- Predictions are probabilistic estimates — for entertainment & learning  

## Future Improvements

- Full post-auction squad integration  
- Detailed batter vs bowler matchup modeling  
- Live playing XI scraping  
- Real-time win probability during matches  
- Web dashboard / visualizations  

## Purpose

Built as a personal learning project exploring:  
- Sports analytics  
- Probabilistic modeling  
- Cricket strategy & team composition  

Feedback, suggestions, and pull requests are very welcome! 🚀
