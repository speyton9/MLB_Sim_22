import box
import teams
class restart:
    def reset(self):
        teams.g = []
        teams.h = []
        teams.a = []
        box.inning = 0
        box.home = 0
        box.away = 0
        box.out = 0
        box.first = 0
        box.second = 0
        box.third = 0
        box.hbo = 1
        box.abo = 1
        teams.hp = []
        teams.ap = []
        teams.hstart = []
        teams.astart = []
        teams.Hdict = {}
        teams.Adict = {}
        teams.lhbo = 0
        teams.labo = 0
        teams.hss = {}
        teams.hss['home'] = 0
        teams.hss['away'] = 0
        teams.hqs = 0
        teams.ass = {}
        teams.ass['home'] = 0
        teams.ass['away'] = 0
        teams.aqs = 0
        teams.hsp = []
        teams.asp = []