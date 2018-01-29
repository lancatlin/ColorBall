import pygame
from pygame.locals import *

import game_object


class Wall(game_object.GameObject):
    w = 20
    h = 100
    def __init__(self, player, y):
        self.player = player
        self.x = player.x
        self.y = y

    def repaint(self, screen):
        y = [self.player.y + self.y + x*Wall.h for x in range(3)]
        for i in range(3):
            pygame.draw.rect(screen, Wall.colors[i], [self.x, y[i], Wall.w, Wall.h])

    def update(self):
        y = self.y + self.player.y
        if y < self.player.LOW:
            self.player.LOW = y
        elif y + 3 * Wall.h > self.player.HIGH:
            self.player.HIGH = y + 3*Wall.h

        if y > 800 or y < -3*Wall.h:
            self.kill()
    def kill(self):
        self.player.walls.remove(self)


class Player(game_object.GameObject):
    def __init__(self, master, mode='r'):
        self.master = master
        if mode == 'l':
            self.x = 20
            self.keys = {'up':K_w, 'dw':K_s}
        else:
            self.x = self.master.wh[0] - 20
            self.keys = {'up':K_UP, 'dw':K_DOWN}
        self.y = 0
        self.walls = []
        self.HIGH = 0
        self.LOW = 800

    def update(self):
        if self.iskey(self.keys['up']):
            self.y -= 6
        elif self.iskey(self.keys['dw']):
            self.y += 6

        self.HIGH, self.LOW = 0, 800
        for w in self.walls:
            w.update()

        if self.LOW > 0:
            y = self.LOW - 3 * Wall.h
            self.walls.append(Wall(self, y))
        elif self.HIGH < 800:
            y = self.HIGH
            self.walls.append((Wall(self, y)))


    def iskey(self, key):
        return self.master.iskey(key)

    def repait(self, screen):
        for w in self.walls:
            w.repaint(screen)