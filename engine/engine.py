import os
import json
import pygame
import ctypes 
from pygame.locals import *
import sys
import time
import threading
import random

def get_resource_path(filename):
    if getattr(sys, 'frozen', False):

        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, filename)

json_path = get_resource_path('game.json')
with open(json_path, 'r', encoding='utf-8') as f:
    try:
        filedata = json.load(f)
    except:
        ctypes.windll.user32.MessageBoxW(0, "No game.json file found", "Error", 0)

# set the pygame vars.
clock = pygame.time.Clock()
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

pygame.init()
pygame.display.set_caption(name)
displaysurf = pygame.display.set_mode((int(width), int(height)), 0, 32)

i = filedata['bg']
if 'color' in i:
    global color
    color = i['color']

gui = pygame.font.Font(get_resource_path(os.path.join('data', 'Font.ttf')), 70)

texts = {}
images = {}

keys = pygame.key.get_pressed()
# position 0 = left, position 1 = center

def time(num):
    time.sleep(num)

def hide():
    pygame.sprite.Sprite.kill()


# data loading
for sprite in filedata['sprites'].values():
    # set the xy pos
    global spritex
    global spritey
    spritex = sprite['xloc']
    spritey = sprite['yloc']
    if sprite['type'] == 'text':
        text = gui.render(sprite['data'], True, colorlist['black'])
        textrect = text.get_rect()
        pos = int(sprite['position'])
        if pos == 0:
            textrect.topleft = ((width/10)*sprite['xloc'], (height/10)*sprite['yloc'])
        else:
            textrect.center = ((width/10)*sprite['xloc'], (height/10)*sprite['yloc'])
        texts[sprite['name']] = {'text': text, 'textrect': textrect}

    elif sprite['type'] == 'image':
        img = pygame.image.load(get_resource_path(os.path.join('data', str(sprite['data'])))).convert_alpha()
        imgrect = img.get_rect()
        imgrect.center = ((width/10)*sprite['xloc'], (height/10)*sprite['yloc'])
        images[sprite['name']] = {'img': img, 'imgrect': imgrect}
    try:
        exec(sprite['code'])
    except:
        print('exec err')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    displaysurf.fill(colorlist[color])
    for sprite in texts.values():
        displaysurf.blit(sprite['text'], sprite['textrect'])
    for sprite in images.values():
        displaysurf.blit(sprite['img'], sprite['imgrect'])


    pygame.display.update() 