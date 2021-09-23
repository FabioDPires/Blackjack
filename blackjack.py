from pip._vendor.distlib.compat import raw_input

from card import Card
from player import Player
from deck import Deck
import os
import time


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(False)
        self.dealer = Player(True)

    def play(self):
        self.start_game()
        self.player_turn()

        if self.player.count > 21:
            print('BUSTED! You lost')
        else:

            print("Player's Cards")
            self.player.print_player_cards()
            print(f'Score: {self.player.count}')
            print("Dealer's Cards")
            self.dealer.print_player_cards()
            self.dealer.calculate_player_score()
            print(f"Dealer's Score: {self.dealer.count}")
            self.dealer_turn()
            if self.player.count > self.dealer.count:
                print('You won!')
            elif self.player.count == self.dealer.count:
                print('Tie')
            else:
                if self.dealer.count <= 21:
                    print('You lost')
                else:
                    print("You win! Dealer busted!")

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
            BlackJack.clear_screen()
            if response == 'S':
                draw = False
            else:
                self.player.hit_me(self.deck)
                print("Player's card")
                self.player.print_player_cards()
                print(f'Player score: {self.player.count}')
                if self.player.count == 21:
                    print('BLACKJACK!')
                print("Dealer's cards")
                self.dealer.print_first_card()
                Card.print_downed_card()
                self.dealer.calculate_dealer_score_first_round()
                print(f"Dealer's Score: {self.dealer.count}")

    def dealer_turn(self):

        while self.dealer.count < 17:
            BlackJack.clear_screen()
            self.dealer.hit_me(self.deck)
            print("Player's Cards")
            self.player.print_player_cards()
            print(f'Score: {self.player.count}')
            print("Dealer's Cards")
            self.dealer.print_player_cards()
            self.dealer.calculate_player_score()
            print(f"Dealer's Score: {self.dealer.count}")
            if self.dealer.count < 17:
                time.sleep(3)

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


play = True
while play:
    blackjack = BlackJack()
    blackjack.play()
    raw_input('Press enter to play again: ')
    BlackJack.clear_screen()
