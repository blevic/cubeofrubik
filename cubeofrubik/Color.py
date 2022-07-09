from enum import Enum

class Color(Enum):
    """Colors enumeration"""
    RED = ('R', '🟥')
    ORANGE = ('O', '🟧')
    YELLOW = ('Y', '🟨')
    WHITE = ('W', '⬜')
    BLUE = ('B', '🟦')
    GREEN = ('G', '🟩')
    BLACK = ('-', '⬛')

    def __init__(self, letter, emoji):
        self.letter = letter
        self.emoji = emoji

    def __str__(self):
        return self.name