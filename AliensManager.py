from GameParameters import GameParameters
from Utils import Utils
from Alien import Alien
import pygame
class AliensManager:

    def __init__(self):
        self.utils=Utils()

    def createAliens(self,aliens,actualAlienId):
        # creation of an alien :

            alien = Alien(actualAlienId, self.utils.getRandomNuMberForXPosition(), 1)
            aliens.append(alien)
            actualAlienId += 1
    def removeAliens(self,aliens):
        for alien in aliens:
            if not(alien.isAlive()) and (len(aliens))>0 :
                aliens.remove(alien)
            if alien.isGone() and (len(aliens))>0 :
                aliens.remove(alien)
    def checkIfAlienIsGone(self,aliens):
        for alien in aliens:
            if alien.y > GameParameters.WINDOW_HEIGHT :
                alien.gone=True
    def mouveAliens(self,aliens):

            for alien in aliens :
                alien.decrement()