class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value - 1]
        self.suit = '♥♦♣♠'[suit]

    # Note: in Python is a good practise that functions' names should be all lowercase. So if a function's name has
    # more than one word they should be separated by a _
    def get_price(self):

        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost

    def print_card(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')

    @staticmethod
    def print_downed_card():
        print('┌───────┐')
        print('|       |')
        print('|       |')
        print('|       |')
        print('|       |')
        print('|       |')
        print('└───────┘')
