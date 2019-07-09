import pygame
from Singleton import Singleton


class Platform(metaclass=Singleton):
    def __init__(self, color, x, y, widht, height, screenWidth):
        self.rect = pygame.Rect(x, y, widht, height)
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = color
        self.vel = 10
        self.screen_width = screenWidth

    def move_sideways(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < self.screen_width - self.width:
            self.x += self.vel

    def update(self):
        self.move_sideways()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def handle_events(self, event):
        pass

    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
