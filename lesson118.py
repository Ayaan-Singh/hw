import pygame
import random
pygame.init()
sw = 800
sh = 600
screen = pygame.display.set_mode([sw, sh])
a = pygame.sprite.Group()
class s1(pygame.sprite.Sprite):
    def __init__(self,height,width):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(0, 550)

sprite = s1(50, 50)
a.add(sprite)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255, 255, 255))
    a.draw(screen)
    if pygame.sprite.spritecollide(a.sprites()[0], a, False):
     sprite.rect.x = max(min(sprite.rect.x, 750), 0)
     sprite.rect.y = max(min(sprite.rect.y, 550), 0)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        sprite.rect.x -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        sprite.rect.x += 1
    if pygame.key.get_pressed()[pygame.K_UP]:
        sprite.rect.y += 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        sprite.rect.y -= 1
pygame.display.flip()
clock.tick(60)


