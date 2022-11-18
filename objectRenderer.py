import pygame
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.wallTextures = self.loadWallTextures()

    def draw(self):
        self.renderObjects()

    def renderObjects(self):
        listObjects = self.game.raycast.objectsToRender
        for depth, image, pos in listObjects:
            self.game.screen.blit(image, pos)
    
    @staticmethod
    def getTexture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture,res)
    
    def loadWallTextures(self):
        return {
            '_': self.getTexture("Resources/floor.png"),
            '1': self.getTexture("Resources/walls.jpg")
        }
