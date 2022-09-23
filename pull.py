import pandas as pd

"""
Imports CSV and pre-process some data so sims can run smoothly
"""

scores = {}     #Sum of all Sim Team Scores
gameFP = {}     #Sum of all Sim Player Scores
probs = []       #Imported Stats from CSV
gms = []        #List of Games
names = []      #List of Player names for tracking points
sumFP = {}
team = []

#Pull Stats from CSV and set up Initial Lists
def pull_csv(self):
    df = pd.read_csv(r'YOUR PATH HERE', delimiter=',')     #Get CSV
    data = [list(row) for row in df.values]     # Place Stats in List
    games = df.Game.unique()        # List of Unique Games
    players = df.Nickname.unique()        # List of Unique Names
    tm = df.Team.unique()       #List of Unique Teams
    #Names in dictionary for Projections
    for row in data:
        key = row[1]
        gameFP[key] = []
    #Teams in dictionary for Projections
    for row in tm:
        key = row[0:]
        scores[key] = 0
    #Games in List for use for sim
    i = 0
    while i < len(games):
        gms.append(games[i])
        i+=1
    i = 0
    while i < len(players):
        names.append(players[i])
        i+=1
    i = 0
    while i < len(data):
        probs.append(data[i])
        i+=1
    i = 0
    while i < len(tm):
        team.append(tm[i])
        i += 1
        
def scoring(self):
    i = 0
    for row in probs:
        key = row[1]
        sumFP[key] = 0
        i += 0

