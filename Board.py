import random
import pygame

class Board:

    def __init__(self, size, who_first='o'):

        self.size = size
        self.who_moves = who_first
        self.game_over = False
        self.wins = None
        self.board = []

        for _ in range(self.size):

            self.board.append(['_' for _ in range(self.size)])


    def placeToken(self, row, column):

        self.board[row][column] = self.who_moves
        self.game_over = self.check_game_over(row,column)

        if self.who_moves == 'o':
            self.who_moves = 'x'
        else:
            self.who_moves = 'o'


    def possibleMoves(self):

        possible_moves = []

        for row in range(self.size):
            for column in range(self.size):

                if self.board[row][column] == '_':
                    move = row,column
                    possible_moves.append(move)

        return possible_moves


    def getRandomMove(self):

        possibleMoves = self.possibleMoves()

        randomMoveSelected = random.randint(0, len(possibleMoves) - 1)

        return possibleMoves[randomMoveSelected]



    def check_game_over(self, row, column):

        diagonal1 = []
        diagonal2 = []

        if self.board[row][:].count(self.who_moves) == self.size:
            self.wins = self.who_moves
            return True

        if self.board[:][column].count(self.who_moves) == self.size:
            self.wins = self.who_moves
            return True

        for n in range(self.size):
            diagonal1.append(self.board[n][n])
            diagonal2.append(self.board[self.size-1-n][n])

        if diagonal1.count(self.who_moves) == self.size or diagonal2.count(self.who_moves) == self.size:
            self.wins = self.who_moves
            return True

        if len(self.possibleMoves()) == 0:
            return True

        return False


    def draw(self, screen, screenWidth, screenHeight, background_color, font):

        screen.fill(background_color)
        self.sumProportion = (screenWidth + screenHeight)/1000

        n = self.size

        for row in range(self.size):
            for column in range(self.size):

                   boxWidth = screenWidth / n
                   boxHeight = screenHeight / n

                   boxCenterOffset = boxWidth / 2
                   boxCenterOffset = boxHeight / 2

                   boxRowPosition = row * boxWidth
                   boxColumnPosition = column * boxHeight

                   self.CHARACTER_TEXT = font.get_title_font(smaller = self.sumProportion * n / 8).render(self.board[row][column], True, "Red")
                   self.CHARACTER_RECT = self.CHARACTER_TEXT.get_rect(center=(boxRowPosition + boxCenterOffset, boxColumnPosition + boxCenterOffset))

                   for characterObject in [(self.CHARACTER_TEXT, self.CHARACTER_RECT)]:
                        screen.blit(characterObject[0], characterObject[1])

                   print(self.board[row][column],end=" ")
            print()

        if self.game_over:
            print('game over')
            print('wins:', self.wins)

        else:
            print('now moves:', self.who_moves)
            print('possible moves:', self.possibleMoves())