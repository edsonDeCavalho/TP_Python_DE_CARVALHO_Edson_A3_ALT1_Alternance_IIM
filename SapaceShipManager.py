from SpaceShip import SapaceShip
import pygame
from GameParameters import GameParameters
class SapaceShipManager:


    def moveToLeftSpaceSHip(self, s):
        s.decrementX()

    def moveToRightSpaceSHip(self, s):
        s.incrementX()

    def moveToUpSpaceSHip(self, s):
        s.decrementY()

    def moveToDownSpaceSHip(self, s):
        s.incrementY()

