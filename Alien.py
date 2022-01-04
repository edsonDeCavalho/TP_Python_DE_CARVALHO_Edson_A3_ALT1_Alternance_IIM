from GameParameters import GameParameters
class Alien:
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.alive=True
        self.gone=False
    def decrement(self):
        self.y=self.y+GameParameters.BLOCK_SIZE

    def toStringAlien(self):
        print(f"Alien positions {self.x} and  {self.y} :")
        print(self.x)
        print(self.y)
        print("Is Gone ? :")
        print(self.gone)
        print("Is Alive ? :")
        print(self.alive)
    def die(self):
        self.alive=False
    def isAlive(self):
        return self.alive
    def isGone(self):
        return self.gone