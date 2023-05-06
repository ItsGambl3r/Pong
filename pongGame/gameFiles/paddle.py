# Author: Gabriel Walker
# Student ID: gcw37
# FileName: paddle.py
# Purpose: Paddle class

from drawable import Drawable
import pygame

'''
Class: Paddle
'''

class Paddle(Drawable):

    def __init__(self, x, y, width, height, color, difficulty = 1):
        surface = pygame.display.get_surface()
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        self.__height = height
        self.__difficulty = difficulty


    def draw(self, surface):
        if self.__color == (0, 0, 0):
            pygame.draw.rect(surface, self.__color, self.getRect(), 1)
        pygame.draw.rect(surface, self.__color, self.getRect())

    def getRect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        return pygame.Rect(self.getX(), self.getY(), self.__width, self.__height) 
    
    def move(self):
        pass

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

    def setDifficulty(self, difficulty):
        self.__difficulty = difficulty
    
    def followMouse(self):
        mouseY= pygame.mouse.get_pos()[1]
        if mouseY - self.__height/2 <= 0:
            self.setY(0)
        elif mouseY + self.__height/2 >= pygame.display.get_surface().get_height():
            self.setY(pygame.display.get_surface().get_height() - self.__height)
        else:
            self.setY(mouseY - self.__height/2)

    def followObject(self, object):
        if self.__difficulty == 1:
            if object.getY() <= 0:
                self.setY(0)
            elif object.getY() + self.__height >= pygame.display.get_surface().get_height():
                self.setY(pygame.display.get_surface().get_height() - self.__height)
            else:
                self.setY(object.getY())
        elif self.__difficulty == 2:
            self.setY(object.getY() - self.__height/2)
    