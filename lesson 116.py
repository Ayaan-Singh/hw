import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
caption = pygame.display.set_caption('my first game screen')
r = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        
            r = False
    if not r:
        break

    pygame.display.update()
pygame.quit()
m = (58, 58, 58)