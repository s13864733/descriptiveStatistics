import pygame
from player import *
from scenes import Market
from settings import GAME_WIDTH, GAME_HEIGHT, FULLSCREEN

pygame.init()

sceneOpen = True
running = True

if FULLSCREEN:
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
dt = 0

player = Player(100, 100, "P1", 0)
market = Market()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not sceneOpen:
        player.update(dt)

        screen.fill((100, 100, 100))
        player.draw(screen)
        player.drawDebug(screen)
    else:
        # market test
        market.draw(screen)

    pygame.display.flip()
    dt = clock.tick(120) / 1000