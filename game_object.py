import json

setting = json.load(open('setting.json', 'r'))


class GameObject:
    colors = setting["colors"]

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
