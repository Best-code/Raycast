import sys
from settings import *
import pygame
from pygame.locals import *

class GameEngine:

  fpsClock = pygame.time.Clock()
  deltaTime = fpsClock.tick(FPS)
  
  WIDTH, HEIGHT = 1500, 982
  screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
  
  def __init__(self):
    self.load()

  def load(self):
    pygame.init()
  
  def draw(self):
    pass
  
  def run(self):
  # Game loop.
    while True:
      # Clear screen before redraw
      self.screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      
      # Draw.
      self.draw()
      
      pygame.display.flip()
      self.deltaTime

 