import teams
"""
Defines matchup of current batter vs pitcher
"""
#League Averages
aSO = .23
aBB = .09
aHBP = .009
aSing = .14
aDbl = .05
aTrp = .009
aHR = .04

class Matchup:

    def __init__(self, so, fo, walk, hbp, sing, dbl, trp, hr):
        self.so = so
        self.fo = fo
        self.walk = walk
        self.hbp = hbp
        self.sing = sing
        self.dbl = dbl
        self.trp = trp
        self.hr = hr

    # Runs at bat for current home hitter vs current away pitcher (params batting order and batters faced or lhbo)
    def home(self, bo, bf):
        dur = (bf - (teams.ap[0][15] - 4)) / 100
        if dur < 0:
            so = ((teams.Hdict[bo][6] * teams.ap[0][7]) / aSO) / (((teams.Hdict[bo][6] * teams.ap[0][7]) / aSO) + (
                    ((1 - teams.Hdict[bo][6]) * (1 - teams.ap[0][7])) / (1 - aSO)))
            bb = ((teams.Hdict[bo][8] * teams.ap[0][9]) / aBB) / (((teams.Hdict[bo][8] * teams.ap[0][9]) / aBB) + (
                    ((1 - teams.Hdict[bo][8]) * (1 - teams.ap[0][9])) / (1 - aBB)))
            hbp = ((teams.Hdict[bo][9] * teams.ap[0][10]) / aHBP) / (((teams.Hdict[bo][9] * teams.ap[0][10]) / aHBP) + (
                    ((1 - teams.Hdict[bo][9]) * (1 - teams.ap[0][10])) / (1 - aHBP)))
            sing = ((teams.Hdict[bo][10] * teams.ap[0][11]) / aSing) / (((teams.Hdict[bo][10] * teams.ap[0][11]) / aSing) + (
                    ((1 - teams.Hdict[bo][10]) * (1 - teams.ap[0][11])) / (1 - aSing)))
            dbl = ((teams.Hdict[bo][11] * teams.ap[0][12]) / aDbl) / (((teams.Hdict[bo][11] * teams.ap[0][12]) / aDbl) + (
                    ((1 - teams.Hdict[bo][11]) * (1 - teams.ap[0][12])) / (1 - aDbl)))
            trp = ((teams.Hdict[bo][12] * teams.ap[0][13]) / aTrp) / (((teams.Hdict[bo][12] * teams.ap[0][13]) / aTrp) + (
                    ((1 - teams.Hdict[bo][12]) * (1 - teams.ap[0][13])) / (1 - aTrp)))
            hr = ((teams.Hdict[bo][13] * teams.ap[0][14]) / aHR) / (((teams.Hdict[bo][13] * teams.ap[0][14]) / aHR) + (
                    ((1 - teams.Hdict[bo][13]) * (1 - teams.ap[0][14])) / (1 - aHR)))
            fo = 1 - so - hbp - bb - sing - dbl - trp - hr

        else:
            so = ((teams.Hdict[bo][6] * ((1 - dur) * teams.ap[0][7])) / aSO) / (((teams.Hdict[bo][6] * ((1 - dur) * teams.ap[0][7])) / aSO) + (
                    ((1 - teams.Hdict[bo][6]) * (1 - ((1 - dur) * teams.ap[0][7]))) / (1 - aSO)))
            bb = ((teams.Hdict[bo][8] * ((1 + (dur * .5)) * teams.ap[0][9])) / aBB) / (((teams.Hdict[bo][8] * ((1 + (dur * .5)) * teams.ap[0][9])) / aBB) + (
                    ((1 - teams.Hdict[bo][8]) * (1 - ((1 + (dur * .5)) * teams.ap[0][9]))) / (1 - aBB)))
            hbp = ((teams.Hdict[bo][9] * ((1 + (dur * .5)) * teams.ap[0][10])) / aHBP) / (((teams.Hdict[bo][9] * ((1 + (dur * .5)) * teams.ap[0][10])) / aHBP) + (
                    ((1 - teams.Hdict[bo][9]) * (1 - ((1 + (dur * .5)) * teams.ap[0][10]))) / (1 - aHBP)))
            sing = ((teams.Hdict[bo][10] * ((1 + (dur * .5)) * teams.ap[0][11])) / aSing) / (((teams.Hdict[bo][10] * ((1 + (dur * .5)) * teams.ap[0][11])) / aSing) + (
                        ((1 - teams.Hdict[bo][10]) * (1 - ((1 + (dur * .5)) * teams.ap[0][11]))) / (1 - aSing)))
            dbl = ((teams.Hdict[bo][11] * ((1 + (dur * .5)) * teams.ap[0][12])) / aDbl) / (((teams.Hdict[bo][11] * ((1 + (dur * .5)) * teams.ap[0][12])) / aDbl) + (
                        ((1 - teams.Hdict[bo][11]) * (1 - ((1 + (dur * .5)) * teams.ap[0][12]))) / (1 - aDbl)))
            trp = ((teams.Hdict[bo][12] * ((1 + (dur * .5)) * teams.ap[0][13])) / aTrp) / (
                        ((teams.Hdict[bo][12] * ((1 + (dur * .5)) * teams.ap[0][13])) / aTrp) + (
                        ((1 - teams.Hdict[bo][12]) * (1 - ((1 + (dur * .5)) * teams.ap[0][13]))) / (1 - aTrp)))
            hr = ((teams.Hdict[bo][13] * ((1 + (dur * .5)) * teams.ap[0][14])) / aHR) / (((teams.Hdict[bo][13] * ((1 + (dur * .5)) * teams.ap[0][14])) / aHR) + (
                    ((1 - teams.Hdict[bo][13]) * (1 - ((1 + (dur * .5)) * teams.ap[0][14]))) / (1 - aHR)))
            fo = 1 - so - hbp - bb - sing - dbl - trp - hr
    
        bvp = Matchup(so, so + fo, so + fo + bb, so + fo + bb + hbp, so + fo + bb + hbp + sing,
                      so + fo + bb + hbp + sing + dbl, so + fo + bb + hbp + sing + dbl + trp,
                      so + fo + bb + hbp + sing + dbl + trp + hr)
        return bvp
        
    # Runs at bat for current away hitter vs current home pitcher(params batting order and batters faced or labo)
    def away(self, bo, bf):
        dur = (bf - (teams.hp[0][15] - 4)) / 100
        if dur < 0:
            so = ((teams.Adict[bo][6] * teams.hp[0][7]) / aSO) / (((teams.Adict[bo][6] * teams.hp[0][7]) / aSO) + (
                    ((1 - teams.Adict[bo][6]) * (1 - teams.hp[0][7])) / (1 - aSO)))
            bb = ((teams.Adict[bo][8] * teams.hp[0][9]) / aBB) / (((teams.Adict[bo][8] * teams.hp[0][9]) / aBB) + (
                    ((1 - teams.Adict[bo][8]) * (1 - teams.hp[0][9])) / (1 - aBB)))
            hbp = ((teams.Adict[bo][9] * teams.hp[0][10]) / aHBP) / (((teams.Adict[bo][9] * teams.hp[0][10]) / aHBP) + (
                    ((1 - teams.Adict[bo][9]) * (1 - teams.hp[0][10])) / (1 - aHBP)))
            sing = ((teams.Adict[bo][10] * teams.hp[0][11]) / aSing) / (
                        ((teams.Adict[bo][10] * teams.hp[0][11]) / aSing) + (
                        ((1 - teams.Adict[bo][10]) * (1 - teams.hp[0][11])) / (1 - aSing)))
            dbl = ((teams.Adict[bo][11] * teams.hp[0][12]) / aDbl) / (
                        ((teams.Adict[bo][11] * teams.hp[0][12]) / aDbl) + (
                        ((1 - teams.Adict[bo][11]) * (1 - teams.hp[0][12])) / (1 - aDbl)))
            trp = ((teams.Adict[bo][12] * teams.hp[0][13]) / aTrp) / (
                        ((teams.Adict[bo][12] * teams.hp[0][13]) / aTrp) + (
                        ((1 - teams.Adict[bo][12]) * (1 - teams.hp[0][13])) / (1 - aTrp)))
            hr = ((teams.Adict[bo][13] * teams.hp[0][14]) / aHR) / (((teams.Adict[bo][13] * teams.hp[0][14]) / aHR) + (
                    ((1 - teams.Adict[bo][13]) * (1 - teams.hp[0][14])) / (1 - aHR)))
            fo = 1 - so - hbp - bb - sing - dbl - trp - hr
            
        else:
            so = ((teams.Adict[bo][6] * ((1 - dur) * teams.hp[0][7])) / aSO) / (
                        ((teams.Adict[bo][6] * ((1 - dur) * teams.hp[0][7])) / aSO) + (
                        ((1 - teams.Adict[bo][6]) * (1 - ((1 - dur) * teams.hp[0][7]))) / (1 - aSO)))
            bb = ((teams.Adict[bo][8] * ((1 + (dur * .5)) * teams.hp[0][9])) / aBB) / (
                        ((teams.Adict[bo][8] * ((1 + (dur * .5)) * teams.hp[0][9])) / aBB) + (
                        ((1 - teams.Adict[bo][8]) * (1 - ((1 + (dur * .5)) * teams.hp[0][9]))) / (1 - aBB)))
            hbp = ((teams.Adict[bo][9] * ((1 + (dur * .5)) * teams.hp[0][10])) / aHBP) / (
                        ((teams.Adict[bo][9] * ((1 + (dur * .5)) * teams.hp[0][10])) / aHBP) + (
                        ((1 - teams.Adict[bo][9]) * (1 - ((1 + (dur * .5)) * teams.hp[0][10]))) / (1 - aHBP)))
            sing = ((teams.Adict[bo][10] * ((1 + (dur * .5)) * teams.hp[0][11])) / aSing) / (
                        ((teams.Adict[bo][10] * ((1 + (dur * .5)) * teams.hp[0][11])) / aSing) + (
                        ((1 - teams.Adict[bo][10]) * (1 - ((1 + (dur * .5)) * teams.hp[0][11]))) / (1 - aSing)))
            dbl = ((teams.Adict[bo][11] * ((1 + (dur * .5)) * teams.hp[0][12])) / aDbl) / (
                        ((teams.Adict[bo][11] * ((1 + (dur * .5)) * teams.hp[0][12])) / aDbl) + (
                        ((1 - teams.Adict[bo][11]) * (1 - ((1 + (dur * .5)) * teams.hp[0][12]))) / (1 - aDbl)))
            trp = ((teams.Adict[bo][12] * ((1 + (dur * .5)) * teams.hp[0][13])) / aTrp) / (
                        ((teams.Adict[bo][12] * ((1 + (dur * .5)) * teams.hp[0][13])) / aTrp) + (
                        ((1 - teams.Adict[bo][12]) * (1 - ((1 + (dur * .5)) * teams.hp[0][13]))) / (1 - aTrp)))
            hr = ((teams.Adict[bo][13] * ((1 + (dur * .5)) * teams.hp[0][14])) / aHR) / (
                        ((teams.Adict[bo][13] * ((1 + (dur * .5)) * teams.hp[0][14])) / aHR) + (
                        ((1 - teams.Adict[bo][13]) * (1 - ((1 + (dur * .5)) * teams.hp[0][14]))) / (1 - aHR)))
            fo = 1 - so - hbp - bb - sing - dbl - trp - hr
    
        bvp = Matchup(so, so + fo, so + fo + bb, so + fo + bb + hbp, so + fo + bb + hbp + sing,
                      so + fo + bb + hbp + sing + dbl, so + fo + bb + hbp + sing + dbl + trp,
                      so + fo + bb + hbp + sing + dbl + trp + hr)
        return bvp
    