class UnitClass:

    def __init__(self,growthRates,name,advClass):
        self.growthRates = growthRates;
        self.name = name;
        self.advClass = advClass;
    
    def setGrowthRates(self, hp, str, mag, skl, spd, lck, defe, res):
        self.growthRates.setStats(hp, str, mag, skl, spd, lck, defe, res);

    def setName(self, name):
        self.name = name;

    def setAdvClass(self, advClass):
        self.advClass = advClass;

    def getGrowthRates(self):
        return self.growthRates;

    def getName(self):
        return self.name;

    def getAdvClass(self):
        return self.advClass;