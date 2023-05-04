from Button import Button
from Mixer import Mixer
from SelectionMenu import SelectionMenu
from Font import Font

import pygame
import pygame, sys
from pygame._sdl2.video import Window

import time 
import math
import asyncio
import os
import re

class Menu:

    def __init__(self):

        pygame.init()

        self.GAME_TITLE = "Circles and Crosses"
        self.maxResolutionObject = pygame.display.Info()

        self.maxResolutionWidth = self.maxResolutionObject.current_w
        self.maxResolutionHeight = self.maxResolutionObject.current_h

        self.screenWidth = self.maxResolutionWidth
        self.screenHeight = self.maxResolutionHeight

        self.initialVolume = 0.5
        self.mixer = Mixer(self.initialVolume)

        self.FPS = 60

        self.resolution_init()


    def resolution_init(self, firstTime = True):

        pygame.display.quit()

        self.setGameWindowCenter((self.maxResolutionWidth - self.screenWidth) / 2, (self.maxResolutionHeight - self.screenHeight) / 2)

        pygame.display.init()

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight) ) 

        pygame.display.set_caption(self.GAME_TITLE)

        self.BG = pygame.image.load("assets/picture/MenuBackground.jpg")
        self.BG = pygame.transform.scale(self.BG, (self.screenWidth, self.screenHeight))

        self.Font = Font(self.screenWidth, self.screenHeight)

        self.MENU_TEXT = self.Font.get_title_font().render(self.GAME_TITLE, True, "Yellow")
        self.MENU_RECT = self.MENU_TEXT.get_rect(center=(self.screenWidth / 2, self.screenHeight / 7.2))

        self.NEURAL_NETWORK_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 3.0), text_input="NEURAL NETWORK", font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")
        self.QLEARNING_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 2.0), text_input="QLERNING", font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")
        self.HEURISTIC_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 1.5), text_input="HEURISTIC", font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")
        self.QUIT_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 1.2), text_input="QUIT", font=self.Font.get_normal_font(), base_color="Green", hovering_color="Red")

        self.MENU_MOUSE_POS = pygame.mouse.get_pos()

        self.displayMainMenu(firstTime = firstTime)


    def setGameWindowCenter(self, x, y):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

    def goToSelection(self):
        selectionMenu = SelectionMenu(self.screen, self.screenWidth, self.screenHeight, self.FPS, self.mixer, self, self.Font)
        selectionMenu.displaySelection()

    def qLearning(self):
        self.goToSelection()

    def neuralNetwork(self):
        self.goToSelection()

    def heuristic(self):
        self.goToSelection()
         

    def displayMainMenu(self, firstTime = False):

        if firstTime == True:
           self.mixer.playMenuMusic()
        
        while True:

            self.screen.blit(self.BG, (0, 0))
            self.MENU_MOUSE_POS = pygame.mouse.get_pos()

            self.screen.blit(self.MENU_TEXT, self.MENU_RECT)

            for button in [self.NEURAL_NETWORK_BUTTON, self.QLEARNING_BUTTON, self.HEURISTIC_BUTTON, self.QUIT_BUTTON]:
                button.changeColor(self.MENU_MOUSE_POS)
                button.update(self.screen)
        
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.NEURAL_NETWORK_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        self.neuralNetwork()

                    if self.QLEARNING_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        self.qLearning()

                    if self.HEURISTIC_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        self.heuristic()

                    if self.QUIT_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

                if event.type == self.mixer.SONG_END:
                    self.mixer.playMenuMusic()

            pygame.display.update()


    








