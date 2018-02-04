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