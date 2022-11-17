import pygame
import numpy
from PygameEngine import GameEngine
import sys
import math

class RayCasting:

    FOV = numpy.pi/5
    HALF_FOV = FOV/2
    NUM_RAYS = GameEngine.WIDTH//2
    HALF_NUM_RAYS = NUM_RAYS//2
    DELTA_ANGLE = FOV/NUM_RAYS
    MAX_DEPTH = 20

    def __init__(self, game):
        self.game = game


    def rayCast(self):
        scale = self.game.CELLSIZE

        ox, oy = self.game.wasd.pos
        x_map = int(ox)
        y_map = int(oy)

        rayAngle = self.game.wasd.angle 
        # Get the direction the rys are going to shoot in
        dirX = numpy.cos(rayAngle)
        dirY = numpy.sin(rayAngle)

        # The distance to the next vertical and horizontal line
        sideDistX = sideDistY = 0

        # If the angle is perpendicular to another axis and will never cross it,
        #    set that length to max
        #    else get the trig function
        deltaDistX = 1 if dirX==0 else abs(1/dirX)
        deltaDistY = 1 if dirY==0 else abs(1/dirY)
        
        # How much we will step by
        dx = 0
        dy = 0
        
        if dirX < 0:
            dx = -1
            sideDistX = (ox - x_map) * deltaDistX
        else:
            dx = 1
            sideDistX = (x_map + 1.0 - ox) * deltaDistX

        if (dirY < 0):
            dy = -1
            sideDistY = (oy - y_map) * deltaDistY
        else:
            dy = 1
            sideDistY = (y_map + 1.0 - oy) * deltaDistY
        
        for i in range(self.MAX_DEPTH):
            # If we hit a wallstop the loop
            if((x_map, y_map) in self.game.MAP.wallMap):
                break
            # If we can go more on the x axis before catching the y axis we will
            if(sideDistX < sideDistY):
                sideDistX += deltaDistX
                x_map += dx
            else:
            # If we can go more on the y axis before catching the x axis we will
                sideDistY += deltaDistY
                y_map += dy
        

        pygame.draw.line(self.game.screen, "blue", (ox*scale, oy*scale), (x_map*scale, y_map*scale), 5)
        pygame.draw.circle(self.game.screen, "pink", (x_map*scale,y_map*scale),15)


    def update(self):
        self.rayCast()