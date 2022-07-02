import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480
x = 300
y = 220

tela = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption('Lil Game')
while True:
    clock.tick(120)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x -= 1
    if pygame.key.get_pressed()[K_d]:
        x += 1
    if pygame.key.get_pressed()[K_s]:
        y += 1
    if pygame.key.get_pressed()[K_w]:
        y -= 1
    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))


    pygame.display.update()
