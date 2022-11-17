from PygameEngine import GameEngine
import pygame
from pygame.locals import *
import numpy
from map import Map
import math

class Circle:

    keySpeed = .01
    rotateSpeed = .3
    speedSin, speedCos = 0,0
    angle = 0
    keyX = 5
    keyY = 10
    pos = (1,1)
    radius = 25
    
    def __init__(self, rgb, map):
        self.rgb = rgb
        self.map = map
    
    def placePlanet(self):
        pass
    """
      if pygame.key.get_pressed()[K_SPACE]:
        self.keyX = pygame.mouse.get_pos()[0]
        self.keyY = pygame.mouse.get_pos()[1]
    """

    def draw(self, surface):
        self.pos = (self.keyX,self.keyY)
        pygame.draw.circle(surface, self.rgb,
                           (self.keyX*self.map.CELLSIZE,self.keyY*self.map.CELLSIZE), self.radius)
        # Direction tracker
        pygame.draw.circle(surface, (0,0,0),
                           (self.keyX*self.map.CELLSIZE+numpy.cos(self.angle)*self.radius,self.keyY*self.map.CELLSIZE+numpy.sin(self.angle)*self.radius), self.radius//3)

    def noWall(self, x, y):
        # Return True if location is not a wall
        return (x,y) not in self.map.wallMap

    def playerCollision(self, dx, dy):

        if self.noWall(int((self.keyX + dx)), int(self.keyY)):
            self.keyX += dx
        if self.noWall(int(self.keyX), int((self.keyY + dy))):
            self.keyY += dy


    def move(self):
        sinA = numpy.sin(self.angle)
        cosA = numpy.cos(self.angle)
        speed = self.keySpeed * GameEngine.deltaTime
        dx = dy = 0
        speedSin = speed * sinA
        speedCos = speed * cosA
        
        if pygame.key.get_pressed()[K_w]:
            #self.keySpeed = abs(self.keySpeed)*-1
            dx += speedCos
            dy += speedSin
        if pygame.key.get_pressed()[K_s]:
           # self.keySpeed = abs(self.keySpeed)
            dx += -speedCos
            dy += -speedSin
        if pygame.key.get_pressed()[K_a]:
           # self.keySpeed = abs(self.keySpeed)*-1
            dx += speedSin
            dy += -speedCos
        if pygame.key.get_pressed()[K_d]:
           # self.keySpeed = abs(self.keySpeed)
            dx += -speedSin
            dy += speedCos

        self.playerCollision(dx, dy)
        
        if pygame.key.get_pressed()[K_LEFT]:
            self.angle -= self.rotateSpeed * speed
        if pygame.key.get_pressed()[K_RIGHT]:
            self.angle += self.rotateSpeed * speed
        self.angle%=math.tau


    def update(self):
        self.move()
        self.placePlanet() 