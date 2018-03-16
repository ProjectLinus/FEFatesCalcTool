from Stats import Stats;
from GameBools import GameBools;

class Character:

    def __init__(self,growthRates,name):
        self.gameBools = GameBools();
        self.growthRates = growthRates;
        self.name = name;
    
    def setGrowthRates(self, hp, str, mag, skl, spd, lck, defe, res):
        self.growthRates.setStats(hp, str, mag, skl, spd, lck, defe, res);

    def setGameBools(self, gameBools):
        self.gameBools = gameBools;

    def setBirthright(self, birthright):
        self.gameBools.setBirthright(birthright);

    def setConquest(self, conquest):
        self.gameBools.setConquest(conquest);

    def setRevelations(self, revelations):
        self.gameBools.setRevelations(revelations);

    def setName(self, name):
        self.name = name;

    def getGameBools(self):
        return self.gameBools;

    def getGrowthRates(self):
        return self.growthRates;

    def getName(self):
        return self.name;