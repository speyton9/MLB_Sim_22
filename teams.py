import pull

"""
Organizes Players from each game into lists for the sim to run. Goal is to clean up by removing lists g, h, a
"""

#Home and Away Hitters lists
h = []
a = []

g = []      #list of players from both teams in game

hp = []     #Current Home Pitcher
ap = []     #Current Away Pitcher
hstart = []     #Home Starter
astart = []     #Away Starter

Hdict = {}      #Home Batters Dictionary for game
Adict = {}      #Away Batters Dictionary for game

#Number of batters faced for pulling
lhbo = 0
labo = 0
#Home score when pitcher is pulled
hss = {}
hss['home'] = 0
hss['away'] = 0
hqs = 0
#Away score when pitcher is pulled
ass = {}
ass['home'] = 0
ass['away'] = 0
aqs = 0

#Home/Away starters
hsp = []
asp = []

def split(self, game):
    # Place Game n in list g
    i = 0
    while i < len(pull.probs):

        if pull.probs[i][6] == pull.gms[game]:
            g.append(pull.probs[i])
        i += 1

    #Split home and away teams
    i = 0
    while i < len(g):

        if g[i][3] == g[i][5]:
            h.append(g[i])
            i+=1
        else:
            a.append(g[i])
            i+=1

    x = 0
    #Place home pitcher in own list, remove from previous
    while x < len(h):
        if h[x][2] == 'P':
            hp.append(h[x])
            h.pop(x)
        x+=1
    y = 0
    #Place away pitcher in own list, remove from previous
    while y < len(a):
        if a[y][2] == 'P':
            ap.append(a[y])
            a.pop(y)
        y+=1

    #Place home hitters in dict
    for row in h:
        key = row[0]
        Hdict[key] = row[1:]
    #Place away hitters in dict
    for row in a:
        key = row[0]
        Adict[key] = row[1:]
    inning = 0
    # Pitcher List
    hsp.append(hp[0][1])
    asp.append(ap[0][1])
    
def reset(self):
    # Home and Away Hitters lists
    h = []
    a = []

    g = []  # list of players from both teams in game

    hp = []  # Current Home Pitcher
    ap = []  # Current Away Pitcher
    hstart = []  # Home Starter
    astart = []  # Away Starter

    Hdict = {}  # Home Batters Dictionary for game
    Adict = {}  # Away Batters Dictionary for game

    # Number of batters faced for pulling
    lhbo = 0
    labo = 0
    # Home score when pitcher is pulled
    hss = {}
    hss['home'] = 0
    hss['away'] = 0
    hqs = 0
    # Away score when pitcher is pulled
    ass = {}
    ass['home'] = 0
    ass['away'] = 0
    aqs = 0

    # Home/Away starters
    hsp = []
    asp = []
    
