import json

setting = json.load(open('data/setting.json', 'r'))


class GameObject:
    colors = setting["colors"]
    bg = [20, 60, 80]

    def repaint(self, screen):
        pass

    def update(self):
        pass

    def kill(self):
        pass

