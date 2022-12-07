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
        self.pacmanX_change = 0
        self.pacmanY_change = 0
        self.pacmanDir = self.pacmanRight
        self.screen.blit(self.pacmanDir, (self.pacmanX, self.pacmanY))
        self.pacman1X = random.randint(0, 930)
        self.pacman1Y = random.randint(0, 730)
        self.pacman1X_change = 0
        self.pacman1Y_change = 0
        self.pacman1Dir = self.pacmanRight
        self.screen.blit(self.pacman1Dir, (self.pacman1X, self.pacman1Y))
        self.pacman2X = random.randint(0, 930)
        self.pacman2Y = random.randint(0, 730)
        self.pacman2X_change = 0
        self.pacman2Y_change = 0
        self.pacman2Dir = self.pacmanRight
        self.screen.blit(self.pacman2Dir, (self.pacman2X, self.pacman2Y))
        self.pacman3X = random.randint(0, 930)
        self.pacman3Y = random.randint(0, 730)
        self.pacman3X_change = 0
        self.pacman3Y_change = 0
        self.pacman3Dir = self.pacmanRight
        self.screen.blit(self.pacman3Dir, (self.pacman3X, self.pacman3Y))
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
                        self.pacmanX_change = -0.25
                        self.pacmanDir = self.pacmanLeft
                        self.pacman1X_change = 0.25
                        self.pacman1Dir = self.pacmanRight
                        self.pacman2Y_change = 0.25
                        self.pacman2Dir = self.pacmanDown
                        self.pacman3Y_change = -0.25
                        self.pacman3Dir = self.pacmanUp
                    if event.key == pygame.K_RIGHT:
                        self.geistX_change = 0.3
                        self.geistDir = self.geistRight
                        self.pacmanX_change = 0.25
                        self.pacmanDir = self.pacmanRight
                        self.pacman1X_change = -0.25
                        self.pacman1Dir = self.pacmanLeft
                        self.pacman2Y_change = -0.25
                        self.pacman2Dir = self.pacmanUp
                        self.pacman3Y_change = 0.25
                        self.pacman3Dir = self.pacmanDown
                    if event.key == pygame.K_DOWN:
                        self.geistY_change = 0.3
                        self.geistDir = self.geistDown
                        self.pacmanY_change = 0.25
                        self.pacmanDir = self.pacmanDown
                        self.pacman1Y_change = -0.25
                        self.pacman1Dir = self.pacmanUp
                        self.pacman2X_change = 0.25
                        self.pacman2Dir = self.pacmanRight
                        self.pacman3X_change = -0.25
                        self.pacman3Dir = self.pacmanLeft
                    if event.key == pygame.K_UP:
                        self.geistY_change = -0.3
                        self.geistDir = self.geistUp
                        self.pacmanY_change = -0.25
                        self.pacmanDir = self.pacmanUp
                        self.pacman1Y_change = 0.25
                        self.pacman1Dir = self.pacmanDown
                        self.pacman2X_change = -0.25
                        self.pacman2Dir = self.pacmanLeft
                        self.pacman3X_change = 0.25
                        self.pacman3Dir = self.pacmanRight
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.geistX_change = 0
                        self.pacmanX_change = 0
                        self.pacman1X_change = 0
                        self.pacman2X_change = 0
                        self.pacman3X_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        self.geistY_change = 0
                        self.pacmanY_change = 0
                        self.pacman1Y_change = 0
                        self.pacman2Y_change = 0
                        self.pacman3Y_change = 0

            self.geistX += self.geistX_change
            self.geistY += self.geistY_change

            self.pacmanX += self.pacmanX_change
            self.pacmanY += self.pacmanY_change

            self.pacman1X += self.pacman1X_change
            self.pacman1Y += self.pacman1Y_change

            self.pacman2X += self.pacman2X_change
            self.pacman2Y += self.pacman2Y_change

            self.pacman3X += self.pacman3X_change
            self.pacman3Y += self.pacman3Y_change

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
                self.pacmanX = 0
            if self.pacmanX >= 930:
                self.pacmanX = 930
            if self.pacmanY <= 0:
                self.pacmanY = 0
            if self.pacmanY >= 720:
                self.pacmanY = 720
            
            if self.pacman1X <= 0:
                self.pacman1X = 0
            if self.pacman1X >= 930:
                self.pacman1X = 930
            if self.pacman1Y <= 0:
                self.pacman1Y = 0
            if self.pacman1Y >= 720:
                self.pacman1Y = 720

            if self.pacman2X <= 0:
                self.pacman2X = 0
            if self.pacman2X >= 930:
                self.pacman2X = 930
            if self.pacman2Y <= 0:
                self.pacman2Y = 0
            if self.pacman2Y >= 720:
                self.pacman2Y = 720

            if self.pacman3X <= 0:
                self.pacman3X = 0
            if self.pacman3X >= 930:
                self.pacman3X = 930
            if self.pacman3Y <= 0:
                self.pacman3Y = 0
            if self.pacman3Y >= 720:
                self.pacman3Y = 720
 
            self.geistMove(self.geistX, self.geistY)
            self.pacMove(self.pacmanX, self.pacmanY)
            self.pac1Move(self.pacman1X, self.pacman1Y)
            self.pac2Move(self.pacman2X, self.pacman2Y)
            self.pac3Move(self.pacman3X, self.pacman3Y)
            pygame.display.update()

    def geistMove(self, x, y):
        self.screen.blit(self.geistDir, (x, y))

    def pacMove(self, x, y):
        self.screen.blit(self.pacmanDir, (x, y))

    def pac1Move(self, x, y):
        self.screen.blit(self.pacman1Dir, (x, y))
    
    def pac2Move(self, x, y):
        self.screen.blit(self.pacman2Dir, (x, y))
    
    def pac3Move(self, x, y):
        self.screen.blit(self.pacman3Dir, (x, y))
     
a = Characters()