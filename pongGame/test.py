import pygame, sys, os

pygame.init()
images = []
surface = pygame.display.set_mode((800, 800))
for file in os.listdir("assets/images"):
    if file.endswith(".png"):
        try:
            img = pygame.image.load(os.path.join("assets", "images", file))
            img = pygame.transform.scale(img, (100, 100))
            images.append(file)
        except:
            print("Error loading image: " + file)
            continue

while True:
    x, y = 0,0
    for image in images:
        surface.blit(pygame.image.load(os.path.join("assets", "images", image)), (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update()
