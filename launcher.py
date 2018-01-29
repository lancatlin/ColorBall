import pygame
import random
import sys

import ball
import wall


class Launcher:
    def __init__(self):
        pygame.init()
        self.wh = (800, 800)
        self.screen = pygame.display.set_mode(self.wh)
        self.surface = pygame.Surface(self.wh)
        self.clock = pygame.time.Clock()
        self.last_time = 0
        #物件設定
        self.P1 = wall.Player(self, 'r')
        self.P2 = None
        self.balls = []

    def repaint(self):
        self.screen.fill([20, 50, 80])
        for ball in self.balls:
            ball.repaint(self.screen)
        self.P1.repait(self.screen)

        pygame.display.flip()
        pygame.display.update()

    def update(self):
        for b in self.balls:
            b.update()
        self.P1.update()

    def begin(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.repaint()
            self.creat_ball()
            self.clock.tick(30)

    def creat_ball(self):
        if pygame.time.get_ticks() - self.last_time > 1000:
            self.last_time = pygame.time.get_ticks()
            self.balls.append(ball.Ball(self))

    def iskey(self, key):
        allkey = pygame.key.get_pressed()
        return allkey[key]


root = Launcher()
root.begin()
