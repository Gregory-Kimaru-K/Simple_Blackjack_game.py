import random

# CARD CLASS

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    
    def __str__(self) :
        return f"{Card.ranks[self.rank]}{Card.suits[self.suit]}"
    
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank

# DECK CLASS

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                #Create card
                self.deck.append(Card(rank,suit))
            self.shuffle_cards()

    
    def __len__(self):
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)
    
    def pop_card(self):
        return self.deck.pop()
    
    def shuffle_cards(self):
        random.shuffle(self.deck)


# CLASS PLAYER

class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ', '.join([str(card) for card in self.deck])
    
    def get_label(self):
        return self.label
    
    def get_win_count(self):
        return self.win_count 
    
    def round_winner(self):
        self.win_count += 1
    
d = Deck()
hands = []
for i in range(1, 5):
    hands.append(Hand(f'P{i}'))

while len(d) > 0:
    for h in hands:
        h.add_card(d.pop_card())

print(hands[0])

for i in range(1,14):
    input()
    played_cards = []

    for h in hands:
        played_cards.append(h.pop_card())

    winner_card = max(played_cards)
    winner_hand = hands[played_cards.index(winner_card)]

    winner_hand.round_winner()

    print(f"R{i}\n" + ' '.join([str(card) for card in played_cards]) + f"\nWinner: {winner_hand.get_label()} {str(winner_card)}")

for h in hands:
    print(f'score for {h.get_label()}: {h.get_win_count()}')