import pygame



class Block(object):
    def __init__(self, color, x, y, widht, height):
        self.rect = pygame.Rect(x, y, widht, height)
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = color


    def update(self):
        pass

    def handle_events(self, event):
        pass

    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

