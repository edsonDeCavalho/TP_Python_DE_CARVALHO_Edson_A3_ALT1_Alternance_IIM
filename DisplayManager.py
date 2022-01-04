from GameParameters import GameParameters
from GameCharacteristics import GameCharacteristics
import pygame
class DisplayManager:
    #Displays the title
    def displayTitle(self,screen,background):
        font = pygame.font.SysFont(None, 50)
        img = font.render('Alien Invaders', True, GameParameters.WHITE)
        screen.blit(img, (390, 20))

    def displayScore(self,screen,aircraft,gc):
        font = pygame.font.SysFont(None, 40)
        img = font.render(f' Dead aliens : {gc.score}', True, GameParameters.WHITE)
        screen.blit(img, (20, 20))
        img2 = font.render(f' Lifes : {aircraft.life}', True, GameParameters.WHITE)
        screen.blit(img2, (20,70 ))


