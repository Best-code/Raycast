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
        ox, oy = self.game.wasd.pos
        x_map = int(ox)
        y_map = int(oy)

        ray_angle = self.game.wasd.angle - self.HALF_FOV + 0.000001
        for ray in range(self.NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            print("YHor: ",y_hor, " DY:", dy, " Depth Hor: ",  depth_hor, "X Hor: ", x_hor,
             " Delta Depth: ", delta_depth, " DX: ", dx)

            for i in range(self.MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.MAP.wallMap:
                   # print("INSIDE HOR")
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(self.MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.MAP.wallMap:
                  #  print("INSIDE VERT")
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth, texture offset
            if depth_vert < depth_hor:
                depth = depth_vert 
                #y_vert %= 1
                #offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth = depth_hor
            

                #x_hor %= 1
                #offset = (1 - x_hor) if sin_a > 0 else x_hor

            # remove fishbowl effect
            #depth *= math.cos(self.game.wasd.angle - ray_angle)

            # projection
            #proj_height = SCREEN_DIST / (depth + 0.0001)

            # ray casting result
            #self.ray_casting_result.append((depth, proj_height, texture, offset))

            ray_angle += self.DELTA_ANGLE
            pygame.draw.line(self.game.screen, "yellow", (ox*self.game.CELLSIZE,oy*self.game.CELLSIZE), (ox*self.game.CELLSIZE+depth*cos_a, oy*self.game.CELLSIZE+depth*sin_a), 1)

    def update(self):
        self.rayCast()