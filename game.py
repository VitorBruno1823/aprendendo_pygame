import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480
x = 300
y = 0

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


    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))
    if y >= height:
        y = 0
    y += 1


    pygame.display.update()
