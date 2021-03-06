from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        for x in range(4):  # values 0,1,2,3 of cards' suit
            for y in range(13):
                card = Card(y + 1, x);
                self.cards.append(card);

        random.shuffle(self.cards)

    def show_deck_card(self):
        for card in self.cards:
            print(f'|Suit: {card.suit} ,Value: {card.value}    |')

    def draw_card(self):
        drawn_card = self.cards[0]
        self.cards.pop(0)
        return drawn_card
