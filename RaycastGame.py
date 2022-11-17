from PygameEngine import GameEngine
from Circle import Circle
import pygame
from pygame.locals import *
import sys
from map import Map
from RaycastFunction import RayCasting

class RaycastGame(GameEngine):

    def __init__(self):
        super().__init__()
        self.load()

        self.MAP = Map()
        
        self.CELLSIZE = self.MAP.CELLSIZE
        self.planet = Circle((0,0,0), self.MAP)

        # Circle controllable with WASD
        self.wasd = Circle((123, 255, 123), self.MAP)

        self.raycast = RayCasting(self)

    def draw(self):
            # Draw MAP array
            self.MAP.drawMap()
            self.MAP.drawGrid()

            # Draw mouse character
            #pygame.draw.circle(self.screen, (0, 0, 0),
                               #(self.plane), Circle.radius)
            # Draw planet
           # self.planet.draw(self.screen)
            # Draw wasd character
            self.wasd.draw(self.screen)
            # Connect mouse and wasd characters with a line
            #pygame.draw.line(self.screen, (255, 255, 255), self.planet.pos, (self.wasd.keyX, self.wasd.keyY), 5)

    def update(self):
      self.planet.update()
      self.wasd.update()

    def run(self):
        # Game loop.
        while True:
          #This gets written over. Only for clearing screen before each draw
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.MAP.update()
                    print((pygame.mouse.get_pos()[0]//self.CELLSIZE),(pygame.mouse.get_pos()[1]//self.CELLSIZE))


            # Update.
            self.update()
            # Draw
            self.draw()
            self.raycast.update()


            pygame.display.flip()
            self.fpsClock.tick(self.FPS)
