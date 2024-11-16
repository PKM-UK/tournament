from Game import Game
from NineCoins import *

class Tournament:
    def runNineCoins(self):
        
        # For i in 1 to 10:
        # play the players one way, set the board seed to i, play the players the other way, set the board seed again
        algo_totals = [0, 0]
        algo_wins = [0, 0]

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

          algo_totals[0] = algo_totals[0] + gameOneScores[0] + gameTwoScores[1]
          algo_totals[1] = algo_totals[1] + gameOneScores[1] + gameTwoScores[0]
          if gameOneScores[0] > gameOneScores[1]:
            algo_wins[0] = algo_wins[0] + 1
          elif gameOneScores[0] < gameOneScores[1]:
            algo_wins[1] = algo_wins[1] + 1
          if gameTwoScores[0] < gameTwoScores[1]:
            algo_wins[0] = algo_wins[0] + 1
          elif gameTwoScores[0] > gameTwoScores[1]:
            algo_wins[1] = algo_wins[1] + 1

        print(f'Greedy vs lookahead points totals {algo_totals}, a total of {algo_wins} games')     


tourney = Tournament()
tourney.runNineCoins()