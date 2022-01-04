class GameCharacteristics:
    def __init__(self,numberOfAliens,timeOfAlienMouvement):
        self.numberOfAliens=numberOfAliens
        self.timeOfAlienMouvement=timeOfAlienMouvement
        self.score=0

    def incrementScore(self):
        self.score+=1


