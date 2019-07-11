import numpy as np
import pygame
from Platform import Platform
from Ball import Ball
from BlockHandler import BlockHandler
import random


screenWidth = 800
screenHeight = 600
WHITE = (255, 255, 255)
pygame.init()

window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()
colorrandom = list(np.random.choice(range(256), size=3))
random_start_pos = random.randint(100, 700)
font = pygame.font.SysFont("comicsansms", 30)
score_caption = font.render("Wynik: ", True, WHITE)


def gamewin():
    message = font.render("You win, congratulations!", False, WHITE)
    window.blit(message, ((screenWidth - message.get_width()) / 2, 240))
    pygame.display.update()
    pygame.time.wait(3000)


def gameover():
    message = font.render("You died, game over!", False, WHITE)
    window.blit(message, ((screenWidth - message.get_width()) / 2, 240))
    pygame.display.update()
    pygame.time.wait(3000)


def gameloop():
    platform = Platform(colorrandom, 330, 550, 150, 30, 800)
    ball = Ball(WHITE, random_start_pos, 500, 15, 15)
    blocks = BlockHandler()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        platform.update()
        ball.update()

        window.fill((0x00,) * 3)

        window.blit(score_caption, (0, 0))
        ball.show(window)
        platform.show(window)
        for i in range(len(blocks.blocks)):
           blocks.blocks[i].show(window)

        collisionIndex = ball.rect.collidelist(blocks.blocks)
        if collisionIndex != -1:
            ball.reverseY()
            blocks.blocks.pop(collisionIndex)
            score += 1
        if ball.lives <= 0:
            return True
        if len(blocks.blocks) == 0:
            return False

        score_render = font.render(str(score), True, WHITE)
        window.blit(score_render, (100, 0))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    while True:
        is_game_over = gameloop()
        if is_game_over:
            gameover()
        else:
            gamewin()