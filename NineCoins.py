from CoreElements import Player, Board, Turn, BoardState
import random

class NineCoinsBoard(Board):
    def __init__(self):
        self.board = []

    def init(self, seed = 0, length = 8):
        random.seed(seed)
        # self.board = [int((random.random() * 10) ** 2) for i in range(1,length + 1)]
        self.board = [2 ** int((random.random() * 9) - 1) for i in range(1,length + 1)]
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

        # print(f'Player {self.nextPlayer} takes {takenCoin} to make {self.scores[self.nextPlayer]}')
        # print(f'Board is now {self.board}')
        if len(self.board) < 1:
            self.terminated = True
        self.nextPlayer = 1 - self.nextPlayer

class NineCoinsPlayer(Player):
    def __init__(self, algorithm):
        self.algorithm = algorithm
        
    def greedyValue(self, board, direction):
        # Value functions return the expected value of a direction to the player taking the turn
        if direction == 'L':
            return board[0]
        else:
            return board[-1]

    def greedyPick(self, board):
        # Pick functions return (action, value)
        if len(board) == 1:
            return ('L', board[0])
        else:
            lValue = self.greedyValue(board, 'L')
            rValue = self.greedyValue(board, 'R')
            # print(f'L gives {lValue}, R gives {rValue}')
            return ('L', lValue) if lValue > rValue else ('R', rValue)
        
    def oneLookaheadValue(self, board, direction):
        if len(board) == 1:
            # We get the one coinn
            return board[0]
        elif len(board) == 2:
            # We pick one, opponent picks the other
            if direction == 'L':
                return board[0] - board[1]
            else:
                return board[1] - board[0]
        else:
            # There are three or coins - return ours minus greedy pick of the remainder
            if direction == 'L':
                # This could be board[0] - greedyValue(board[1:])[0]
                # That's how to write recursive minmax
                # print(f'L would return {board[0] - max(board[1], board[-1])} ({board[0]} minus {max(board[1], board[-1])})')
                return board[0] - max(board[1], board[-1])
            else:
                # print(f'R would return {board[-1] - max(board[0], board[-2])} ({board[-1]} minus {max(board[0], board[-2])})')
                return board[-1] - max(board[0], board[-2])
            
    def oneLookAheadPick(self, board):
        # Pick functions return (action, value)
        if len(board) == 1:
            return ('L', board[0])
        else:
            lValue = self.oneLookaheadValue(board, 'L')
            rValue = self.oneLookaheadValue(board, 'R')
            return ('L', lValue) if lValue > rValue else ('R', rValue)

    def minMax(self, board, depth):
        if len(board) == 1:
            return ('L', board[0])
        elif len(board) == 2:
            if board[0] > board[1]:
                return ('L', board[0] - board[1])
            else:
                return ('R', board[1] - board[0])
        elif depth == 0:
            if board[0] > board[-1]:
                return ('L', board[0])
            else:
                return ('R', board[-1])
        else:
            lUtility = board[0] - self.minMax(board[1:], depth-1)[1]
            rUtility = board[-1] - self.minMax(board[:-1], depth-1)[1]
            if lUtility > rUtility:
                return ('L', lUtility)
            else:
                return ('R', rUtility)
             
    def takeTurn(self, state):
        # Algorithm here! Factor out later
        # Algo argument should be depth of recursion - 
        # 0 is greedy, 1 is one step, 10 is whole game
        action = ''
        if self.algorithm == 0:
            action = self.greedyPick(state.board)[0]
        elif self.algorithm == 1:
            action = self.oneLookAheadPick(state.board)[0]
        else:
            action = self.minMax(state.board, 10)[0]

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
        return f'Scores {self.scores[0]} - {self.scores[1]}'

def testHarness():
    testPlayer = NineCoinsPlayer(2)
    testBoard = NineCoinsBoard()
    testBoard.init(1, 4)
    turn = testPlayer.takeTurn(testBoard.getState())

    print(turn.actions)

if __name__ == "__main__":
    testHarness()