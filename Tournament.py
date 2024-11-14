from Game import Game
from NineCoins import *

class Tournament:
    def runNineCoins(self):
        players = [NineCoinsPlayer(), NineCoinsPlayer()]

        board = NineCoinsBoard()

        game = Game(players, board)

        game.setup()
        endState = game.loop()

        print(endState)

tourney = Tournament()
tourney.runNineCoins()