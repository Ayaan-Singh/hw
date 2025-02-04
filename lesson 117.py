import pygame
import random
sw = 800
sh =600
screen = pygame.display.set_mode((sw,sh))
bgcolor = pygame.Color("white")
screen.fill(bgcolor)
pygame.draw.rect(screen,pygame.Color("red"),(0,0,30,30))
running = True
while True :
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False
      pygame.display.flip()
pygame.quit()
