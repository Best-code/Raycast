import pygame

class GUI:

    def __init__(self, game, map):
        self.game = game
        self.map = map
        self.titles = self.map.tiles
    
    def drawGui(self):
        pygame.draw.rect(self.game.screen, (0xff,0xff,0xff,100), ())