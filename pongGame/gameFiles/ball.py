# Author: Gabriel Walker
# Student ID: gcw37
# FileName: ball.py
# Purpose: Ball class

from drawable import Drawable
import pygame

'''
Class: Ball
modified from template
'''

class Ball(Drawable):
    def __init__(self, x = 0, y = 0, radius = 10, color = (0, 0, 0)):
       super().__init__(x, y)
       self.__color = color
       self.__radius = radius
       self.__speedX = 1
       self.__speedY = 1

    def draw(self):
        if self.isVisible():
            pygame.draw.circle(self.getSurface(), self.__color, self.getLoc(), self.__radius)
        
    def setYSpeed(self, speedY):
        self.__speedY = speedY

    def getYSpeed(self):
        return self.__speedY
    
    def setXSpeed(self, speedX):
        self.__speedX = speedX

    def getXSpeed(self):
        return self.__speedX
    
    def getRadius(self):
        return self.__radius

    def move(self, dx = 1, dy = 1):
        currentX, currentY = self.getLoc()
        newX = currentX + self.__speedX
        newY = currentY + self.__speedY
        self.setX(newX)
        self.setY(newY)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__speedX *= -1


        if newY <= self.__radius or newY + self.__radius >= height:
            self.__speedY *= -1
    
    def getRect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius) 