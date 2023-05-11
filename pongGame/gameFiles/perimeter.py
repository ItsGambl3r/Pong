from drawable import Drawable
import pygame

WHITE = (255, 255, 255)

class Perimeter(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
        self.__surface = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.__surface, self.__color, (self.getX(), self.getY(), self.__width, self.__height), 1)

    def shrink(self, width, height):
        self.__width -= width
        self.__height -= height

    def getRect(self):
        pass

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height