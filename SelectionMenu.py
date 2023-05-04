import pygame, sys

from Button import Button

import time 

class SelectionMenu:

    def __init__(self, screen, screenWidth, screenHeight, FPS, mixer, menu, font):
         
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.FPS = FPS
        self.mixer = mixer
        self.menu = menu
        self.Font = font

        self.boardSize = "4"
        self.boardSizeMax = 10

        self.BG = menu.BG
        self.LOBBY_MOUSE_POS = pygame.mouse.get_pos()

        self.initializeGUI()


    def initializeGUI(self):
        self.BOARD_TEXT = self.Font.get_title_font(smaller=2).render("Board size", True, "White")
        self.BOARD_RECT = self.BOARD_TEXT.get_rect(center=(self.screenWidth / 2, self.screenHeight / 3.9))

        self.BOARD_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 2.8), text_input= self.boardSize, font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")

        self.BACK_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 1.3), text_input="BACK", font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")
        self.PLAY_BUTTON = Button(image=None, pos=(self.screenWidth / 2, self.screenHeight / 1.1), text_input="PLAY", font=self.Font.get_normal_font(), base_color="White", hovering_color="Red")


    def displaySelection(self):

        while True:

            self.screen.blit(self.BG, (0, 0))
            self.LOBBY_MOUSE_POS = pygame.mouse.get_pos()
            self.LOBBY_MOUSE_BUTTONS = pygame.mouse.get_pressed()

            for button in [self.PLAY_BUTTON, self.BACK_BUTTON, self.BOARD_BUTTON]:
                button.changeColor(self.LOBBY_MOUSE_POS)
                button.update(self.screen)

            for selectObject in [(self.BOARD_TEXT, self.BOARD_RECT)]:
                self.screen.blit(selectObject[0], selectObject[1])

            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.BACK_BUTTON.checkForInput(self.LOBBY_MOUSE_POS):
                        return

                    if self.PLAY_BUTTON.checkForInput(self.LOBBY_MOUSE_POS):
                        pass
                        
                    if self.BOARD_BUTTON.checkForInput(self.LOBBY_MOUSE_POS):

                        self.boardSize = (str)((int)(self.boardSize) + 1)
                        if((int)(self.boardSize) > self.boardSizeMax):
                            self.boardSize = "1"

                        self.BOARD_BUTTON.changeText(self.boardSize)
                                 
                if event.type == self.mixer.SONG_END:
                    self.mixer.playMenuMusic()

            pygame.display.update()



