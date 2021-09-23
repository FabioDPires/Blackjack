from card import Card
from player import Player
from deck import Deck
import os


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(False)
        self.dealer = Player(True)

    def play(self):
        self.start_game()
        self.player_turn()

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

    def player_turn(self):
        draw = True
        while draw and self.player.count < 21:
            print("Hit (H) or Stand (S)")
            response = input()
            if response == 'S':
                draw = False
            else:
                BlackJack.clear_screen()
                self.player.hit_me(self.deck)
                self.player.print_player_cards()
                print(f'Player score: {self.player.count}')
                if self.player.count == 21:
                    print('BLACKJACK!')
                elif self.player.count > 21:
                    print('BUSTED!')
                self.dealer.print_first_card()
                Card.print_downed_card()
                self.dealer.calculate_dealer_score_first_round()
                print(f"Dealer's Score: {self.dealer.count}")

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


blackjack = BlackJack()
blackjack.play()