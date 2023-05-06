# Author: Gabriel Walker
# Student ID: gcw37
# FileName: text.py
# Purpose: Text class

from drawable import Drawable
import pygame, os

class Text(Drawable):
    #TODO: Add costum font /Applications/pongGame/Assets/Fonts/DJ5CTRIAL.ttf
    def __init__(self, message="Pygame", x=0, y=0, \
        color=(255, 255, 255), size = 90):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)


    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, \
        True, self.__color)
        surface.blit(self.__surface, self.getLoc())

    def get_rect(self):
        return self.__surface.get_rect()

    def setMessage(self, message):
    
        self.__message = message 