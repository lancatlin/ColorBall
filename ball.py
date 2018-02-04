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
        self.y_change = random.uniform(0.5, 1.5)

    def update(self):
        self.y += self.y_change
        self.x += self.change
        c = None
        p = None
        if self.x > (self.master.wh[0] - 20 - self.r):
            p = self.master.P1
            c = p.get_color(self.y)
        elif self.x < 20 + self.r:
            p = self.master.P2
            c = p.get_color(self.y)
        elif self.y > 800 + self.r:
            print("Die")
            self.kill()

        if c:
            if c == self.color:
                self.change *= -1.1
                self.y_change *= 1.1
                self.r += 1
                p.score += 1
            else:
                p.score -= 1
                self.kill()

    def kill(self):
        self.master.balls.remove(self)

    def repaint(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.x), int(self.y)], self.r)