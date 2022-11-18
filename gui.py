import pygame
from settings import *

class GUI:

    def __init__(self, game, map):
        self.game = game
        self.map = map
        self.tiles = self.map.tiles
    
    def drawGui(self):
        
        # PRINT THE INVENTORY BACKGROUND
        inventoryBox = pygame.Surface((WIDTH//3,CELLSIZE*1.3))  # the size of your rect
        inventoryBox.set_alpha(128)                # alpha level
        inventoryBox.fill((255,0,255))           # this fills the entire surface
        self.game.screen.blit(inventoryBox, (WIDTH//3,HEIGHT-100+CELLSIZE))    # (x,y) are the top-left coordinates
        
    
        blitTile = pygame.Surface((WIDTH//3-40,CELLSIZE))
        blitTile.fill((0xff,0xff,0xff))
        for index, tile in enumerate(self.tiles):
            blitTile.blit(tile, (index * CELLSIZE, 0, CELLSIZE, CELLSIZE))
            
        self.game.screen.blit(blitTile, (WIDTH//3+20,HEIGHT-100+(CELLSIZE+CELLSIZE*1.3)/2))   # (x,y) are the top-left coordinates
        
        