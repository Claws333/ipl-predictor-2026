"""
IPL 2026 - REAL Full Fixture List
Source: ESPN Cricinfo / BCCI / BBC
Start: 28 March 2026 (RCB vs SRH at Chinnaswamy)
End:   31 May 2026 (Final at Bengaluru)
Total: 74 matches (70 league + 4 playoffs)

Groups:
  Group A: CSK, KKR, RR, RCB, PBKS  (same group plays each other ONCE)
  Group B: MI, SRH, GT, DC, LSG     (opposite group plays each other TWICE)

Venue notes:
  RR early home = Barsapara Cricket Stadium, Guwahati (matches vs CSK & MI)
  RR later home = Sawai Mansingh Stadium, Jaipur
  PBKS early home = PCA Stadium, New Chandigarh
  PBKS later home = HPCA Stadium, Dharamsala
"""

FIXTURES = [
    # ── CONFIRMED FIRST 20 (BBC / BCCI official) ──────────────────────────────
    {"match": 1,  "date": "28 Mar", "t1": "RCB",  "t2": "SRH",  "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 2,  "date": "29 Mar", "t1": "MI",   "t2": "KKR",  "venue": "Wankhede Stadium, Mumbai"},
    {"match": 3,  "date": "30 Mar", "t1": "RR",   "t2": "CSK",  "venue": "Barsapara Cricket Stadium, Guwahati"},
    {"match": 4,  "date": "31 Mar", "t1": "PBKS", "t2": "GT",   "venue": "PCA Stadium, New Chandigarh"},
    {"match": 5,  "date": "01 Apr", "t1": "LSG",  "t2": "DC",   "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 6,  "date": "02 Apr", "t1": "KKR",  "t2": "SRH",  "venue": "Eden Gardens, Kolkata"},
    {"match": 7,  "date": "03 Apr", "t1": "CSK",  "t2": "PBKS", "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 8,  "date": "04 Apr", "t1": "DC",   "t2": "MI",   "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 9,  "date": "04 Apr", "t1": "GT",   "t2": "RR",   "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 10, "date": "05 Apr", "t1": "SRH",  "t2": "LSG",  "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 11, "date": "05 Apr", "t1": "RCB",  "t2": "CSK",  "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 12, "date": "06 Apr", "t1": "KKR",  "t2": "PBKS", "venue": "Eden Gardens, Kolkata"},
    {"match": 13, "date": "07 Apr", "t1": "RR",   "t2": "MI",   "venue": "Barsapara Cricket Stadium, Guwahati"},
    {"match": 14, "date": "08 Apr", "t1": "DC",   "t2": "GT",   "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 15, "date": "09 Apr", "t1": "KKR",  "t2": "LSG",  "venue": "Eden Gardens, Kolkata"},
    {"match": 16, "date": "10 Apr", "t1": "RR",   "t2": "RCB",  "venue": "Sawai Mansingh Stadium, Jaipur"},
    {"match": 17, "date": "11 Apr", "t1": "PBKS", "t2": "SRH",  "venue": "PCA Stadium, New Chandigarh"},
    {"match": 18, "date": "11 Apr", "t1": "CSK",  "t2": "DC",   "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 19, "date": "12 Apr", "t1": "LSG",  "t2": "GT",   "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 20, "date": "12 Apr", "t1": "MI",   "t2": "RCB",  "venue": "Wankhede Stadium, Mumbai"},
    # ── CONFIRMED ORDER from ESPNCricinfo, dates estimated ────────────────────
    {"match": 21, "date": "13 Apr", "t1": "SRH",  "t2": "RR",   "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 22, "date": "14 Apr", "t1": "CSK",  "t2": "KKR",  "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 23, "date": "15 Apr", "t1": "RCB",  "t2": "LSG",  "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 24, "date": "16 Apr", "t1": "MI",   "t2": "PBKS", "venue": "Wankhede Stadium, Mumbai"},
    {"match": 25, "date": "17 Apr", "t1": "GT",   "t2": "KKR",  "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 26, "date": "18 Apr", "t1": "RCB",  "t2": "DC",   "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 27, "date": "19 Apr", "t1": "SRH",  "t2": "CSK",  "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 28, "date": "20 Apr", "t1": "KKR",  "t2": "RR",   "venue": "Eden Gardens, Kolkata"},
    {"match": 29, "date": "21 Apr", "t1": "PBKS", "t2": "LSG",  "venue": "PCA Stadium, New Chandigarh"},
    {"match": 30, "date": "22 Apr", "t1": "GT",   "t2": "MI",   "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 31, "date": "23 Apr", "t1": "SRH",  "t2": "DC",   "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 32, "date": "24 Apr", "t1": "LSG",  "t2": "RR",   "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 33, "date": "25 Apr", "t1": "MI",   "t2": "CSK",  "venue": "Wankhede Stadium, Mumbai"},
    {"match": 34, "date": "26 Apr", "t1": "RCB",  "t2": "GT",   "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 35, "date": "27 Apr", "t1": "DC",   "t2": "PBKS", "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 36, "date": "28 Apr", "t1": "RR",   "t2": "SRH",  "venue": "Sawai Mansingh Stadium, Jaipur"},
    {"match": 37, "date": "29 Apr", "t1": "GT",   "t2": "CSK",  "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 38, "date": "30 Apr", "t1": "LSG",  "t2": "KKR",  "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 39, "date": "01 May", "t1": "DC",   "t2": "RCB",  "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 40, "date": "02 May", "t1": "PBKS", "t2": "RR",   "venue": "HPCA Stadium, Dharamsala"},
    {"match": 41, "date": "03 May", "t1": "MI",   "t2": "SRH",  "venue": "Wankhede Stadium, Mumbai"},
    {"match": 42, "date": "04 May", "t1": "GT",   "t2": "RCB",  "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 43, "date": "05 May", "t1": "RR",   "t2": "DC",   "venue": "Sawai Mansingh Stadium, Jaipur"},
    {"match": 44, "date": "06 May", "t1": "CSK",  "t2": "LSG",  "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 45, "date": "07 May", "t1": "KKR",  "t2": "MI",   "venue": "Eden Gardens, Kolkata"},
    {"match": 46, "date": "08 May", "t1": "SRH",  "t2": "PBKS", "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 47, "date": "09 May", "t1": "RCB",  "t2": "RR",   "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 48, "date": "10 May", "t1": "DC",   "t2": "KKR",  "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 49, "date": "11 May", "t1": "MI",   "t2": "GT",   "venue": "Wankhede Stadium, Mumbai"},
    {"match": 50, "date": "11 May", "t1": "CSK",  "t2": "RCB",  "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 51, "date": "12 May", "t1": "LSG",  "t2": "SRH",  "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 52, "date": "13 May", "t1": "KKR",  "t2": "DC",   "venue": "Eden Gardens, Kolkata"},
    {"match": 53, "date": "14 May", "t1": "PBKS", "t2": "MI",   "venue": "HPCA Stadium, Dharamsala"},
    {"match": 54, "date": "15 May", "t1": "RR",   "t2": "GT",   "venue": "Sawai Mansingh Stadium, Jaipur"},
    {"match": 55, "date": "15 May", "t1": "CSK",  "t2": "SRH",  "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 56, "date": "16 May", "t1": "RCB",  "t2": "PBKS", "venue": "M Chinnaswamy Stadium, Bengaluru"},
    {"match": 57, "date": "17 May", "t1": "DC",   "t2": "LSG",  "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 58, "date": "17 May", "t1": "GT",   "t2": "KKR",  "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 59, "date": "18 May", "t1": "MI",   "t2": "DC",   "venue": "Wankhede Stadium, Mumbai"},
    {"match": 60, "date": "18 May", "t1": "SRH",  "t2": "KKR",  "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 61, "date": "19 May", "t1": "RR",   "t2": "PBKS", "venue": "Sawai Mansingh Stadium, Jaipur"},
    {"match": 62, "date": "20 May", "t1": "LSG",  "t2": "MI",   "venue": "BRSABV Ekana Cricket Stadium, Lucknow"},
    {"match": 63, "date": "20 May", "t1": "CSK",  "t2": "GT",   "venue": "MA Chidambaram Stadium, Chennai"},
    {"match": 64, "date": "21 May", "t1": "KKR",  "t2": "RCB",  "venue": "Eden Gardens, Kolkata"},
    {"match": 65, "date": "22 May", "t1": "DC",   "t2": "SRH",  "venue": "Arun Jaitley Stadium, Delhi"},
    {"match": 66, "date": "22 May", "t1": "PBKS", "t2": "CSK",  "venue": "HPCA Stadium, Dharamsala"},
    {"match": 67, "date": "23 May", "t1": "GT",   "t2": "LSG",  "venue": "Narendra Modi Stadium, Ahmedabad"},
    {"match": 68, "date": "24 May", "t1": "MI",   "t2": "RR",   "venue": "Wankhede Stadium, Mumbai"},
    {"match": 69, "date": "24 May", "t1": "SRH",  "t2": "RCB",  "venue": "Rajiv Gandhi Intl Cricket Stadium, Hyderabad"},
    {"match": 70, "date": "24 May", "t1": "KKR",  "t2": "CSK",  "venue": "Eden Gardens, Kolkata"},
    # ── PLAYOFFS ──────────────────────────────────────────────────────────────
    {"match": 71, "date": "27 May", "t1": "TBD1", "t2": "TBD2", "venue": "M Chinnaswamy Stadium, Bengaluru",
     "phase": "Qualifier 1", "neutral": True},
    {"match": 72, "date": "28 May", "t1": "TBD3", "t2": "TBD4", "venue": "M Chinnaswamy Stadium, Bengaluru",
     "phase": "Eliminator",  "neutral": True},
    {"match": 73, "date": "30 May", "t1": "TBD",  "t2": "TBD",  "venue": "M Chinnaswamy Stadium, Bengaluru",
     "phase": "Qualifier 2", "neutral": True},
    {"match": 74, "date": "31 May", "t1": "TBD",  "t2": "TBD",  "venue": "M Chinnaswamy Stadium, Bengaluru",
     "phase": "Final",       "neutral": True},
]
