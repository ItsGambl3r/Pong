# Author: Gabriel Walker
# Student ID: gcw37
# FileName: main.py
# Purpose: Parent class for all drawable objects

from abc import ABC, abstractmethod
import pygame

'''
Class: Drawable
modified from template
'''

class Drawable(ABC):
    def __init__(self, x = 0,y = 0, visible = True):
        self.__surface = pygame.display.get_surface()
        self.__x = x
        self.__y = y
        self.__visible = visible
    
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def getRect(self):
        pass

    def getLoc(self):
        return (self.__x, self.__y)
    
    def setLoc(self, x, y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
        
    def isVisible(self):
        return self.__visible
    
    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False 
            
    def intersects(self, other):
        rect1 = self.getRect()
        rect2 = other.getRect()
        if (rect1.x < rect2.x + rect2.width) and \
        (rect1.x + rect1.width > rect2.x) and \
        (rect1.y < rect2.y + rect2.height) and \
        (rect1.height + rect1.y > rect2.y):
            return True
        return False
    

