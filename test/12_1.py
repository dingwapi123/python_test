# 开发时间：2022/7/7 15:37
import pygame
import sys


class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("bluesky")


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill((5, 39, 175))


if __name__ == '__main__':
    bluesky = BlueSky()
    bluesky.run_game()
