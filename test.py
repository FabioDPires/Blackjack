from deck import Deck


class Test:
    def __init__(self):
        self.deck = Deck()

    def test_generate_deck(self):
        self.deck.fill_deck()

    def test_show_deck(self):
        self.deck.show_deck_card()

    def test_draw_card(self):
        card = self.deck.draw_card()
        print(f' Drawn card - Suit: {card.suit} Value: {card.value}')


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
