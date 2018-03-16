class GameBools:
    def __init__(self):
        self.birthright = False;
        self.conquest = False;
        self.revelations = False;

    def setGameBools(self,birthright,conquest,revelations):
        self.birthright = birthright;
        self.conquest = conquest;
        self.revelations = revelations;

    def getGameBools(self):
        return self;

    def getBirthright(self):
        return self.birthright;

    def getConquest(self):
        return self.conquest;

    def getRevelations(self):
        return self.revelations;

    def setBirthright(self,birthright):
        self.birthright = birthright;

    def setConquest(self,conquest):
        self.conquest = conquest;

    def setRevelations(self,revelations):
        self.revelations = revelations;
