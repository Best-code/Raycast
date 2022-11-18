import pygame
import numpy
from PygameEngine import GameEngine
from settings import *

class RayCasting:

    def __init__(self, game):
        self.game = game

    """
    def rayCast(self):
        ox, oy = self.game.wasd.pos
        rayAngle = self.game.wasd.angle
        aX = numpy.cos(rayAngle)
        aY = numpy.sin(rayAngle)

        for ray in range(WIDTH):
            x_map = int(ox)
            y_map = int(oy)

            print(ray, rayAngle)
            # Get the direction the rys are going to shoot in
    
            cameraX = 2*ox / COLS - 1; #x-coordinate in camera space
            dirX = aX + aX * cameraX 
            dirY = aY + aY * cameraX 

            # The distance to the next vertical and horizontal line
            sideDistX = sideDistY = 0

            # If the angle is perpendicular to another axis and will never cross it,
            #    set that length to max
            #    else get the trig function
            deltaDistX = 1e30 if dirX == 0 else abs(1/dirX)
            deltaDistY = 1e30 if dirY == 0 else abs(1/dirY)

            side = int

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

            for i in range(MAX_DEPTH):
                # If we hit a wallstop the loop
                if ((x_map, y_map) in self.game.MAP.wallMap):
                    break
                # If we can go more on the x axis before catching the y axis we will
                if (sideDistX < sideDistY):
                    sideDistX += deltaDistX
                    x_map += dx
                    side = 0
                else:
                    # If we can go more on the y axis before catching the x axis we will
                    sideDistY += deltaDistY
                    y_map += dy
                    side = 1

            if (side == 0):
                perpWallDist = (sideDistX - deltaDistX)
            else:
                perpWallDist = (sideDistY - deltaDistY)

            hit = x_map + (1-dx)/2, y_map + (1-dy)/2


            # Calculate height of line to draw on screen
            lineHeight = int(hit[1] / (perpWallDist + 0.00001))

            #calculate lowest and highest pixel to fill in current stripe
            drawStart = -lineHeight / 2 + hit[1] / 2
            if(drawStart < 0): 
                drawStart = 0
            drawEnd = lineHeight / 2 + hit[1] / 2
            if(drawEnd >= hit[1]):
                drawEnd = hit[1] - 1

            color = "black"
            code = self.game.MAP.gameMap[int(hit[1])][int(hit[0])]
            if code == "1":
                color = "red"
            if code == "2":
                color = "green"
                
            rayAngle+=DELTA_ANGLE
                
            pygame.draw.line(self.game.screen, color, (hit[0]*CELLSIZE, drawStart*CELLSIZE), (hit[0]*CELLSIZE, drawEnd*CELLSIZE), CELLSIZE)


            pygame.draw.line(self.game.screen, "blue", (ox*CELLSIZE, oy*CELLSIZE), (hit[0]*CELLSIZE, hit[1]*CELLSIZE), 5)
            pygame.draw.circle(self.game.screen, "pink", (hit[0]*CELLSIZE,hit[1]*CELLSIZE),15)
        """
    
    def rayCast(self):

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
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth, texture offset
            if depth_vert < depth_hor:
                depth = depth_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth = depth_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # remove fishbowl effect
            depth *= numpy.cos(self.game.wasd.angle - ray_angle)
            

            # 3d projection
            proj_height = SCREEN_DIST / (depth + 0.0001)
            color = [255 / (1+depth ** 4 * 0.0001)]*3
            pygame.draw.rect(self.game.screen, color,
                (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
            # ray casting result
            #self.ray_casting_result.append((depth, proj_height, texture, offset))
            #pygame.draw.line(self.game.screen, "yellow", (ox*CELLSIZE, oy*CELLSIZE), (ox*CELLSIZE + depth*CELLSIZE*cos_a, oy*CELLSIZE + depth*CELLSIZE*sin_a))

            ray_angle += DELTA_ANGLE

    def update(self):
        self.rayCast()