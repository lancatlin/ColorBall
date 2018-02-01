import pygame
from pygame.locals import *

import game_object


class Wall(game_object.GameObject):
    '''兩邊牆壁物件，聽令於Player'''
    w = 30
    h = 100

    def __init__(self, player, y):
        self.player = player
        self.x = player.x
        self.y = y

    def repaint(self, screen):
        y = [self.y + x*Wall.h for x in range(3)]
        for i in range(3):
            pygame.draw.rect(screen, Wall.colors[i],
                             [self.x, y[i], Wall.w, Wall.h])

    def update(self, change=0):
        self.y += change
        y = self.y
        if y < self.player.LOW:
            self.player.LOW = y
        elif y + 3 * Wall.h > self.player.HIGH:
            self.player.HIGH = y + 3*Wall.h

    def kill(self):
        y = self.y
        if y > 800 or y < -3*Wall.h:
            self.player.walls.remove(self)

    def get_color(self, y):
        y_range = [self.y + x*Wall.h for x in range(4)]
        for i in range(3):
            if y_range[i] < y < y_range[i+1]:
                return Wall.colors[i]
        else:
            return None


class Player(game_object.GameObject):
    def __init__(self, master, mode='r'):
        self.master = master
        if mode == 'l':
            self.x = 0
            self.keys = {'up': K_w, 'dw': K_s}
        else:
            self.x = self.master.wh[0]-Wall.w
            self.keys = {'up': K_UP, 'dw': K_DOWN}
        self.walls = []
        self.HIGH = 0
        self.LOW = 800

    def update(self):
        change = 0
        if self.iskey(self.keys['up']):
            change = -6
        elif self.iskey(self.keys['dw']):
            change = 6

        for w in self.walls:
            w.kill()

        self.HIGH, self.LOW = 400, 400
        for w in self.walls:
            w.update(change)

        if self.LOW > 0:
            y = self.LOW - 3 * Wall.h
            self.walls.append(Wall(self, y))
        elif self.HIGH < 800:
            y = self.HIGH
            self.walls.append((Wall(self, y)))

    def iskey(self, key):
        return self.master.iskey(key)

    def repaint(self, screen):
        for w in self.walls:
            w.repaint(screen)

    def get_color(self, y):
        for w in self.walls:
            result = w.get_color(y)
            if result is not None:
                return result
