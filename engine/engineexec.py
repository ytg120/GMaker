def main(jsondata):
    import pygame
    global clock, name, width, height, filedata, gamedata, colorlist
    gamedata = {}
    filedata = jsondata

    # set the pygame vars.
    name = filedata['name']
    width = filedata['width']
    height = filedata['height']
    colorlist = {
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'orange': (255, 50, 0),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'purple': (100, 0, 255),
    'black': (0, 0, 0)
    }
    # pygame init
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption(name)
    displaysurf = pygame.display.set_mode((int(width), int(height)), 0, 32)

    # setting the bg color
    bg_color = filedata['bg']
    if 'color' in bg_color:
        color = colorlist[bg_color['color']]
    else:
        color = (255, 255, 255)

class Sprites:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        if self.type == 'image':
            self.data = gamedata[self.name]['text']
            self.imgrect = gamedata[self.name]['imgrect']
    def set_xy(self, x, y):
        pass
