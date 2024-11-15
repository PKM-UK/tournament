from CoreElements import Player, Board, Turn, BoardState
import random

class NineCoinsBoard(Board):
    def __init__(self):
        self.board = []

    def init(self, seed = 0):
        random.seed(seed)
        self.board = [int(random.random() * 10) for i in range(1,9)]
        print(self.board)
        self.nextPlayer = 0
        self.scores = [0, 0]
        self.terminated = False

    def getState(self):
        sendState = NineCoinsState(self.board, self.nextPlayer, self.scores, self.terminated)
        return sendState

    def doTurn(self, turn):
        takenCoin = 0
        if turn.actions[0] == 'L':
            takenCoin = self.board.pop(0)
        else:
            takenCoin = self.board.pop()
        self.scores[self.nextPlayer] = self.scores[self.nextPlayer] + takenCoin

        print(f'Player {self.nextPlayer} takes {takenCoin} to make {self.scores[self.nextPlayer]}')
        print(f'Board is now {self.board}')
        if len(self.board) < 1:
            self.terminated = True
        self.nextPlayer = 1 - self.nextPlayer

class NineCoinsPlayer(Player):
    def takeTurn(self, state):
        # Algorithm here! Factor out later
        action = ''
        if state.board[0] > state.board[-1]:
            action = 'L'
        else:
            action = 'R'
        turn = NineCoinsTurn(action)
        return turn

class NineCoinsTurn(Turn):
    def __init__(self, action):
        self.actions = [action]

class NineCoinsState(BoardState):
    def __init__(self, board, nextPlayer, scores, terminated):
        self.board = board
        self.nextPlayer = nextPlayer
        self.scores = scores
        self.terminated = terminated

    def __str__(self):
        return f'Board is {self.board}. Scores {self.scores[0]} - {self.scores[1]}'