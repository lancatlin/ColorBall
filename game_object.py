import pygame


class GameObject:
    colors = [
        (255, 80, 40),
        (200, 255, 100),
        (80, 190, 255)
    ]
    bg = [20, 50, 80]

    def repaint(self, screen):
        pass

    def update(self):
        pass

    def kill(self):
        pass

    @staticmethod
    def txt(screen, string, big, color, xy):
        f1 = pygame.font.Font('freesansbold.ttf', big)
        fc1 = f1.render(string, True, color)
        fr1 = fc1.get_rect()
        fr1.center = xy
        screen.blit(fc1, fr1)