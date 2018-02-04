import pygame
from pygame.locals import *
import json

import game_object


setting = json.load(open('data/setting.json', 'r'))

class Wall(game_object.GameObject):
    '''兩邊牆壁物件，聽令於Player'''
    w = setting['w']
    h = setting['h']

    def __init__(self, player, y):
        self.player = player
        self.x = player.x
        self.y = y
        self.color = []

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
    '''玩家物件，操縱兩個牆壁，並負責其他程式與牆壁的中介
    玩家物件本身沒有畫面'''
    def __init__(self, master):
        self.master = master
        self.walls = []
        self.HIGH = 0
        self.LOW = 800
        self.font = pygame.font.Font("data/font/freesansbold.ttf", 45)
        self.keys = {}
        self.x = 0
        self.text_x = 0
        self.name = ''
        self.score = 0

    def update(self):
        change = 0
        if self.iskey(self.keys['up']):
            change = -setting['speed']
        elif self.iskey(self.keys['dw']):
            change = setting['speed']

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

        if self.score < 0:
            self.score = 0

    def iskey(self, key):
        return self.master.iskey(key)

    def repaint(self, screen):
        string = self.name+':'+str(self.score)
        text_color = self.color
        text = self.font.render(string, True, text_color)
        screen.blit(text, (self.text_x,50))
        for w in self.walls:
            w.repaint(screen)

    def get_color(self, y):
        for w in self.walls:
            result = w.get_color(y)
            if result is not None:
                return result


class P1(Player):
    def __init__(self, master):
        super().__init__(master)
        self.name = "P1"
        self.x = self.master.wh[0]-Wall.w
        self.keys = {'up': K_UP, 'dw': K_DOWN}
        self.text_x = 650
        self.color = self.colors[0]


class P2(Player):
    def __init__(self, master):
        super().__init__(master)
        self.name = "P2"
        self.x = 0
        self.keys = {'up': K_w, 'dw': K_s}
        self.text_x = 50
        self.color = self.colors[2]
