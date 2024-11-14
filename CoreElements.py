class Board():
    def __init__(self):
        self.state = None

    def getState(self):
        return None

    def doTurn(self, turn):
        return None
    
class Player():
    def __init__(self):
        self.agent = None

    def takeTurn(self, state):
        return None
    
class Turn():
    def __init__(self):
        self.actions = None

class BoardState():
    def __init__(self):
        self.terminated = False

