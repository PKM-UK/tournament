class Game:
    def __init__(self, players, board):
        self.board = board
        self.players = players

    def setup(self):
        self.board.init()

    def loop(self):
        gameState = self.board.getState()

        while not gameState.terminated:
            nextPlayer = self.players[gameState.nextPlayer]
            turn = nextPlayer.takeTurn(gameState)
            self.board.doTurn(turn)
            gameState = self.board.getState()

        return gameState