import pygame
import sys
import json

import ball
import wall
from game_object import GameObject

setting = json.load(open('setting.json', 'r'))

class Launcher:
    def __init__(self):
        pygame.init()
        self.wh = (800, 800)
        self.screen = pygame.display.set_mode(self.wh)
        pygame.display.set_caption("ColorBall 彩色碰碰球")
        self.surface = pygame.Surface(self.wh)
        self.clock = pygame.time.Clock()
        self.time = setting['time']
        self.last_time = 0
        #物件設定
        self.P1 = wall.P1(self)
        self.P2 = wall.P2(self)
        self.balls = []
        self.font = pygame.font.Font("freesansbold.ttf", 64)

    def repaint(self):
        self.screen.fill([20, 50, 80])
        for ball in self.balls:
            ball.repaint(self.screen)
        self.P1.repaint(self.screen)
        self.P2.repaint(self.screen)
        string = "Time:"+str(self.time - int(pygame.time.get_ticks()/1000))
        text = self.font.render(string, True, [255,255,255])
        self.screen.blit(text, (250,30))

        pygame.display.flip()
        pygame.display.update()

    def end(self):
        self.screen.fill([20, 50, 80])
        self.P1.repaint(self.screen)
        self.P2.repaint(self.screen)
        if self.P1.score > self.P2.score:
            winner = "P1 Win"
            color = self.P1.color
        elif self.P2.score > self.P1.score:
            winner = "P2 win"
            color = self.P2.color
        else:
            winner = "Tie"
            color = GameObject.colors[1]
        font = pygame.font.Font('freesansbold.ttf', 90)
        text = font.render(winner, True, color)
        rect = text.get_rect()
        rect.center = (400, 400)
        self.screen.blit(text, rect)
        pygame.display.flip()
        pygame.display.update()

    def update(self):
        for b in self.balls:
            b.update()
        self.P1.update()
        self.P2.update()

    def begin(self):
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.time-(pygame.time.get_ticks()/1000) <= 0:
                self.end()
            else:
                self.update()
                self.repaint()
                self.creat_ball()
            self.clock.tick(30)

    def creat_ball(self):
        if pygame.time.get_ticks() - self.last_time > 1500:
            self.last_time = pygame.time.get_ticks()
            self.balls.append(ball.Ball(self))

    def iskey(self, key):
        allkey = pygame.key.get_pressed()
        return allkey[key]


root = Launcher()
root.begin()
