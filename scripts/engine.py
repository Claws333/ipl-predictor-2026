"""IPL 2026 - Advanced Match Prediction Engine"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.teams import TEAMS, TEAM_STRENGTH, VENUES, HEAD_TO_HEAD

def team_score(team):
    s = TEAM_STRENGTH[team]
    return s["batting"]*0.35 + s["bowling"]*0.30 + s["allround"]*0.20 + s["form"]*0.15

def predict_match(t1, t2, venue, neutral=False):
    s1, s2 = team_score(t1), team_score(t2)
    v = VENUES.get(venue, VENUES["Wankhede Stadium, Mumbai"])
    factors = []
    adj1, adj2 = s1, s2
    if not neutral:
        if TEAMS[t1]["home"] == venue:
            adj1 *= TEAMS[t1]["home_adv"]; factors.append("Home advantage -> " + t1)
        if TEAMS[t2]["home"] == venue:
            adj2 *= TEAMS[t2]["home_adv"]; factors.append("Home advantage -> " + t2)
    pb = v.get("pitch_bias", {})
    if t1 in pb: adj1 *= pb[t1]; factors.append(f"Pitch ({v['pitch_type']}) -> {t1}")
    if t2 in pb: adj2 *= pb[t2]; factors.append(f"Pitch ({v['pitch_type']}) -> {t2}")
    if v["dew_factor"] == "High":
        adj2 *= 1.03; factors.append("Dew (High) -> " + t2)
    elif v["dew_factor"] == "Medium":
        adj2 *= 1.015; factors.append("Dew (Medium) -> " + t2)
    key = (t1, t2)
    if key in HEAD_TO_HEAD:
        h1_pct, _ = HEAD_TO_HEAD[key]
        adj1 *= (0.90 + (h1_pct/50.0)*0.10)
        factors.append(f"H2H history ({h1_pct}% {t1})")
    total = adj1 + adj2
    raw_w1 = (adj1/total)*100
    w1 = max(28, min(72, round(raw_w1)))
    w2 = 100 - w1
    diff = abs(w1 - w2)
    margin = "close" if diff <= 6 else "moderate" if diff <= 16 else "heavy"
    return {"t1": t1, "t2": t2, "venue": venue, "w1": w1, "w2": w2,
            "winner": t1 if w1 >= w2 else t2, "factors": factors,
            "margin": margin, "avg_first_innings": v["avg_first"],
            "pitch_type": v["pitch_type"], "dew_factor": v["dew_factor"]}
