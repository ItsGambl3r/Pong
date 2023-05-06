# Author: Gabriel Walker
# Student ID: gcw37
# FileName: main.py
# Purpose: Handle game loop

import pygame, sys, os, random
from scripts import drawDottedLine
from ball import Ball
from paddle import Paddle
from text import Text

pygame.init()
pygame.mixer.init()

screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
pygame.display.set_caption('Pong')

surface = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

background = pygame.image.load(os.path.join("assets", "images", "YuriDokiDoki.png"))
background = pygame.transform.scale(background, (screenWidth, screenHeight))
opacity = 0
background.set_alpha(opacity)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x, y = 0,0
gameObjects = []
halfScreenWidth, halfScreenHeight = screenWidth / 2, screenHeight / 2

ball = Ball(halfScreenWidth, halfScreenHeight, 10, WHITE)
playerPaddle = Paddle(screenWidth * (1 / 15), 0, 10, 100, WHITE)
computerPaddle = Paddle(screenWidth * (14 / 15), 0, 10, 100, WHITE)
gameObjects.append(ball)
gameObjects.append(playerPaddle)
gameObjects.append(computerPaddle)

 
fpsClock = pygame.time.Clock()
playerScore, computerScore = 0, 0
playerScoreText = Text(f"{playerScore}", screenWidth * (1 / 4), screenHeight * (1 / 12), WHITE, 90)
computerScoreText = Text(f"{computerScore}", screenWidth * (3 / 4), screenHeight * (1 / 12), WHITE, 90)
gameObjects.append(playerScoreText)
gameObjects.append(computerScoreText)
counter = 0
wallCollision = pygame.mixer.Sound(os.path.join("assets", "soundsEffects", "wallCollision.mp3"))
pongSound = pygame.mixer.Sound(os.path.join("assets", "soundsEffects", "pongSound.mp3"))
crash = pygame.mixer.Sound(os.path.join("assets", "soundsEffects", "crash.mp3"))
running = True
STARTDELAY = True

direction = [1, -1]
images = []
pygame.mixer.music.load(os.path.join("assets", "soundTracks", "doki.mp3"))
pygame.mixer.music.play(-1)

while running:
    isFullscreen = pygame.display.get_surface().get_flags() & pygame.FULLSCREEN
    screenWidth, screenHeight = surface.get_size()
    
    # TODO: Fix mouse visibility
    # Error after exiting fullscreen then re-entering full screen
    if isFullscreen:
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)

    if STARTDELAY:
        counter += 1
        if counter % 100 == 0:
            STARTDELAY = False

            ball.setVisible(True)
            ball.setXSpeed(random.choice(direction) * random.randint(2, 4))
            ball.setYSpeed(random.choice(direction) * random.randint(2, 4))
            counter = 0
    else:
        ball.move()
    
    #TODO: add surface attribute to drawable class 
    # iterate through gameObjects and draw them
    surface.fill((0, 0, 0))
    surface.blit(background, (0, 0))
    drawDottedLine(surface, (screenWidth / 2, 0), (screenWidth / 2, screenHeight))
    ball.draw(surface)
    playerScoreText.draw(surface)
    computerScoreText.draw(surface)
    playerPaddle.draw(surface)
    computerPaddle.draw(surface)
    playerPaddle.followMouse()
    computerPaddle.followObject(ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        
        if event.type == pygame.VIDEORESIZE:
            #TODO: Resizing screws ups objects not on screen
            ball.setLoc(event.w / 2, event.h / 2) #
            playerScoreText = Text(f"{playerScore}", event.w * (1 / 4), event.h * (1 / 12), WHITE, 90)
            computerScoreText = Text(f"{computerScore}", event.w * (3 / 4), event.h * (1 / 12), WHITE, 90)
            playerPaddle.setX(event.w * (1 / 15))
            computerPaddle.setX(event.w * (14 / 15))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if isFullscreen:
                    pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

    if ball.intersects(playerPaddle) or ball.intersects(computerPaddle):
        ball.setXSpeed(ball.getXSpeed()*-1.5)
        pongSound.play()

    if ball.getLoc()[0] <= ball.getRadius():
        ball.setLoc(halfScreenWidth, halfScreenHeight)
        crash.play()
        STARTDELAY = True
        computerScore += 1
        computerScoreText.setMessage(f"{computerScore}")
        opacity += 10

    if ball.getLoc()[0] >= screenWidth - ball.getRadius():
        ball.setLoc(halfScreenWidth, halfScreenHeight)
        crash.play()
        STARTDELAY = True
        playerScore += 1 
        playerScoreText.setMessage(f"{playerScore}")
        opacity += 10

    if ball.getLoc()[1] <= ball.getRadius() or ball.getLoc()[1] >= screenHeight - ball.getRadius():
        wallCollision.play()

    # TODO: add more conditions
    if playerScore == 2:
        computerPaddle.setHeight(300)
    if playerScore == 3:
        computerPaddle.setDifficulty(2)
    if computerScore >= 11:
        pygame.mixer.music.stop()
        
        for file in os.listdir("assets/images"):
                try:
                    img = pygame.image.load(os.path.join("assets", "images", file))
                    img = pygame.transform.scale(img, (random.randint(0, 500), random.randint(0, 500)))
                    images.append(file)
                except:
                    print(f"Error loading image: {file}")
                    continue

        for image in images:
            surface.blit(pygame.image.load(os.path.join("assets", "images", image)), (x, y))
            x = random.randint(0, screenWidth)
            y = random.randint(0, screenHeight)

    if playerScore >= 11:
        running = False
        sys.exit()

    if opacity >= 255:
        opacity = 255
    background.set_alpha(opacity)
    fpsClock.tick(144)

    pygame.display.update()

