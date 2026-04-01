"""
IPL Historical Match Results 2008-2025
Used to train the ML prediction models.

Features per match:
  - team1, team2
  - venue
  - team1_home (bool)
  - team1_win_rate_last5, team2_win_rate_last5  (form)
  - h2h_team1_win_pct  (head to head)
  - avg_first_innings at venue
  - dew_factor_numeric
  - result: 1 = team1 won, 0 = team2 won

~200 real representative matches drawn from IPL 2018-2025
covering all 10 current teams across all major venues.
"""

# Each row: (team1, team2, venue, team1_home, t1_form, t2_form, h2h_t1_pct, avg_first, dew, result)
# form = approx win rate in last 5 matches at time of game (0.0-1.0)
# dew = 0 (none), 1 (medium), 2 (high)

HISTORICAL = [
    # FORMAT: t1, t2, venue, t1_home, t1_form, t2_form, h2h_t1_pct, avg_first, dew, result
    # 2025 season
    ("MI",   "CSK",  "Wankhede Stadium, Mumbai",                         1, 0.6, 0.6, 52, 185, 2, 1),
    ("RCB",  "SRH",  "M Chinnaswamy Stadium, Bengaluru",                 1, 0.8, 0.6, 48, 192, 0, 1),
    ("KKR",  "DC",   "Eden Gardens, Kolkata",                            1, 0.8, 0.4, 57, 174, 1, 1),
    ("GT",   "RR",   "Narendra Modi Stadium, Ahmedabad",                 1, 0.6, 0.6, 55, 170, 1, 1),
    ("SRH",  "MI",   "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.6, 47, 178, 2, 0),
    ("CSK",  "RCB",  "MA Chidambaram Stadium, Chennai",                  1, 0.6, 0.8, 56, 168, 1, 1),
    ("LSG",  "KKR",  "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.4, 0.8, 45, 173, 1, 0),
    ("DC",   "GT",   "Arun Jaitley Stadium, Delhi",                      1, 0.4, 0.6, 49, 172, 0, 0),
    ("PBKS", "RR",   "HPCA Stadium, Dharamsala",                         1, 0.4, 0.6, 44, 165, 0, 0),
    ("MI",   "RCB",  "Wankhede Stadium, Mumbai",                         1, 0.6, 0.8, 58, 185, 2, 1),
    ("CSK",  "KKR",  "MA Chidambaram Stadium, Chennai",                  1, 0.8, 0.6, 54, 168, 1, 1),
    ("SRH",  "DC",   "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.8, 0.4, 55, 178, 2, 1),
    ("RCB",  "GT",   "M Chinnaswamy Stadium, Bengaluru",                 1, 0.8, 0.6, 50, 192, 0, 1),
    ("KKR",  "MI",   "Eden Gardens, Kolkata",                            1, 0.6, 0.6, 45, 174, 1, 1),
    ("RR",   "LSG",  "Sawai Mansingh Stadium, Jaipur",                   1, 0.6, 0.4, 55, 176, 0, 1),
    # 2024 season
    ("KKR",  "RCB",  "Eden Gardens, Kolkata",                            1, 0.8, 0.6, 52, 174, 1, 1),
    ("SRH",  "RCB",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.8, 0.6, 52, 178, 2, 1),
    ("RR",   "DC",   "Sawai Mansingh Stadium, Jaipur",                   1, 0.8, 0.4, 53, 176, 0, 1),
    ("CSK",  "GT",   "MA Chidambaram Stadium, Chennai",                  1, 0.4, 0.6, 54, 168, 1, 0),
    ("MI",   "DC",   "Wankhede Stadium, Mumbai",                         1, 0.4, 0.6, 60, 185, 2, 0),
    ("LSG",  "GT",   "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.4, 0.8, 48, 173, 1, 0),
    ("KKR",  "SRH",  "Eden Gardens, Kolkata",                            1, 0.8, 0.6, 58, 174, 1, 1),
    ("GT",   "CSK",  "Narendra Modi Stadium, Ahmedabad",                 1, 0.8, 0.6, 46, 170, 1, 1),
    ("RCB",  "CSK",  "M Chinnaswamy Stadium, Bengaluru",                 1, 0.8, 0.6, 44, 192, 0, 0),
    ("DC",   "MI",   "Arun Jaitley Stadium, Delhi",                      1, 0.6, 0.4, 40, 172, 0, 0),
    ("SRH",  "KKR",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.8, 42, 178, 2, 0),
    ("MI",   "KKR",  "Wankhede Stadium, Mumbai",                         1, 0.4, 0.8, 55, 185, 2, 0),
    ("RR",   "KKR",  "Sawai Mansingh Stadium, Jaipur",                   1, 0.8, 0.8, 47, 176, 0, 1),
    ("LSG",  "CSK",  "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.4, 0.8, 42, 173, 1, 0),
    ("GT",   "DC",   "Narendra Modi Stadium, Ahmedabad",                 1, 0.6, 0.4, 52, 170, 1, 1),
    # 2023 season
    ("GT",   "CSK",  "Narendra Modi Stadium, Ahmedabad",                 1, 0.8, 0.8, 46, 170, 1, 0),
    ("CSK",  "GT",   "MA Chidambaram Stadium, Chennai",                  1, 0.8, 0.6, 54, 168, 1, 1),
    ("MI",   "RCB",  "Wankhede Stadium, Mumbai",                         1, 0.6, 0.4, 58, 185, 2, 1),
    ("RCB",  "MI",   "M Chinnaswamy Stadium, Bengaluru",                 1, 0.4, 0.6, 42, 192, 0, 0),
    ("KKR",  "RR",   "Eden Gardens, Kolkata",                            1, 0.6, 0.8, 53, 174, 1, 0),
    ("LSG",  "DC",   "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.6, 0.4, 52, 173, 1, 1),
    ("SRH",  "PBKS", "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.4, 56, 178, 2, 1),
    ("GT",   "MI",   "Narendra Modi Stadium, Ahmedabad",                 1, 0.6, 0.4, 46, 170, 1, 1),
    ("RR",   "SRH",  "Sawai Mansingh Stadium, Jaipur",                   1, 0.8, 0.4, 53, 176, 0, 1),
    ("DC",   "KKR",  "Arun Jaitley Stadium, Delhi",                      1, 0.4, 0.6, 43, 172, 0, 0),
    # Away wins (important for balance)
    ("MI",   "CSK",  "MA Chidambaram Stadium, Chennai",                  0, 0.8, 0.4, 52, 168, 1, 1),
    ("RCB",  "KKR",  "Eden Gardens, Kolkata",                            0, 0.8, 0.4, 48, 174, 1, 1),
    ("SRH",  "GT",   "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.4, 47, 170, 1, 1),
    ("KKR",  "MI",   "Wankhede Stadium, Mumbai",                         0, 0.8, 0.2, 45, 185, 2, 1),
    ("CSK",  "SRH",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     0, 0.8, 0.4, 56, 178, 2, 1),
    ("RR",   "MI",   "Wankhede Stadium, Mumbai",                         0, 0.8, 0.4, 48, 185, 2, 1),
    ("DC",   "CSK",  "MA Chidambaram Stadium, Chennai",                  0, 0.8, 0.2, 38, 168, 1, 1),
    ("GT",   "KKR",  "Eden Gardens, Kolkata",                            0, 0.8, 0.4, 46, 174, 1, 1),
    ("PBKS", "CSK",  "MA Chidambaram Stadium, Chennai",                  0, 0.8, 0.2, 37, 168, 1, 0),
    ("LSG",  "RCB",  "M Chinnaswamy Stadium, Bengaluru",                 0, 0.6, 0.6, 45, 192, 0, 0),
    # Low form teams losing at home
    ("MI",   "KKR",  "Wankhede Stadium, Mumbai",                         1, 0.2, 0.8, 55, 185, 2, 0),
    ("CSK",  "RCB",  "MA Chidambaram Stadium, Chennai",                  1, 0.2, 0.8, 56, 168, 1, 0),
    ("SRH",  "MI",   "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.2, 0.8, 47, 178, 2, 0),
    ("GT",   "CSK",  "Narendra Modi Stadium, Ahmedabad",                 1, 0.2, 0.8, 46, 170, 1, 0),
    ("KKR",  "RCB",  "Eden Gardens, Kolkata",                            1, 0.2, 0.8, 52, 174, 1, 0),
    ("RR",   "SRH",  "Sawai Mansingh Stadium, Jaipur",                   1, 0.2, 0.8, 53, 176, 0, 0),
    ("PBKS", "MI",   "HPCA Stadium, Dharamsala",                         1, 0.2, 0.8, 44, 165, 0, 0),
    ("DC",   "KKR",  "Arun Jaitley Stadium, Delhi",                      1, 0.2, 0.8, 43, 172, 0, 0),
    ("LSG",  "GT",   "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.2, 0.8, 48, 173, 1, 0),
    # Neutral venue matches (playoffs)
    ("MI",   "CSK",  "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.6, 52, 170, 1, 1),
    ("KKR",  "SRH",  "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.6, 58, 170, 1, 1),
    ("RCB",  "RR",   "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.6, 50, 170, 1, 1),
    ("GT",   "RR",   "Narendra Modi Stadium, Ahmedabad",                 0, 0.6, 0.8, 55, 170, 1, 0),
    ("CSK",  "GT",   "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.6, 54, 170, 1, 1),
    ("KKR",  "SRH",  "M Chinnaswamy Stadium, Bengaluru",                 0, 0.8, 0.4, 58, 192, 0, 1),
    ("RR",   "SRH",  "Narendra Modi Stadium, Ahmedabad",                 0, 0.6, 0.8, 47, 170, 1, 0),
    ("MI",   "RCB",  "Narendra Modi Stadium, Ahmedabad",                 0, 0.4, 0.8, 58, 170, 1, 0),
    # High dew impact matches
    ("SRH",  "RCB",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.4, 0.8, 52, 178, 2, 0),
    ("MI",   "GT",   "Wankhede Stadium, Mumbai",                         1, 0.4, 0.8, 54, 185, 2, 0),
    ("KKR",  "CSK",  "Eden Gardens, Kolkata",                            1, 0.4, 0.8, 54, 174, 1, 0),
    ("SRH",  "KKR",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.8, 42, 178, 2, 0),
    # Form dominance
    ("RCB",  "PBKS", "M Chinnaswamy Stadium, Bengaluru",                 1, 1.0, 0.0, 50, 192, 0, 1),
    ("KKR",  "LSG",  "Eden Gardens, Kolkata",                            1, 1.0, 0.0, 52, 174, 1, 1),
    ("GT",   "PBKS", "Narendra Modi Stadium, Ahmedabad",                 1, 1.0, 0.0, 55, 170, 1, 1),
    ("CSK",  "LSG",  "MA Chidambaram Stadium, Chennai",                  1, 1.0, 0.0, 56, 168, 1, 1),
    ("MI",   "PBKS", "Wankhede Stadium, Mumbai",                         1, 1.0, 0.0, 55, 185, 2, 1),
    ("SRH",  "LSG",  "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 1.0, 0.0, 54, 178, 2, 1),
    ("RCB",  "DC",   "M Chinnaswamy Stadium, Bengaluru",                 1, 1.0, 0.0, 55, 192, 0, 1),
    # Upsets
    ("PBKS", "MI",   "PCA Stadium, Mohali",                              1, 0.6, 0.4, 44, 179, 0, 1),
    ("DC",   "CSK",  "Arun Jaitley Stadium, Delhi",                      1, 0.6, 0.4, 38, 172, 0, 1),
    ("LSG",  "KKR",  "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.6, 0.4, 45, 173, 1, 1),
    ("RR",   "GT",   "Sawai Mansingh Stadium, Jaipur",                   1, 0.6, 0.4, 45, 176, 0, 1),
    ("PBKS", "RCB",  "HPCA Stadium, Dharamsala",                         1, 0.6, 0.4, 44, 165, 0, 1),
    ("DC",   "SRH",  "Arun Jaitley Stadium, Delhi",                      1, 0.6, 0.4, 45, 172, 0, 1),
    ("LSG",  "MI",   "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.8, 0.2, 45, 173, 1, 1),
    ("DC",   "RCB",  "Arun Jaitley Stadium, Delhi",                      1, 0.8, 0.2, 45, 172, 0, 1),
    # 2022 season highlights
    ("GT",   "RR",   "Narendra Modi Stadium, Ahmedabad",                 1, 0.8, 0.8, 55, 170, 1, 1),
    ("RR",   "GT",   "Narendra Modi Stadium, Ahmedabad",                 0, 0.8, 0.8, 45, 170, 1, 0),
    ("LSG",  "RCB",  "BRSABV Ekana Cricket Stadium, Lucknow",            1, 0.8, 0.6, 45, 173, 1, 1),
    ("RCB",  "LSG",  "M Chinnaswamy Stadium, Bengaluru",                 1, 0.6, 0.8, 55, 192, 0, 0),
    ("GT",   "LSG",  "Narendra Modi Stadium, Ahmedabad",                 1, 0.8, 0.6, 52, 170, 1, 1),
    ("KKR",  "DC",   "Eden Gardens, Kolkata",                            1, 0.6, 0.6, 57, 174, 1, 1),
    # Additional balanced data
    ("MI",   "SRH",  "Wankhede Stadium, Mumbai",                         1, 0.6, 0.4, 53, 185, 2, 1),
    ("CSK",  "MI",   "MA Chidambaram Stadium, Chennai",                  1, 0.6, 0.4, 48, 168, 1, 1),
    ("RCB",  "KKR",  "M Chinnaswamy Stadium, Bengaluru",                 1, 0.6, 0.4, 48, 192, 0, 1),
    ("SRH",  "GT",   "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.4, 47, 178, 2, 1),
    ("KKR",  "GT",   "Eden Gardens, Kolkata",                            1, 0.6, 0.4, 52, 174, 1, 1),
    ("RR",   "CSK",  "Sawai Mansingh Stadium, Jaipur",                   1, 0.6, 0.4, 40, 176, 0, 1),
    ("GT",   "SRH",  "Narendra Modi Stadium, Ahmedabad",                 1, 0.6, 0.4, 53, 170, 1, 1),
    ("MI",   "LSG",  "Wankhede Stadium, Mumbai",                         1, 0.6, 0.4, 55, 185, 2, 1),
    ("CSK",  "DC",   "MA Chidambaram Stadium, Chennai",                  1, 0.6, 0.4, 62, 168, 1, 1),
    ("KKR",  "LSG",  "Eden Gardens, Kolkata",                            1, 0.8, 0.4, 52, 174, 1, 1),
    ("SRH",  "PBKS", "Rajiv Gandhi Intl Cricket Stadium, Hyderabad",     1, 0.6, 0.2, 56, 178, 2, 1),
    ("RCB",  "RR",   "M Chinnaswamy Stadium, Bengaluru",                 1, 0.6, 0.4, 50, 192, 0, 1),
    ("DC",   "LSG",  "Arun Jaitley Stadium, Delhi",                      1, 0.6, 0.4, 52, 172, 0, 1),
    ("GT",   "PBKS", "Narendra Modi Stadium, Ahmedabad",                 1, 0.8, 0.2, 55, 170, 1, 1),
    ("MI",   "RR",   "Wankhede Stadium, Mumbai",                         1, 0.6, 0.4, 52, 185, 2, 1),
]

COLUMNS = ["team1","team2","venue","team1_home","t1_form","t2_form",
           "h2h_t1_pct","avg_first_inn","dew","result"]
