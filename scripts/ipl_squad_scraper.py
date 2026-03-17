import csv
import random

# -----------------------------
# LOAD OLD DATABASE
# -----------------------------
def load_old_db(file_path):

    old_players = {}

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["Player_Name"].strip().lower()

            old_players[name] = {
                "Power": row["Power"],
                "Innovation": row["Innovation"],
                "Acceleration": row["Acceleration"]
            }

    print("Loaded old players:", len(old_players))

    return old_players


def normalize(name):
    return name.lower().strip()


# -----------------------------
# IPL 2026 SQUADS
# -----------------------------
squads = {

"Chennai Super Kings":[
"Ruturaj Gaikwad","MS Dhoni","Dewald Brevis","Ayush Mhatre","Urvil Patel",
"Anshul Kamboj","Jamie Overton","Ramakrishna Ghosh","Shivam Dube","Khaleel Ahmed",
"Noor Ahmad","Mukesh Choudhary","Nathan Ellis","Shreyas Gopal","Gurjapneet Singh",
"Sanju Samson","Akeal Hosein","Prashant Veer","Kartik Sharma","Matthew Short",
"Aman Khan","Sarfaraz Khan","Rahul Chahar","Matt Henry","Zak Foulkes"
],

"Delhi Capitals":[
"KL Rahul","Karun Nair","Abishek Porel","Tristan Stubbs","Axar Patel",
"Sameer Rizvi","Ashutosh Sharma","Vipraj Nigam","Ajay Mandal","Tripurana Vijay",
"Madhav Tiwari","Mitchell Starc","T Natarajan","Mukesh Kumar","Dushmantha Chameera",
"Kuldeep Yadav","Nitish Rana","Auqib Dar","Ben Duckett","David Miller",
"Pathum Nissanka","Lungi Ngidi","Sahil Parakh","Prithvi Shaw","Kyle Jamieson"
],

"Gujarat Titans":[
"Shubman Gill","Sai Sudharsan","Kumar Kushagra","Anuj Rawat","Jos Buttler",
"Nishant Sindhu","Glenn Phillips","Washington Sundar","Arshad Khan","Shahrukh Khan",
"Rahul Tewatia","Kagiso Rabada","Mohammed Siraj","Prasidh Krishna","Ishant Sharma",
"Gurnoor Singh Brar","Rashid Khan","Manav Suthar","Sai Kishore","Jayant Yadav",
"Ashok Sharma","Jason Holder","Tom Banton","Luke Wood","Prithviraj Yarra"
],

"Kolkata Knight Riders":[
"Ajinkya Rahane","Rinku Singh","Angkrish Raghuvanshi","Manish Pandey","Rovman Powell",
"Anukul Roy","Ramandeep Singh","Vaibhav Arora","Sunil Narine","Varun Chakaravarthy",
"Harshit Rana","Umran Malik","Cameron Green","Matheesha Pathirana","Finn Allen",
"Tejasvi Singh","Prashant Solanki","Kartik Tyagi","Rahul Tripathi","Tim Seifert",
"Sarthak Ranjan","Daksh Kamra","Akash Deep","Rachin Ravindra","Blessing Muzarabani"
],

"Lucknow Super Giants":[
"Rishabh Pant","Ayush Badoni","Abdul Samad","Aiden Markram","Himmat Singh",
"Matthew Breetzke","Nicholas Pooran","Mitchell Marsh","Shahbaz Ahmed","Arshin Kulkarni",
"Mayank Yadav","Avesh Khan","Mohsin Khan","M Siddharth","Digvesh Rathi",
"Prince Yadav","Akash Singh","Arjun Tendulkar","Mohammed Shami","Anrich Nortje",
"Wanindu Hasaranga","Mukul Choudhary","Naman Tiwari","Akshat Raghuwanshi","Josh Inglis"
],

"Mumbai Indians":[
"Rohit Sharma","Suryakumar Yadav","Robin Minz","Ryan Rickelton","Tilak Varma",
"Hardik Pandya","Naman Dhir","Mitchell Santner","Will Jacks","Corbin Bosch",
"Raj Bawa","Trent Boult","Jasprit Bumrah","Deepak Chahar","Ashwani Kumar",
"Raghu Sharma","Allah Ghazanfar","Mayank Markande","Shardul Thakur","Sherfane Rutherford",
"Quinton De Kock","Atharva Ankolekar","Mohammad Izhar","Danish Malewar","Mayank Rawat"
],

"Punjab Kings":[
"Shreyas Iyer","Nehal Wadhera","Vishnu Vinod","Harnoor Pannu","Pyla Avinash",
"Prabhsimran Singh","Shashank Singh","Marcus Stoinis","Harpreet Brar","Marco Jansen",
"Azmatullah Omarzai","Priyansh Arya","Musheer Khan","Suryansh Shedge","Mitch Owen",
"Arshdeep Singh","Yuzvendra Chahal","Vyshak Vijaykumar","Yash Thakur","Xavier Bartlett",
"Lockie Ferguson","Cooper Connolly","Ben Dwarshuis","Vishal Nishad","Pravin Dubey"
],

"Rajasthan Royals":[
"Shubham Dubey","Vaibhav Suryavanshi","Lhuan-dre Pretorius","Shimron Hetmyer","Yashasvi Jaiswal",
"Dhruv Jurel","Riyan Parag","Yudhvir Singh Charak","Jofra Archer","Tushar Deshpande",
"Sandeep Sharma","Kwena Maphaka","Nandre Burger","Ravindra Jadeja","Sam Curran",
"Donovan Ferreira","Ravi Bishnoi","Sushant Mishra","Vignesh Puthur","Yash Raj Punja",
"Ravi Singh","Brijesh Sharma","Aman Rao","Adam Milne","Kuldeep Sen"
],

"Royal Challengers Bengaluru":[
"Rajat Patidar","Virat Kohli","Tim David","Devdutt Padikkal","Phil Salt",
"Jitesh Sharma","Krunal Pandya","Jacob Bethell","Romario Shepherd","Swapnil Singh",
"Josh Hazlewood","Bhuvneshwar Kumar","Rasikh Salam","Yash Dayal","Suyash Sharma",
"Nuwan Thushara","Abhinandan Singh","Venkatesh Iyer","Jacob Duffy","Mangesh Yadav",
"Satvik Deswal","Jordan Cox","Kanishk Chouhan","Vihaan Malhotra","Vicky Ostwal"
],

"Sunrisers Hyderabad":[
"Travis Head","Abhishek Sharma","Aniket Verma","R Smaran","Ishan Kishan",
"Heinrich Klaasen","Nitish Kumar Reddy","Harsh Dubey","Kamindu Mendis","Harshal Patel",
"Brydon Carse","Pat Cummins","Jaydev Unadkat","Eshan Malinga","Zeeshan Ansari",
"Shivang Kumar","Salil Arora","Krains Fuletra","Praful Hinge","Amit Kumar",
"Onkar Tarmale","Sakib Hussain","Liam Livingstone","Shivam Mavi","Jack Edwards"
]

}


# -----------------------------
# GENERATE NEW DB
# -----------------------------
def generate_db(old_db):

    rows = []
    player_id = 1001

    for team, players in squads.items():

        for player in players:

            key = normalize(player)

            if key in old_db:

                stats = old_db[key]

                power = stats["Power"]
                innovation = stats["Innovation"]
                accel = stats["Acceleration"]

            else:

                power = random.randint(40,95)
                innovation = random.randint(40,95)
                accel = random.randint(40,95)

            rows.append({
                "Player_ID":player_id,
                "Player_Name":player,
                "Team":team,
                "Power":power,
                "Innovation":innovation,
                "Acceleration":accel
            })

            player_id += 1

    with open("new_player_db_2026.csv","w",newline="",encoding="utf-8") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["Player_ID","Player_Name","Team","Power","Innovation","Acceleration"]
        )

        writer.writeheader()
        writer.writerows(rows)

    print("Saved new_player_db_2026.csv")
    print("Total players:",len(rows))


if __name__ == "__main__":

    old_db = load_old_db("player_db - 2025.csv")

    generate_db(old_db)