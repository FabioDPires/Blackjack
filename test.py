from deck import Deck


class Test:
    def __init__(self):
        self.deck = Deck()

    def test_generate_deck(self):
        self.deck.fill_deck()
        self.deck.show_deck_card()


test = Test()
test.test_generate_deck()
