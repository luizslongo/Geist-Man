import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("GEIST-MAN")
        self.icon = pygame.image.load("displayIcon.png")
        pygame.display.set_icon(self.icon)
        self.screen.fill((0, 0, 0))

        pygame.display.update()
        self.loadSprites()

    def loadSprites(self):
        self.geistLeft = pygame.image.load("geistLeft.png")
        self.geistRight = pygame.image.load("geistRight.png")
        self.geistDown = pygame.image.load("geistDown.png")
        self.geistUp = pygame.image.load("geistUp.png") 
        self.pacmanLeft = pygame.image.load("pacmanLeft.png")
        self.pacmanRight = pygame.image.load("pacmanRight.png")
        self.pacmanDown = pygame.image.load("pacmanDown.png")
        self.pacmanUp = pygame.image.load("pacmanUp.png") 

class Characters(Game):
    def __init__(self):
        super().__init__()
        self.geistX = 460
        self.geistY = 650
        self.geistX_change = 0
        self.geistY_change = 0
        self.geistDir = self.geistRight
        self.screen.blit(self.geistDir, (self.geistX, self.geistY))
        self.pacmanX = random.randint(0, 930)
        self.pacmanY = random.randint(0, 730)
        self.pacmanX_change = 0.25
        self.pacmanY_change = 0
        self.pacmanDir = self.pacmanRight
        self.screen.blit(self.pacmanDir, (self.pacmanX, self.pacmanY))
        pygame.display.update()  
        self.gameplay()
        
    def gameplay(self):
        self.isRunning = True
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.geistX_change = -0.3
                        self.geistDir = self.geistLeft
                    if event.key == pygame.K_RIGHT:
                        self.geistX_change = 0.3
                        self.geistDir = self.geistRight
                    if event.key == pygame.K_DOWN:
                        self.geistY_change = 0.3
                        self.geistDir = self.geistDown
                    if event.key == pygame.K_UP:
                        self.geistY_change = -0.3
                        self.geistDir = self.geistUp
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.geistX_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.geistY_change = 0

            self.geistX += self.geistX_change
            self.geistY += self.geistY_change

            self.pacmanX += self.pacmanX_change
            self.pacmanY += self.pacmanY_change

            #Geist border boundries
            if self.geistX <= 0:
                self.geistX = 0
            if self.geistX >= 930:
                self.geistX = 930
            if self.geistY <= 0:
                self.geistY = 0
            if self.geistY >= 720:
                self.geistY = 720

            #Pacman border boundries
            if self.pacmanX <= 0:
                self.pacmanX_change = 0.25
                self.pacmanDir = self.pacmanRight
            if self.pacmanX >= 930:
                self.pacmanX_change = -0.25
                self.pacmanDir = self.pacmanLeft
            if self.pacmanY <= 0:
                self.pacmanY_change = 0.25
                self.pacmanDir = self.pacmanDown
            if self.pacmanY >= 720:
                self.pacmanY_change = -0.25
                self.pacmanDir = self.pacmanUp
 
            self.geistMove(self.geistX, self.geistY)
            self.pacMove(self.pacmanX, self.pacmanY)
            pygame.display.update()

    def geistMove(self, x, y):
        self.screen.blit(self.geistDir, (x, y))

    def pacMove(self, x, y):
        self.screen.blit(self.pacmanDir, (x, y))
     
a = Characters()