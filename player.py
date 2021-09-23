class Player:
    def __init__(self, is_dealer):
        self.count = 0;
        self.player_cards = []
        self.isDealer = is_dealer

    def hit_me(self, deck):
        drawn_card = deck.draw_card()
        self.player_cards.append(drawn_card)
        self.calculate_player_score()

    def print_player_cards(self):
        for card in self.player_cards:
            card.print_card()

    def print_first_card(self):
        card=self.player_cards[0]
        card.print_card()

    def calculate_player_score(self):
        self.count = 0
        ace_counter = 0
        for card in self.player_cards:
            self.count += card.get_price()
            if card.value == 'A':
                ace_counter += 1

        while self.count > 21 and ace_counter > 0:
            self.count -= 10
            ace_counter -= 1

    def calculate_dealer_score_first_round(self):
        self.count=self.player_cards[0].get_price()
