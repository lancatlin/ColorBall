import pygame
import sys

from launcher import Launcher
from game_object import GameObject


class Main(GameObject):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))

    def welcome(self):
        self.screen.fill(self.bg)
        string = "ColorBall!"
        GameObject.txt(self.screen, string, 80, [255, 255, 255], (400, 300))

    def start(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.welcome()
            self.repaint(self.screen)

    def repaint(self, screen):
        pygame.display.flip()
        pygame.display.update()

root = Main()
root.start()