import pygame
from Platform import Platform


class Ball:
    def __init__(self, color, x, y, widht, height):
        self.rect = pygame.Rect(x, y, widht, height)
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = color
        self. acceleration = 5
        self.velx = 5
        self.vely = -5
        self.lives = 1
        self.score = 0

    def ball_movement(self):
        self.rect.x += self.velx
        self.rect.y += self.vely

    def reverseY(self):
        self.vely = -self.vely

    def reverseX(self):
        self.velx = -self.velx

    def collision_edges(self):
        if self.rect.left <= 0:
            self.reverseX()
        elif self.rect.right >= 800:
            self.reverseX()
        if self.rect.top <= 0:
            self.reverseY()
        if self.rect.bottom >= 600:
            self.reverseY()

    def collision_platform(self):
        platform = Platform()
        if self.rect.bottom >= platform.rect.top and self.rect.bottom <= 600 and self.rect.centerx < platform.rect.right and self.rect.centerx > platform.rect.left:
            self.reverseY()

    def check_ball_out(self):
        if self.rect.bottom >= 600:
            self.lives -= 1
            print(self.lives)

    def update(self):
        self.ball_movement()
        self.collision_edges()
        self.collision_platform()
        self.check_ball_out()

    def handle_events(self, event):
        pass

    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
