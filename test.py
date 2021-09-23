from deck import Deck
from player import Player


class Test:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(False)
        self.dealer = Player(True)

    def test_generate_deck(self):
        self.deck.fill_deck()

    def test_show_deck(self):
        self.deck.show_deck_card()

    def test_draw_card(self):
        self.player.hit_me(self.deck)


test = Test()
test.test_generate_deck()
test.test_show_deck()
draw = True

while draw:
    print("Draw Card? Y or N")
    response = input()
    if response == 'N':
        draw = False
    else:
        print("Draw card")
        test.test_draw_card()
        print("New deck")
        test.test_show_deck()
