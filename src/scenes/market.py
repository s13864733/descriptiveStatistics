import pygame
from settings import (
    GAME_HEIGHT, GAME_WIDTH,
    RED, GREEN, BLACK, CHARCOAL_BLUE
    )

class Market:
    def __init__(self):
        self.btnW = 100
        self.btnH = 30

        self.sell_btn = pygame.Rect(100, 100, self.btnW, self.btnH)
        self.buy_btn = pygame.Rect(100, 200, self.btnW, self.btnH)

    def draw(self, screen):
        screen.fill(CHARCOAL_BLUE)

        pygame.draw.rect(screen, RED, self.sell_btn, border_radius=10)
        pygame.draw.rect(screen, GREEN, self.buy_btn, border_radius=10)

        screen.blit(pygame.font.SysFont("Arial", 20).render("Sell", True, BLACK), (self.sell_btn.x + self.btnW / 2 - 15, self.sell_btn.y + self.btnH / 2 - 10))
        screen.blit(pygame.font.SysFont("Arial", 20).render("Buy", True, BLACK), (self.buy_btn.x + self.btnW / 2 - 15, self.buy_btn.y + self.btnH / 2 - 10))