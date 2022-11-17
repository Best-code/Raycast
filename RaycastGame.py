from PygameEngine import GameEngine
from Circle import Circle
import pygame
from pygame.locals import *
import sys
import numpy
from map import Map
from RaycastFunction import RayCasting

class RaycastGame(GameEngine):


    # Space bar to place this circle which will connect to the WASD with a line
    planet = Circle((0,0,0))

    planet.keyX = 5
    planet.keyY = 5

    # Grid set up

    def __init__(self):
        super().__init__()
        self.load()

        self.MAP = Map()
        self.CELLSIZE = self.MAP.CELLSIZE

        # Circle controllable with WASD
        self.wasd = Circle((123, 255, 123))

        self.raycast = RayCasting(self)


    def DDA(self):
      #                           -
      #                         * |
      # Remember the Plane is - --m-- +
      #      * = target           |
      #      m = mouse            +

      
      distX = self.wasd.keyX - self.planet.pos[0]
      distY = self.wasd.keyY - self.planet.pos[1]

      #hypotenuse = numpy.sqrt(distX**2+distY**2)
      theta = numpy.arctan((distY/(distX+.0001)))
      theta += numpy.deg2rad(90)
      # print(numpy.rad2deg(theta), " THETA")
      collisionPos = (0,0)

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
      self.planet.placePlanet()
      self.wasd.move()
      self.DDA()
      self.raycast.update()

    def run(self):
        # Game loop.
        while True:
          #This gets written over. Only for clearing screen before each draw
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update.
            self.update()
            # Draw
            self.draw()


            pygame.display.flip()
            self.fpsClock.tick(self.FPS)
