from Board import Board
import pygame
import pygame, sys
import time 
import math
import operator
from threading import Thread
import TreeNode

class Game:

    def __init__(self, screen, screenWidth, screenHeight, FPS, mixer, menu, font, boardSize):

        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.gameBackgroundColor = "black"
        self.boardSeparatorColor = "gray"

        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.FPS = FPS

        self.boardSize = boardSize

        self.board = Board((int)(self.boardSize))

        self.Font = font

        self.menu = menu

        self.gameMixer = mixer

        self.sumProportion = (self.screenWidth + self.screenHeight) / 1000


    def dealWithGameEvents(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.gameMixer.SONG_END:
                self.gameMixer.switchMusicAndPlay()


    def initializeText(self):
        pass
        

    def initializeChangableText(self):
        pass


    def displayScores(self):
        pass


    def runGame(self):

        self.gameMixer.switchMusicAndPlay()

        self.screen.fill(self.gameBackgroundColor)

        clock = pygame.time.Clock() 

        root = TreeNode.createNeuralTree((int)(self.boardSize), 'o')
        
        while (not self.board.game_over):
            
            self.MENU_MOUSE_POS = pygame.mouse.get_pos()
            input = pygame.key.get_pressed() 
   
            self.board.draw(self.screen, self.screenWidth, self.screenHeight, self.gameBackgroundColor, self.Font)


            row, column = self.board.getRandomMove()
            self.board.placeToken(row, column)

            self.dealWithGameEvents()
                         
            pygame.display.update()
            time.sleep(0.5)

        self.board.draw(self.screen, self.screenWidth, self.screenHeight, self.gameBackgroundColor, self.Font)