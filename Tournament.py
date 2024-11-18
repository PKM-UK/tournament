from Game import Game
from NineCoins import *

class Tournament:
    def runNineCoins(self):
        # For i in 1 to 10:
        # play the players one way, set the board seed to i, play the players the other way, set the board seed again
        
        # Make table of algorithm wins
        algo_scorelines = [[(), (), ()], [(), (), ()], [(), (), ()]]

        for playerOneAlgorithm in [0,1,2]:
            for playerTwoAlgorithm in [0,1,2]:
                print(f'Playing set {playerOneAlgorithm} - {playerTwoAlgorithm}')
                set_totals = [0, 0]
                set_wins = [0, 0]            
                for seed in [setgame + playerOneAlgorithm*100 + playerTwoAlgorithm*10 for setgame in range(9, 19)]:
                    print(f'Playing game {seed}')
                    players = [NineCoinsPlayer(playerOneAlgorithm), NineCoinsPlayer(playerTwoAlgorithm)]
                    board = NineCoinsBoard()
                    game = Game(players, board)
                    game.setup(seed)
                    endState = game.loop()
                    gameOneScores = endState.scores
                    print(endState)

                    players = [NineCoinsPlayer(playerTwoAlgorithm), NineCoinsPlayer(playerOneAlgorithm)]
                    game = Game(players, board)
                    game.setup(seed)
                    endState = game.loop()
                    gameTwoScores = endState.scores
                    print(endState)

                    if gameOneScores[0] != gameTwoScores[0]:
                        print ("Different scores!")
                    if (gameOneScores[0] > gameOneScores[1] and gameTwoScores[1] > gameTwoScores[0]) or (gameOneScores[0] < gameOneScores[1] and gameTwoScores[1] < gameTwoScores[0]):
                        print ("DIFFERENT WINNER!")


                    set_totals[0] = set_totals[0] + gameOneScores[0] + gameTwoScores[1]
                    set_totals[1] = set_totals[1] + gameOneScores[1] + gameTwoScores[0]
                    if gameOneScores[0] > gameOneScores[1]:
                        set_wins[0] = set_wins[0] + 1
                    elif gameOneScores[0] < gameOneScores[1]:
                       set_wins[1] = set_wins[1] + 1
                    if gameTwoScores[0] < gameTwoScores[1]:
                       set_wins[0] = set_wins[0] + 1
                    elif gameTwoScores[0] > gameTwoScores[1]:
                       set_wins[1] = set_wins[1] + 1
                  
                # End of ten game "set" - which algorithm won more?
                algo_scorelines[playerOneAlgorithm][playerTwoAlgorithm] = (set_wins, set_totals[1]/(set_totals[0]+set_totals[1]))
        print("END OF TOURNAMENT")
        print(algo_scorelines[0])
        print(algo_scorelines[1])
        print(algo_scorelines[2])        

def gameTest():
    players = [NineCoinsPlayer(0), NineCoinsPlayer(2)]
    board = NineCoinsBoard()
    game = Game(players, board)
    game.setup(1)
    endState = game.loop()
    gameOneScores = endState.scores
    print(endState)

if __name__ == "__main__":
    tourney = Tournament()
    tourney.runNineCoins()

    # gameTest()