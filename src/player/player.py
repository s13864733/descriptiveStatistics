import pygame

BLUE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, name, money):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.rect = pygame.Rect(x, y, 50, 50)
        self.name = name
        self.money = money
        self.speed = 50
    
    def handleMovement(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= dt * self.speed
        if keys[pygame.K_s]:
            self.pos.y += dt * self.speed
        if keys[pygame.K_a]:
            self.pos.x -= dt * self.speed
        if keys[pygame.K_d]:
            self.pos.x += dt * self.speed

    def update(self, dt):
        self.handleMovement(dt)

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
