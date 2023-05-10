# Author: Gabriel Walker
# Student ID: gcw37
# FileName: text.py
# Purpose: Text class

from drawable import Drawable
import pygame, os

'''
Class: Text
modified from template
'''

pygame.font.init() # not sure if this is needed

class Text(Drawable):
    def __init__(self, message="Pygame", x=0, y=0, \
        color=(255, 255, 255), size = 20):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font(os.path.join("pongGame", "Assets", "fonts", "RifficFree-Bold.ttf"), size)
        
    def getWidht(self):
        return self.__fontObj.size(self.__message)[0]

    
    def updateLoc(self):
        self.setX(self.getX() - self.getWidht() / 2)

    def updateMessage(self, message):
        self.__message = message

    def draw(self):
        self.__surface = self.__fontObj.render(self.__message, \
        True, self.__color)
        surface
        pygame.display.get_surface().blit(self.__surface, self.getLoc()) 

    def getRect(self):
        return self.__surface.getRect()
