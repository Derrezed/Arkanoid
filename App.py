import numpy as np
import pygame
from Platform import Platform
from Ball import Ball
from BlockHandler import BlockHandler
screenWidth = 800
screenHeight = 600

pygame.init()

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
colorrandom = list(np.random.choice(range(256), size=3))


if __name__ == '__main__':
    platform = Platform(colorrandom, 330, 550, 150, 30, 800)
    ball = Ball((255, 255, 255), 300, 500, 15, 15)
    blocks = BlockHandler()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        platform.update()
        ball.update()

        window.fill((0x00,) * 3)

        ball.show(window)
        platform.show(window)
        for i in range(len(blocks.blocks)):
           blocks.blocks[i].show(window)

        collisionIndex = ball.rect.collidelist(blocks.blocks)
        print(collisionIndex)
        if collisionIndex != -1:
            ball.reverseY()
            blocks.blocks.pop(collisionIndex)
        pygame.display.update()
        clock.tick(60)