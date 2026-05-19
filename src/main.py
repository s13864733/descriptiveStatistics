import pygame
from player import *

pygame.init()

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
dt = 0

player = Player(100, 100, "P1", 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(dt)

    screen.fill((100, 100, 100))
    player.draw(screen)

    pygame.display.flip()
    dt = clock.tick(120) / 1000