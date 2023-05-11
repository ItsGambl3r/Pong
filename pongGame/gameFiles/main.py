# Author: Gabriel Walker
# Student ID: gcw37
# FileName: main.py
# Purpose: Handle game loop

import pygame, sys, os, random, getpass
from scripts import drawDottedLine
from ball import Ball
from paddle import Paddle
from text import Text
from perimeter import Perimeter

pygame.init()
pygame.mixer.init()

screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
pygame.display.set_caption('Classic Pong')

surface = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)

# This should work for both windows and mac
backgroundPath = os.path.join("pongGame", "Assets", "images", "YuriDokiDoki.png")
background = pygame.image.load(backgroundPath)
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

perimeter = Perimeter(0, 0, screenWidth, screenHeight, WHITE)
gameObjects.append(perimeter)

try: userID = getpass.getuser()
except: userID = "Player"

fpsClock = pygame.time.Clock()
playerScore, computerScore = 0, 0
playerScoreText = Text(f"{userID} {playerScore}", screenWidth * (1 / 4), screenHeight * (1 / 12), WHITE, 50)
computerScoreText = Text(f"Player2: {computerScore}", screenWidth * (3 / 4), screenHeight * (1 / 12), WHITE, 50)

for gameObject in gameObjects:
    if isinstance(gameObject, Text):
        gameObject.updateLoc()

wallCollision = pygame.mixer.Sound(os.path.join("pongGame", "Assets", "soundsEffects", "wallCollision.mp3"))
pongSound = pygame.mixer.Sound(os.path.join("pongGame", "Assets","soundsEffects", "pongSound.mp3"))
crash = pygame.mixer.Sound(os.path.join("pongGame", "Assets","soundsEffects", "crash.mp3"))
running = True
STARTDELAY = True
direction = [1, -1]
images = []
pygame.mixer.music.load(os.path.join("pongGame", "Assets", "soundTracks", "doki.mp3"))
pygame.mixer.music.play(-1)

gameObjects.append(playerScoreText)
gameObjects.append(computerScoreText)

if __name__ == "__main__":
    counter = 0
    playerScoreText.updateLoc()
    computerScoreText.updateLoc()

    while running:
        isFullscreen = pygame.display.get_surface().get_flags() and pygame.FULLSCREEN
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
        surface.fill((BLACK))
        surface.blit(background, (0, 0))
        drawDottedLine(surface, (screenWidth / 2, 0), (screenWidth / 2, screenHeight))
        for gameObject in gameObjects:
            gameObject.draw()

        playerPaddle.followMouse()
        computerPaddle.followObject(ball)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:
                #TODO: Resizing screws ups objects not on screen
                ball.setLoc(event.w / 2, event.h / 2) #
                playerScoreText.setLoc(event.w * (1 / 4), event.h * (1 / 12))
                computerScoreText.setLoc(event.w * (3 / 4), event.h * (1 / 12))
                playerScoreText.updateLoc()
                computerScoreText.updateLoc()
                playerPaddle.setX(event.w * (1 / 15))
                computerPaddle.setX(event.w * (14 / 15))


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if isFullscreen:
                        pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

        if ball.intersects(playerPaddle) or ball.intersects(computerPaddle):
            ball.setXSpeed(ball.getXSpeed()*-1.25)
            pongSound.play()

        if ball.getLoc()[0] <= ball.getRadius():
            ball.setLoc(halfScreenWidth, halfScreenHeight)
            crash.play()
            STARTDELAY = True
            computerScore += 1
            computerScoreText.updateMessage(f"Player2: {computerScore}")
            opacity += 10

        if ball.getLoc()[0] >= screenWidth - ball.getRadius():
            ball.setLoc(halfScreenWidth, halfScreenHeight)
            crash.play()
            STARTDELAY = True
            playerScore += 1
            playerScoreText.updateMessage(f"{userID}: {playerScore}")
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
            
            for file in os.listdir(os.path.join("pongGame", "Assets", "images")):
                    try:
                        img = pygame.image.load(os.path.join("pongGame", "Assets", "images", file))
                        img = pygame.transform.scale(img, (random.randint(0, 500), random.randint(0, 500)))
                        images.append(file)
                    except:
                        print(f"Error loading image: {file}")
                        continue

            for image in images:
                surface.blit(pygame.image.load(os.path.join("pongGame", "Assets", "images", image)), (x, y))
                x = random.randint(0, screenWidth)
                y = random.randint(0, screenHeight)

        if playerScore >= 11:
            running = False
            sys.exit()

        if opacity >= 255:
            opacity = 255
        background.set_alpha(opacity)
        fpsClock.tick(244)

        pygame.display.update()

    pygame.quit()
