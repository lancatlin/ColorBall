import pygame
import random

from game_object import GameObject


class Ball(GameObject):
    def __init__(self, master):
        self.master = master
        #mode 會是r或者l
        mode = random.choice(['r', 'l'])
        if mode == 'l':
            self.x = 50
            self.change = 6
        else:
            self.x = self.master.wh[0] - 50
            self.change = -6
        self.y = -20
        #半徑
        self.r = 20
        self.color = random.choice(Ball.colors)
        self.live = True

    def update(self):
        self.y += 1
        self.x += self.change
        if self.x > (self.master.wh[0] - 2):
            self.kill()
        elif self.x < 5:
            self.kill()

    def kill(self):
        self.master.balls.remove(self)

    def repaint(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.r)