import pygame
from PygameEngine import GameEngine
from pygame.locals import *
import os

from settings import *

class Map:

    def __init__(self, game):

        self.game = game

        
        self.gameMap = [
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","1","_","_","_","_","_","_","_","_","_","_","1","_","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","_","_","1","_","_","_","_","_","_","_","_","_","_","_","_","1","1","1","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","_","_","1","_","1","-","1","1","_","1","_","_","_","_","_","_","1","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","_","_","1","_","1","-","1","1","_","1","_","_","_","_","_","_","1","_","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","1","_","_","1","_","1","_","_","_","_","_","1","1","_","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","_","_","_","1","_","1","_","_","_","_","_","_","_","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","_","_","_","_","_","1","_","_","_","_","1","1","1","1","1","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","1","_","_","1","_","1","_","_","_","_","_","1","1","_","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","_","_","_","1","_","1","_","_","_","_","_","_","_","_","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","_","_","_","1","_","1","_","_","_","_","_","_","_","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","_","_","_","_","_","1","_","_","_","_","1","1","1","1","1","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","_","_","_","_","_","1","_","_","_","_","1","1","1","1","1","1"],
        ["1","_","_","_","_","_","1","1","1","_","_","1","1","_","_","_","1","_","1","_","_","1","_","_","_","_","_","1","_","_","_","1"],
        ["1","1","1","1","1","1","1","1","1","_","_","1","_","_","_","_","1","_","1","_","_","1","_","_","_","_","_","1","_","_","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","1","1","_","1","_","1","_","_","_","_","_","_","_","_","_","_","_","_","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","_","_","1","_","_","_","_","1","_","1","_","_","_","_","_","_","_","_","1"],
        ["1","_","_","_","_","_","1","1","1","1","1","1","1","_","1","_","_","_","_","_","_","1","_","_","_","_","1","1","1","1","1","1"],
        ["1","_","_","_","_","_","1","1","_","_","_","_","_","_","_","_","1","_","1","_","_","1","_","_","_","_","_","1","_","_","_","1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","1","_","_","_","_","_","_","_","_","_","_","_","_","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
    ]
        
        # TODO  FIX LOAD MAP
        #self.gameMap=[[""]*(COLS+1)]*(ROWS+1)
        #self.loadMap()
        self.wallMap = {}
        self.getMap()


        """
        2d Textures 

        wall = pygame.image.load(os.path.join("Resources","walls.jpg")).convert()
        floor = pygame.image.load(os.path.join("Resources","floor.png")).convert()

        self.tiles = [wall, floor]
        self.tileIndicator = {wall:"1", floor:"_"}

        self.currentTileIndex = 0
        self.currentTile = self.tileIndicator[self.tiles[self.currentTileIndex]]
        """ 

    # FIX THIS
    def loadMap(self):
        with open("map.txt") as file:
            for indexY, line in enumerate(file):
                for character in line.splitlines():
                    self.gameMap[indexY] = character
                    print(self.gameMap[indexY])

    """
    2d attributes
    def changeTile(self):
        if pygame.key.get_pressed()[K_1]:
            print(self.currentTileIndex, self.currentTile)
            self.currentTileIndex+=1
            self.currentTileIndex%=len(self.tiles)
            self.currentTile = self.tileIndicator[self.tiles[self.currentTileIndex]]

    def editMap(self):
        if not pygame.key.get_pressed()[K_c]:
            return
        mouseX, mouseY = pygame.mouse.get_pos()

        mouseX = int(mouseX // CELLSIZE)
        mouseY = int(mouseY // CELLSIZE)

        /*
        mapType = self.gameMap[mouseY][mouseX]
        if mapType == "1":
            self.gameMap[mouseY][mouseX] = "_"
        elif mapType == "_":
            self.gameMap[mouseY][mouseX] = "1"
        */

        self.gameMap[mouseY][mouseX] = self.currentTile
        self.wallMap.clear()
        self.getMap()

        with open("map.txt", 'w') as file:
            for y in self.gameMap:
                for x in y:
                    file.write(x+(" " if x!= "\n" else ""))
    """

    def update(self):
        #self.editMap()
        #self.changeTile()
        pass
    """
    2d Attributes 
    def blit(self, index, x, y):
        GameEngine.screen.blit(self.tiles[index],(x*CELLSIZE, y*CELLSIZE,CELLSIZE,CELLSIZE))
            
    def drawMap(self):
        for yInd, y in enumerate(self.gameMap):
            for xInd in range(len(y)):
                if (y[xInd] == "1"):
                                                    # WALL COLOR
                    #pygame.draw.rect(GameEngine.screen, (255, 69, 69),
                      #               pygame.Rect(xInd*CELLSIZE, yInd*CELLSIZE,
                       #                          CELLSIZE, CELLSIZE))
                       self.blit(0,xInd,yInd)
                else:
                       self.blit(1,xInd,yInd)

                                                            # MAP COLOR
                /* pygame.draw.rect(GameEngine.screen, (50, 150, 30),
                pygame.Rect(xInd*CELLSIZE, yInd*CELLSIZE,
                CELLSIZE, CELLSIZE))
                */
        
    def drawGrid(self):
        for x in range(1, COLS+1):
            pygame.draw.line(GameEngine.screen, (0xff, 0xff, 0xff), (
                x*CELLSIZE, 0), (x*CELLSIZE, HEIGHT))
        for y in range(1, ROWS+1):
            pygame.draw.line(GameEngine.screen, (0xff, 0xff, 0xff),
                             (0, y*CELLSIZE), (GameEngine.WIDTH, y*CELLSIZE))
    """

    def getMap(self):
        for j, row in enumerate(self.gameMap):
            for i, value in enumerate(row):
                if value == "1":
                    self.wallMap[(i, j)] = value