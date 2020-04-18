class Player :
    def __init__(self, name, symbol, is_ai = False, is_winner = False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai
        self.is_winner = is_winner