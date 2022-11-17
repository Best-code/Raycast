import pygame
from PygameEngine import GameEngine
from pygame.locals import *
import os
class Map:
    
    CELLSIZE = 47
    ROWS = GameEngine.HEIGHT//CELLSIZE
    COLS = GameEngine.WIDTH//CELLSIZE

    def __init__(self):
        """
        self.gameMap = [
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
        ["1","_","_","_","_","_","1","1","_","_","_","_","_","_","_","_","_","_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "1", "_", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","_","_","1","_","_","_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "1", "1", "1", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","_","_","1","_","1", "-", "1", "1", "_", "1", "_", "_", "_", "_", "_", "_", "1", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","_","_","1","_","1", "-", "1", "1", "_", "1", "_", "_", "_", "_", "_", "_", "1", "_", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","1", "_", "_", "1", "_", "1", "_", "_", "_", "_", "_", "1", "1", "_", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","_", "_", "_", "1", "_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","_","_", "_", "_", "_", "1", "_", "_", "_", "_", "1", "1", "1", "1", "1", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","1", "_", "_", "1", "_", "1", "_", "_", "_", "_", "_", "1", "1", "_", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","_","1","_","_","1","_","_", "_", "_", "1", "_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_","_","_", "_", "_", "_", "1", "_", "_", "_", "_", "1", "1", "1", "1", "1", "1"],
        ["1","_","_","_","_","_","1","1","1","_","_","1","1","_","_","_","1","_", "1", "_", "_", "1", "_", "_", "_", "_", "_", "1", "_", "_", "_", "1"],
        ["1","1","1","1","1","1","1","1","1","_","_","1","_","_","_","_","1","_", "1", "_", "_", "1", "_", "_", "_", "_", "_", "1", "_", "_", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","1","1","1","1","_","1","_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","_","_","1","_","_", "_", "_", "1", "_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
        ["1","_","_","_","_","_","1","1","1","1","1","1","1","_","1","_","_","_", "_", "_", "_", "1", "_", "_", "_", "_", "1", "1", "1", "1", "1", "1"],
        ["1","_","_","_","_","_","1","1","_","_","_","_","_","_","_","_","1","_", "1", "_", "_", "1", "_", "_", "_", "_", "_", "1", "_", "_", "_", "1"],
        ["1","_","_","_","_","_","_","_","_","_","_","_","_","1","1","_","1","_", "1", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
    ]
        """
        self.gameMap=[[""]*33]*19
        self.loadMap()
        self.wallMap = {}
        self.getMap()
        
        wall = pygame.image.load(os.path.join("Resources","walls.jpg")).convert()
        floor = pygame.image.load(os.path.join("Resources","floor.png")).convert()
        self.tiles = [wall, floor]

    def loadMap(self):
        with open("map.txt") as file:
            for indexY, line in enumerate(file):
                self.gameMap[indexY] = line.split(' ')

    def editMap(self):
        if not pygame.key.get_pressed()[K_c]:
            return
        mouseX, mouseY = pygame.mouse.get_pos()

        mouseX = int(mouseX // self.CELLSIZE)
        mouseY = int(mouseY // self.CELLSIZE)

        mapType = self.gameMap[mouseY][mouseX]
        if mapType == "1":
            self.gameMap[mouseY][mouseX] = "_"
        elif mapType == "_":
            self.gameMap[mouseY][mouseX] = "1"
        self.wallMap.clear()
        self.getMap()

        with open("map.txt", 'w') as file:
            for y in self.gameMap:
                for x in y:
                    file.write(x+(" " if x!= "\n" else ""))

    def update(self):
        self.editMap()
    
    def blit(self, index, x, y):
        cellsize = self.CELLSIZE
        GameEngine.screen.blit(self.tiles[index],(x*cellsize, y*cellsize,cellsize,cellsize))
            
    def drawMap(self):
        for yInd, y in enumerate(self.gameMap):
            for xInd in range(len(y)):
                if (y[xInd] == "1"):
                                                    # WALL COLOR
                    #pygame.draw.rect(GameEngine.screen, (255, 69, 69),
                      #               pygame.Rect(xInd*self.CELLSIZE, yInd*self.CELLSIZE,
                       #                          self.CELLSIZE, self.CELLSIZE))
                       self.blit(0,xInd,yInd)
                else:
                       self.blit(1,xInd,yInd)

                                                            # MAP COLOR
                """ pygame.draw.rect(GameEngine.screen, (50, 150, 30),
                pygame.Rect(xInd*self.CELLSIZE, yInd*self.CELLSIZE,
                self.CELLSIZE, self.CELLSIZE))
                """
        
    def drawGrid(self):
        for x in range(1, self.COLS+1):
            pygame.draw.line(GameEngine.screen, (0xff, 0xff, 0xff), (
                x*self.CELLSIZE, 0), (x*self.CELLSIZE, GameEngine.HEIGHT))
        for y in range(1, self.ROWS+1):
            pygame.draw.line(GameEngine.screen, (0xff, 0xff, 0xff),
                             (0, y*self.CELLSIZE), (GameEngine.WIDTH, y*self.CELLSIZE))

    def getMap(self):
        for j, row in enumerate(self.gameMap):
            for i, value in enumerate(row):
                if value == "1":
                    self.wallMap[(i, j)] = value