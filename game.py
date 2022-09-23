import box
import pa
import pull
import teams
import random
import defaults
import pandas as pd
import numpy as np
import re
from defaults import restart
from pull import scoring

class Sim:
    def run(self, sims):

        pull.pull_csv(None) #Get CSV

        # Loop to sim each game n times
        i = 0
        while i < sims:

            # Loop to sim each game in games list
            j = 0
            print(pull.gms)
            while j < len(pull.gms):

                #Split teams of current game into necessary lists
                teams.split(None, j)

                #Pull player list for scoring
                pull.scoring(None)
                print(teams.Hdict)
                print(teams.Adict)
                print("Game Start")
                # Begin gameplay
                while box.inning < 18:

                    #Top of the inning
                    if box.inning % 2 == 0:
                        print('-------------------------------------Top-Of-The-Inning-----------------------------')
                        # Clear bases and reset outs for next inning
                        box.first = 0
                        box.second = 0
                        box.third = 0
                        box.out = 0
                        #inning score --- if exceeds 4, pull pitcher mid inning
                        ins = 0
                        #Inning lasts for 3 outs
                        while box.out < 3:
                            #Resets batting order when last batter has AB
                            if box.abo == 10:
                                box.abo = 1
                            #Loop through batting order
                            while box.abo < 10:
                                if box.out == 3:
                                    break
                                #Calc matchup probabilities
                                pa.Matchup.away(None, box.abo, teams.labo)
                                print(teams.hp[0][1])
                                print('Home: '+str(box.home)+' Away: '+str(box.away))
                                print('1B: '+str(box.first)+' 2B: '+str(box.second)+' 3B: '+str(box.third))
                                print('Out: '+str(box.out))
                                print('abo:'+ str(box.abo))
                                #Result of Plate Appearance
                                ab = random.uniform(0, 1)
                                #Base/roster movement and Scoring as a result of PA result
                                if ab <= pa.Matchup.away(None, box.abo, teams.labo).so:
                                    print("Away SO")
                                    pull.sumFP[teams.hp[0][1]] += 4
                                    box.out+=1

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).fo:
                                    print("Away FO")
                                    pull.sumFP[teams.hp[0][1]] += 1
                                    box.out += 1
                                    #Runners advance
                                    adv = random.uniform(0, 1)
                                    #Is there a DOUBLE PLAY? - Currently place holder
                                    if box.first > 0:
                                        if box.out < 3:
                                            if ab < pa.Matchup.away(None, box.abo, teams.labo).so + .022:
                                                pull.sumFP[teams.hp[0][1]] += 1
                                                box.out += 1
                                                box.first = 0
                                                print("Double Play")
                                    if box.third > 0:
                                        if box.out < 3:
                                            if adv > teams.Adict[box.third][15]:
                                                pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                                pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                                pull.sumFP[teams.hp[0][1]] += -3
                                                box.third = 0
                                                ins += 1
                                                box.away += 1
                                    if box.second > 0:
                                        if box.out < 3:
                                            if box.third == 0:
                                                if adv > teams.Adict[box.second][15]:
                                                    box.third = box.second
                                                    box.second = 0
                                    if box.first > 0:
                                        if box.out < 3:
                                            if box.second == 0:
                                                run = random.uniform(0, 1)
                                                bt = random.uniform(0, 1)
                                                if run > teams.Adict[box.first][15]:
                                                    box.second = box.first
                                                    box.first = 0
                                                elif bt > teams.Adict[box.abo][15]:
                                                    box.first = box.abo

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).walk:
                                    print("Away BB")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 3
                                    if box.first > 0:
                                        if box.second > 0:
                                            if box.third > 0: #Bases Loaded
                                                pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                                pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                                pull.sumFP[teams.hp[0][1]] += -3
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.abo
                                                ins += 1
                                                box.away += 1
                                            else: #Runners 1st and 2nd
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.abo
                                        else: #Runner on 1st, 2nd open (3rd irrelevent)
                                            box.second = box.first
                                            box.first = box.abo
                                    else: #1st is open, runner to 1st, other bases irrelevent
                                        box.first = box.abo

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).hbp:
                                    print("Away HBP")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 3
                                    if box.first > 0:
                                        if box.second > 0:
                                            if box.third > 0:  # Bases Loaded
                                                pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                                pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                                pull.sumFP[teams.hp[0][1]] += -3
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.abo
                                                ins += 1
                                                box.away += 1
                                            else:  # Runners 1st and 2nd
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.abo
                                        else:  # Runner on 1st, 2nd open (3rd irrelevent)
                                            box.second = box.first
                                            box.first = box.abo
                                    else:  # 1st is open, runner to 1st, other bases irrelevent
                                        box.first = box.abo

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).sing:
                                    print("Away Sing")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 3
                                    adv = random.uniform(0, 1)
                                    if box.third > 0:
                                        pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.away += 1
                                    if box.second > 0:
                                        if adv > teams.Adict[box.second][15]:
                                            pull.sumFP[teams.Adict[box.second][0]] += 3.2
                                            pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                            pull.sumFP[teams.hp[0][1]] += -3
                                            box.second = 0
                                            ins += 1
                                            box.away += 1
                                        else:
                                            box.third = box.second
                                            box.second = 0
                                    if box.first > 0:
                                        if box.third > 0:
                                            box.second = box.first
                                            box.first = 0
                                        elif adv > teams.Adict[box.first][15]:
                                            box.third = box.first
                                            box.first = 0
                                        else:
                                            box.second = box.first
                                            box.first = 0
                                    box.first = box.abo

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).dbl:
                                    print("Away dbl")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 6
                                    # Runners on base advance one or 2+ bags
                                    adv = random.uniform(0, 1)
                                    if box.third > 0:
                                        pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.away += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Adict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.away += 1
                                    if box.first > 0:
                                        if adv > (teams.Adict[box.first][15] * 1.15):
                                            pull.sumFP[teams.Adict[box.first][0]] += 3.2
                                            pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                            pull.sumFP[teams.hp[0][1]] += -3
                                            box.first = 0
                                            ins += 1
                                            box.away += 1
                                        else:
                                            box.third = box.first
                                            box.first = 0
                                    box.second = box.abo

                                elif ab <= pa.Matchup.away(None, box.abo, teams.labo).trp:
                                    print("Away trp")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 9
                                    if box.third > 0:
                                        pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.away += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Adict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.away += 1
                                    if box.first > 0:
                                        pull.sumFP[teams.Adict[box.first][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.first = 0
                                        ins += 1
                                        box.away += 1
                                    box.third = box.abo

                                else:# ab <= pa.Matchup.away(None, box.abo).hr:
                                    print("Away hr")
                                    pull.sumFP[teams.Adict[box.abo][0]] += 18.7
                                    pull.sumFP[teams.hp[0][1]] += -3
                                    if box.third > 0:
                                        pull.sumFP[teams.Adict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.away += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Adict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.away += 1
                                    if box.first > 0:
                                        pull.sumFP[teams.Adict[box.first][0]] += 3.2
                                        pull.sumFP[teams.Adict[box.abo][0]] += 3.5
                                        pull.sumFP[teams.hp[0][1]] += -3
                                        box.first = 0
                                        ins += 1
                                        box.away += 1
                                    ins += 1
                                    box.away += 1

                                #Remove Starting pitcher mid inning if 5+ runs agains in one inning
                                if ins > 4:
                                    if len(teams.hp) == 2:
                                        teams.hss['home'] = box.home
                                        teams.hss['away'] = box.away
                                        teams.hstart.append(teams.hp[0])
                                        teams.hp.pop(0)
                                        print('Home SP baaad game')
                                #Remove Starting Pitcher mid inning if down by 5+ runs
                                elif box.away - box.home > 4:
                                    if len(teams.hp) == 2:
                                        teams.hss['home'] = box.home
                                        teams.hss['away'] = box.away
                                        teams.hstart.append(teams.hp[0])
                                        teams.hp.pop(0)
                                        print('Home SP Rocked')
                                #batters faced
                                teams.labo += 1
                                #Advance to next batter
                                box.abo += 1

                    else:
                        # Clear bases and outs for next inning
                        box.first = 0
                        box.second = 0
                        box.third = 0
                        box.out = 0
                        #Inning Score -- Pull pitcher if over 4
                        ins = 0
                        print('------------------------Bottom-Of-Inning----------------------')
                        # Inning lasts for 3 outs
                        while box.out < 3:
                            # Resets batting order when last batter has AB
                            if box.hbo == 10:
                                box.hbo = 1
                            # Loop through batting order
                            while box.hbo < 10:
                                if box.out == 3:
                                    break
                                # Calc matchup probabilities
                                pa.Matchup.home(None, box.hbo, teams.lhbo)
                                print(teams.ap[0][1])
                                print('Home: ' + str(box.home) + ' Away: ' + str(box.away))
                                print('1B: ' + str(box.first) + ' 2B: ' + str(box.second) + ' 3B: ' + str(box.third))
                                print('Out: ' + str(box.out))
                                print('hbo:' + str(box.hbo))
                                # Result of Plate Appearance
                                ab = random.uniform(0, 1)
                                # Base/roster movement and Scoring as a result of PA result
                                if ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).so:
                                    print("Home SO")
                                    pull.sumFP[teams.ap[0][1]] += 4
                                    box.out += 1

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).fo:
                                    print("Home fo")
                                    pull.sumFP[teams.ap[0][1]] += 1
                                    box.out += 1
                                    # Runners advance
                                    adv = random.uniform(0, 1)
                                    # Is there a DOUBLE PLAY? - Currently place holder
                                    if box.first > 0:
                                        if box.out < 3:
                                            if ab < pa.Matchup.home(None, box.hbo, teams.lhbo).so + .022:
                                                pull.sumFP[teams.ap[0][1]] += 1
                                                box.out += 1
                                                box.first = 0
                                                print("Double Play")
                                    if box.third > 0:
                                        if box.out < 3:
                                            if adv > teams.Hdict[box.third][15]:
                                                pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                                pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                                pull.sumFP[teams.ap[0][1]] += -3
                                                box.third = 0
                                                ins += 1
                                                box.home += 1
                                    if box.second > 0:
                                        if box.out < 3:
                                            if box.third == 0:
                                                if adv > teams.Hdict[box.second][15]:
                                                    box.third = box.second
                                                    box.second = 0
                                    if box.first > 0:
                                        if box.out < 3:
                                            if box.second == 0:
                                                run = random.uniform(0, 1)
                                                bt = random.uniform(0, 1)
                                                if run > teams.Hdict[box.first][15]:
                                                    box.second = box.first
                                                    box.first = 0
                                                elif bt > teams.Hdict[box.hbo][15]:
                                                    box.first = box.hbo

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).walk:
                                    print("Home BB")
                                    pull.sumFP[teams.Adict[box.hbo][0]] += 3
                                    if box.first > 0:
                                        if box.second > 0:
                                            if box.third > 0:  # Bases Loaded
                                                pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                                pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                                pull.sumFP[teams.ap[0][1]] += -3
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.hbo
                                                ins += 1
                                                box.home += 1
                                            else:  # Runners 1st and 2nd
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.hbo
                                        else:  # Runner on 1st, 2nd open (3rd irrelevent)
                                            box.second = box.first
                                            box.first = box.hbo
                                    else:  # 1st is open, runner to 1st, other bases irrelevent
                                        box.first = box.hbo

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).hbp:
                                    print("Home HBP")
                                    pull.sumFP[teams.Hdict[box.hbo][0]] += 3
                                    if box.first > 0:
                                        if box.second > 0:
                                            if box.third > 0:  # Bases Loaded
                                                pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                                pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                                pull.sumFP[teams.ap[0][1]] += -3
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.hbo
                                                ins += 1
                                                box.home += 1
                                            else:  # Runners 1st and 2nd
                                                box.third = box.second
                                                box.second = box.first
                                                box.first = box.hbo
                                        else:  # Runner on 1st, 2nd open (3rd irrelevent)
                                            box.second = box.first
                                            box.first = box.hbo
                                    else:  # 1st is open, runner to 1st, other bases irrelevent
                                        box.first = box.hbo

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).sing:
                                    print("Home Sing")
                                    pull.sumFP[teams.Hdict[box.hbo][0]] += 3
                                    adv = random.uniform(0, 1)
                                    if box.third > 0:
                                        pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.home += 1
                                    if box.second > 0:
                                        if adv > teams.Hdict[box.second][15]:
                                            pull.sumFP[teams.Hdict[box.second][0]] += 3.2
                                            pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                            pull.sumFP[teams.ap[0][1]] += -3
                                            box.second = 0
                                            ins += 1
                                            box.home += 1
                                        else:
                                            box.third = box.second
                                            box.second = 0
                                    if box.first > 0:
                                        if box.third > 0:
                                            box.second = box.first
                                            box.first = 0
                                        elif adv > teams.Hdict[box.first][15]:
                                            box.third = box.first
                                            box.first = 0
                                        else:
                                            box.second = box.first
                                            box.first = 0
                                    box.first = box.hbo

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).dbl:
                                    print("Home dbl")
                                    pull.sumFP[teams.Hdict[box.hbo][0]] += 6
                                    # Runners on base advance one or 2+ bags
                                    adv = random.uniform(0, 1)
                                    if box.third > 0:
                                        pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.home += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Hdict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.home += 1
                                    if box.first > 0:
                                        if adv > (teams.Hdict[box.first][15] * 1.15):
                                            pull.sumFP[teams.Hdict[box.first][0]] += 3.2
                                            pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                            pull.sumFP[teams.ap[0][1]] += -3
                                            box.first = 0
                                            ins += 1
                                            box.home += 1
                                        else:
                                            box.third = box.first
                                            box.first = 0
                                    box.second = box.hbo

                                elif ab <= pa.Matchup.home(None, box.hbo, teams.lhbo).trp:
                                    print("Home trp")
                                    pull.sumFP[teams.Hdict[box.hbo][0]] += 9
                                    if box.third > 0:
                                        pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.home += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Hdict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.home += 1
                                    if box.first > 0:
                                        pull.sumFP[teams.Hdict[box.first][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.first = 0
                                        ins += 1
                                        box.home += 1
                                    box.third = box.hbo

                                else: #if ab <= pa.Matchup.home(None, box.hbo).hr:
                                    print("Home hr")
                                    pull.sumFP[teams.Hdict[box.hbo][0]] += 18.7
                                    pull.sumFP[teams.ap[0][1]] += -3
                                    if box.third > 0:
                                        pull.sumFP[teams.Hdict[box.third][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.third = 0
                                        ins += 1
                                        box.home += 1
                                    if box.second > 0:
                                        pull.sumFP[teams.Hdict[box.second][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.second = 0
                                        ins += 1
                                        box.home += 1
                                    if box.first > 0:
                                        pull.sumFP[teams.Hdict[box.first][0]] += 3.2
                                        pull.sumFP[teams.Hdict[box.hbo][0]] += 3.5
                                        pull.sumFP[teams.ap[0][1]] += -3
                                        box.first = 0
                                        ins += 1
                                        box.home += 1
                                    ins += 1
                                    box.home += 1

                                # Remove Starting pitcher mid inning if 5+ runs agains in one inning
                                if ins > 4:
                                    if len(teams.ap) == 2:
                                        teams.ass['home'] = box.home
                                        teams.ass['away'] = box.away
                                        teams.astart.append(teams.ap[0])
                                        teams.ap.pop(0)
                                        print('Away SP baaad game')
                                # Remove Starting Pitcher mid inning if down by 5+ runs
                                elif box.home - box.away > 4:
                                    if len(teams.ap) == 2:
                                        teams.ass['home'] = box.home
                                        teams.ass['away'] = box.away
                                        teams.astart.append(teams.ap[0])
                                        teams.ap.pop(0)
                                        print('Away SP Rocked')
                                # batters faced
                                teams.lhbo += 1
                                # Advance to next batter
                                box.hbo += 1
                                #Ends game in bottom of 9th if home team takes lead
                                if box.inning == 17:
                                    if box.home > box.away:
                                        box.out += 3

                    # Awards QS after 6th Inning Played
                    if box.inning == 10:
                        if teams.hp[0][1] == teams.hsp[0]:
                            if box.away < 4:
                                pull.sumFP[teams.hp[0][1]] += 4
                                teams.hss['away'] = box.away
                                teams.hss['home'] = box.home
                                teams.hqs += 1
                                print('HOME QS!!!!!!')
                    if box.inning == 11:
                        if teams.ap[0][1] == teams.asp[0]:
                            if box.home < 4:
                                pull.sumFP[teams.ap[0][1]] += 4
                                teams.ass['home'] = box.home
                                teams.ass['away'] = box.away
                                teams.aqs += 1
                                print('Away QS!!!!!!')
                    # Removes bonus if needed
                    if box.inning == 12:
                        if teams.hp[0][1] == teams.hsp[0]:
                            if teams.hqs == 1:
                                if box.away > 3:
                                    pull.sumFP[teams.hp[0][1]] += -4
                                    print('HOME SP LOST QS!!!!!!')
                    if box.inning == 13:
                        if teams.ap[0][1] == teams.asp[0]:
                            if teams.aqs == 1:
                                if box.home > 3:
                                    pull.sumFP[teams.ap[0][1]] += -4
                                    print('Away SP LOST QS!!!!!!')
                    # Pulls pitcher over 24 batters faced
                    if teams.labo > (teams.hp[0][15]) + 6:
                        if len(teams.hp) == 2:
                            teams.hss['away'] = box.away
                            teams.hss['home'] = box.home
                            teams.hstart.append(teams.hp[0])
                            teams.hp.pop(0)
                            print('Home SP Batter Limit')
                    if teams.lhbo > (teams.ap[0][15]) + 6:
                        if len(teams.ap) == 2:
                            teams.ass['home'] = box.home
                            teams.ass['away'] = box.away
                            teams.astart.append(teams.ap[0])
                            teams.ap.pop(0)
                            print('Away SP Batter Limit')
                    # Pull pitcher if runs over 5 append BP to hp from
                    if box.away > 5:
                        if len(teams.hp) == 2:
                            teams.hss['away'] = box.away
                            teams.hss['home'] = box.home
                            teams.hstart.append(teams.hp[0])
                            teams.hp.pop(0)
                            print("Home Pitcher Pulled")
                    if box.home > 5:
                        if len(teams.ap) == 2:
                            teams.ass['home'] = box.home
                            teams.ass['away'] = box.away
                            teams.astart.append(teams.ap[0])
                            teams.ap.pop(0)
                            print("Away Pitcher Pulled")
                    # Pull pitcher after 7 IP
                    if box.inning >= 12:
                        if len(teams.hp) == 2:
                            teams.hss['away'] = box.away
                            teams.hss['home'] = box.home
                            teams.hstart.append(teams.hp[0])
                            teams.hp.pop(0)
                            print("New Home Pitcher")
                    if box.inning >= 13:
                        if len(teams.ap) == 2:
                            teams.ass['home'] = box.home
                            teams.ass['away'] = box.away
                            teams.astart.append(teams.ap[0])
                            teams.ap.pop(0)
                            print("New Away Pitcher")
                    # End game if home ahead going into bottom of 9th
                    if box.inning == 16:
                        if box.home > box.away:
                            box.inning += 18
                    # advance inning
                    box.inning += 1
                # Advance to next game sim
                j += 1
                # push final game score to counter
                pull.scores[teams.h[1][3]] = box.home + pull.scores[teams.h[1][3]]
                pull.scores[teams.a[1][3]] = box.away + pull.scores[teams.a[1][3]]
                # awards win bonus if SP was ahead when pulled and team wins game
                if box.home > box.away:
                    if teams.hss['home'] > teams.hss['away']:
                        if box.away < teams.hss['home']:
                            pull.sumFP[teams.hstart[0][1]] += 6
                            print('Home SP Win')
                else:
                    if teams.ass['away'] > teams.ass['home']:
                        if box.home < teams.ass['away']:
                            pull.sumFP[teams.astart[0][1]] += 6
                            print('Away SP Win')
                print('--------------------------------------------------------------------------------------------------')
                print('--------------------------------------------GAME-END----------------------------------------------')
                print('--------------------------------------------------------------------------------------------------')
                # push player game scores to all sim scores counter
                for u in pull.sumFP:
                    pull.gameFP[u].append(pull.sumFP[u])

                #Restore default values
                defaults.restart.reset(None)
            # All games simmed n times, advances to next round
            i += 1
            if i % 1000 == 0:
                print(i)
                #print((time.time() - tss) / 60)

        #Summary of Player Scores
        final = {}
        avg = 0
        for row in pull.probs:
            key = row[1]
            final[key] = pull.gameFP[pull.names[avg]]
            print(pull.names[avg]+' '+str(sum(final[pull.names[avg]])/sims))
            avg+=1

        #Summary of Team Scores
        scr = 0
        while scr < len(pull.team):
            print(pull.team[scr]+": "+str(pull.scores[pull.team[scr]]/sims))
            scr+=1

        templist = []
        pl = 0
        while pl < len(final.keys()):
            Table_dict = {'Name': list(final.keys())[pl], 'FP': str(sum(final[pull.names[pl]]) / sims)}
            templist.append(Table_dict)
            df = pd.DataFrame(templist)
            pl += 1
        df.to_csv(r'C:\Users\Steven\Desktop\DFS\MLB\MLBsim.csv')












