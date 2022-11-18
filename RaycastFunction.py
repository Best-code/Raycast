import pygame
import numpy
from PygameEngine import GameEngine
from settings import *

class RayCasting:

    def __init__(self, game):
        self.game = game
        self.raycastingResult = []
        self.objectsToRender = []
        self.textures = self.game.ObjectRenderer.wallTextures
    
    def getObjectsToRender(self):
        self.objectsToRender = []
        for ray, values in enumerate(self.raycastingResult):
            depth, proj_height, texture, offset = values

            if proj_height < HEIGHT:
                wallColumn = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE)
                wallColumn = pygame.transform.scale(wallColumn, (SCALE, proj_height))
                wallPos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                textureHeight = TEXTURE_SIZE * HEIGHT / proj_height
                wallColumn = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - textureHeight // 2,
                    SCALE, textureHeight
                )
                wallColumn = pygame.transform.scale(wallColumn, (SCALE, HEIGHT))
                wallPos = (ray * SCALE, 0)
            self.objectsToRender.append((depth, wallColumn, wallPos))

    def rayCast(self):
        self.raycastingResult = []
        texture_vert, texture_hor = 1, 1

        ox, oy = self.game.wasd.pos
        x_map, y_map = (int(ox),int(oy))

        ray_angle = self.game.wasd.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = numpy.sin(ray_angle)
            cos_a = numpy.cos(ray_angle)

            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.MAP.wallMap:
                    texture_hor = self.game.MAP.wallMap[tile_hor]
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

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.MAP.wallMap:
                    texture_vert = self.game.MAP.wallMap[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth, texture offset
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # remove fishbowl effect
            depth *= numpy.cos(self.game.wasd.angle - ray_angle)
            

            # 3d projection
            proj_height = SCREEN_DIST / (depth + 0.0001)
            self.raycastingResult.append((depth, proj_height, texture, offset))
            
            # ray casting result
            #self.ray_casting_result.append((depth, proj_height, texture, offset))
            #pygame.draw.line(self.game.screen, "yellow", (ox*CELLSIZE, oy*CELLSIZE), (ox*CELLSIZE + depth*CELLSIZE*cos_a, oy*CELLSIZE + depth*CELLSIZE*sin_a))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.rayCast()
        self.getObjectsToRender()