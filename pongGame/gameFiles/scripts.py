# Author: Gabriel Walker
# Student ID: gcw37
# FileName: scripts.py
# Purpose: module for scripts

import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DIRECTION = [1, -1]

def drawDottedLine(surface, start, end, color = WHITE):
    x1, y1 = start
    x2, y2 = end
    segments = surface.get_height() / 10
    
    gap = (y2 - y1) / segments
    
    while y1 < y2:
        pygame.draw.circle(surface, color, (x1, y1), 2)
        y1 += gap

def delay(startDelay: bool, gameObject: object):
    counter = 0
    if startDelay:
        while counter < 10:
            counter += 1
        startDelay = False
        gameObject.setVisible(True)
        gameObject.setXSpeed(random.choice(DIRECTION) * 4)
        gameObject.setYSpeed(random.choice(DIRECTION) * 4)
        #gameObject.setXSpeed(random.choice(DIRECTION) * random.randint(2, 4))
        #gameObject.setYSpeed(random.choice(DIRECTION) * random.randint(2, 4))
    else:
        gameObject.move()