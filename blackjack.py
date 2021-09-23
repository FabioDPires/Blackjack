from card import Card
from player import Player
from deck import Deck


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(False)
        self.dealer = Player(True)

    def play(self):
        self.start_game()

    def start_game(self):
        self.deck.fill_deck()
        self.player.hit_me(self.deck)
        self.player.hit_me(self.deck)
        print("Player's Cards")
        self.player.print_player_cards()
        print(f'Score: {self.player.count}')
        print("Dealer's Cards")
        self.dealer.hit_me(self.deck)
        self.dealer.hit_me(self.deck)
        self.dealer.print_first_card()
        Card.print_downed_card()
        self.dealer.calculate_dealer_score_first_round()
        print(f"Dealer's Score: {self.dealer.count}")


blackjack = BlackJack()
blackjack.play()
