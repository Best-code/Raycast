import sys
 
import pygame
from pygame.locals import *

class GameEngine:

  FPS = 60
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
      # Main map color
      self.screen.fill((30, 150, 50))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      # Update.
      
      # Draw.
      self.draw()
      
      pygame.display.flip()
      self.fpsClock.tick(self.FPS)

 