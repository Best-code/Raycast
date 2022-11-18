from PygameEngine import GameEngine
from Circle import Circle
import pygame
from pygame.locals import *
import sys
from map import Map
from RaycastFunction import RayCasting
from settings import *
from gui import GUI

class RaycastGame(GameEngine):

    def __init__(self):
        super().__init__()
        self.load()

        self.MAP = Map(self)

        self.gui = GUI(self, self.MAP)
        
        # Circle controllable with WASD
        self.wasd = Circle((123, 255, 123), self.MAP)

        self.raycast = RayCasting(self)

    def draw(self):
            # Draw MAP array
            #self.MAP.drawMap()
            #self.MAP.drawGrid()
            #self.wasd.draw(self.screen)
            #self.gui.drawGui()
            pass

    def update(self):
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
                # Allows the map to change once per Key down
                if event.type == pygame.KEYDOWN:
                    self.MAP.update()


            # Update.
            self.update()
            # Draw
            self.draw()

            # Drawing the Raycast collisino ray
            self.raycast.update()


            pygame.display.flip()
            self.fpsClock.tick(FPS)
