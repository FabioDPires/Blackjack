from pip._vendor.distlib.compat import raw_input

from card import Card
from player import Player
from deck import Deck
import os
import time


def show_instructions():
    print("Both you and the dealer start with 2 cards each but you can only see the dealer's first card.")
    print('You have the option to "stand" (not ask for another card) or "hit" (ask for another card in an attempt '
          'to get closer to a count of 21, or even hit 21 exactly).')
    print("Once your turn is over is the dealer's turn. The dealer's face-down card is turned up. If the total "
          "is 17 or more, it must stand. If the total is 16 or under, a card must be taken.\nThe dealer must "
          "continue to take cards until the total is 17 or more, at which point the dealer must stand.\nIf the "
          "dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), "
          "the dealer must count the ace as 11 and stand.")
    print("Both you and the dealer start with 2 cards each but you can only see the dealer's first card.")
    print("Card values:")
    print(" Ace - 1 or 11\n Face cards(Joker, Queen, King) - 10\n Others - its pip value.")
    print("\n")


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


blackJack = BlackJack()
showMenu = True
while showMenu:
    print("Welcome. Select an option:")
    print("1-Play")
    print("2-Instructions")
    print("3-Quit")
    option = input()
    BlackJack.clear_screen()
    if option == "1":
        showMenu = False
        play = True
        while play:
            blackjack = BlackJack()
            blackjack.play()
            raw_input('Press enter to play again: ')
            BlackJack.clear_screen()
    elif option == "2":
        show_instructions()
        raw_input('Press enter to go back: ')
        BlackJack.clear_screen()
    elif option == 3:
        print("Quit")
    else:
        print("Invalid option")
