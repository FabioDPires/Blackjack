class Player:
    def __init__(self, is_dealer):
        self.count = 0;
        self.player_cards = []
        self.isDealer = is_dealer

    def hit_me(self, deck):
        drawn_card = deck.draw_card()
        print(f' Drawn card - Suit: {drawn_card.suit} Value: {drawn_card.value}')
        self.player_cards.append(drawn_card)
        self.count += drawn_card.get_price()
