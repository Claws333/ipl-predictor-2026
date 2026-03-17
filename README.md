🏏 IPL 2026 Predictor \& Simulator 



A data-driven IPL prediction engine that simulates match outcomes and full seasons using player stats, team composition, and probabilistic modeling.



🚀 IPL 2026 First Phase Release (20 Matches)



Status: First 20 matches (28 Mar – 12 Apr 2026) released by BCCI

Files: All in folder 2026\_first\_phase/



What's New



Real 2026 squads + retentions (from auction)



Realistic Playing XI (Wisden-guided + score-based + role balance)



Player scores with Role, Overseas, Form \& Starter Weight



Match predictions with venue dew \& home advantage



Projected points table after first phase



How to Run (First Phase)

cd 2026\_first\_phase

python predict\_match.py

🔥 What This Project Does



Predicts IPL match winners



Calculates win probabilities



Simulates points table standings



Runs Monte Carlo simulations for title prediction



⚙️ How It Works


1️⃣ Player Scoring



Each player is assigned a score based on:



Power → hitting ability



Innovation → shot variety



Acceleration → scoring rate



Form → recent performance



StarterWeight → likelihood of playing XI



Score = 0.35×Power + 0.25×Innovation + 0.20×Acceleration + 2×Form + 10×StarterWeight



2️⃣ Playing XI Generation



Selects top players based on score



Enforces max 4 overseas players



Prioritizes core/locked players



Maintains role balance (WK, BAT, AR, BOWL)





3️⃣ Match Prediction



Team strength is calculated as:



TeamStrength = sum(Player Scores)



Adjustments applied:



📍 Venue conditions



💧 Dew factor (chasing advantage)



🏠 Home ground advantage





4️⃣ Season Simulation



Predicts match results across schedule



Generates points table



Simulates season outcomes



📊 Example Output

RCB vs SRH → RCB (53%)

MI vs KKR → KKR (52%)

Team                     Points

Kolkata Knight Riders    8

Mumbai Indians           6

Chennai Super Kings      6



📁 Project Structure



ipl\_predictor/

│

├ 2026\_first\_phase/

│   ├ match\_schedule.csv

│   ├ predicted\_playing\_xi.csv

│   ├ player\_scores.csv

│   ├ venue\_conditions.csv

│   ├ predict\_match.py

│   └ simulate\_season.py

│

├ calculate\_player\_scores.py

├ generate\_playing\_xi.py

├ simulate\_montecarlo\_season.py

🚀 How to Run (Full Pipeline)

python calculate\_player\_scores.py

python generate\_playing\_xi.py

python predict\_match.py

python simulate\_season.py



⚠️ Limitations



Uses simplified player metrics



Playing XI predictions are approximate



Currently uses partial IPL schedule (first phase)



No live data integration yet





🔮 Future Improvements



Live playing XI scraping



Batter vs bowler matchup modeling



Full IPL schedule simulation (70 matches)



Real-time win probability engine




💡 Purpose



Built as a learning project exploring:



Sports analytics



Probabilistic modeling



Cricket strategy

