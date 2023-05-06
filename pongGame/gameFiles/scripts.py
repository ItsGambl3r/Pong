import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def drawDottedLine(surface, start, end, color = WHITE):
    x1, y1 = start
    x2, y2 = end
    segments = surface.get_height() / 10
    #print(f"Segments: {segments}")
    
    gap = (y2 - y1) / segments
    
    while y1 < y2:
        pygame.draw.circle(surface, color, (x1, y1), 2)
        y1 += gap