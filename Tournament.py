from Game import Game
from NineCoins import *

class Tournament:
    def runNineCoins(self):
        
        # For i in 1 to 10:
        # play the players one way, set the board seed to i, play the players the other way, set the board seed again
        for seed in range(1, 11):
          print(f'Playing game {seed}')
          players = [NineCoinsPlayer(0), NineCoinsPlayer(1)]
          board = NineCoinsBoard()
          game = Game(players, board)
          game.setup(seed)
          endState = game.loop()

          gameOneScores = endState.scores

          print(endState)

          players = [NineCoinsPlayer(1), NineCoinsPlayer(0)]
          game = Game(players, board)
          game.setup(seed)
          endState = game.loop()

          gameTwoScores = endState.scores

          print(endState)

          if gameOneScores[0] != gameTwoScores[0]:
              print ("Different scores!")
          if (gameOneScores[0] > gameOneScores[1] and gameTwoScores[1] > gameTwoScores[0]) or (gameOneScores[0] < gameOneScores[1] and gameTwoScores[1] < gameTwoScores[0]):
              print ("DIFFERENT WINNER!")


tourney = Tournament()
tourney.runNineCoins()