class Stats:

    def __init__(self, hp, str, mag, skl, spd, lck, defe, res):
        self.hp = hp;
        self.str = str;
        self.mag = mag;
        self.skl = skl;
        self.spd = spd;
        self.lck = lck;
        self.defe = defe;
        self.res = res;

    def setStats(self, hp, str, mag, skl, spd, lck, defe, res):
        self.hp = hp;
        self.str = str;
        self.mag = mag;
        self.skl = skl;
        self.spd = spd;
        self.lck = lck;
        self.defe = defe;
        self.res = res;

    def setHp(self,hp):
        self.hp = hp;

    def setStr(self,str):
        self.str = str;

    def setMag(self,mag):
        self.mag = mag;

    def selfSkl(self,skl):
        self.skl = skl;

    def selfSpd(self,spd):
        self.spd = spd;

    def selfLck(self,lck):
        self.lck = lck;

    def selfDefe(self,defe):
        self.defe = defe;

    def selfRes(self,res):
        self.res = res;

    def getStats(self):
        return self;

    def getDefe(self):
        return self.defe;

    def getHp(self):
        return self.hp;

    def getLck(self):
        return self.lck;

    def getMag(self):
        return self.mag;

    def getRes(self):
        return self.res;

    def getSkl(self):
        return self.skl;

    def getSpd(self):
        return self.spd;

    def getStr(self):
        return self.str;