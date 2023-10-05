# https://py2.codeskulptor.org/#user50_tSqIhovR6u9J2QK.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
card_imgs = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
inPlay = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_imgs, card_loc, CARD_SIZE, [pos[0] + (0.5 * CARD_SIZE[0]), pos[1] + (0.5 * CARD_SIZE[1])], CARD_SIZE)
        
    def draw_back(self, canvas, pos):
        card_loc = ((0.5 * CARD_BACK_SIZE[0]), (0.5 * CARD_BACK_SIZE[1]))
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + (0.5 * CARD_BACK_SIZE[0]) + 1, pos[1] + (0.5 * CARD_BACK_SIZE[1]) + 1], CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        """ Creates Hand object """
        self.cards = []

    def __str__(self):
        """ Returns a string representation of a hand """
        if not self.cards:
            return "got nothing in hand"
        return "holding " + " ".join(str(card) for card in self.cards) + "."

    def add_card(self, card):
        """ Adds a card object to a hand """
        self.cards.append(card)

    def get_value(self):
        """Computes the value of the hand. Counts aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust."""
        current_value = sum(VALUES[card.get_rank()] for card in self.cards) 
        has_ace = any(card.get_rank() == 'A' for card in self.cards)
        if has_ace and current_value <= 11:
            current_value += 10
        return current_value

    def draw(self, canvas, pos):
        """ Draws a hand on the canvas, uses the draw method for cards """
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 30
            card.draw(canvas, pos)
 
        
# define deck class 
class Deck:
    def __init__(self):
        """ Creates a Deck object """
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffles the deck, using random.shuffle() """
        random.shuffle(self.cards)

    def deal_card(self):
        """ Deals a card object from the deck """
        return self.cards.pop()
    
    def __str__(self):
        """ Returns a string representing the deck """
        if not self.cards:
            return "Deck contains nothing."
        return "Deck contains " + " ".join(str(card) for card in self.cards) + "."


#define event handlers for buttons
def deal():
    global outcome, score, inPlay, deck, player_hand, dealer_hand, prompt
    if inPlay:
        inPlay = False
        score -= 1
        deal()
    else:
        player_hand = Hand()
        dealer_hand = Hand()
        deck = Deck()
        deck.shuffle()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        outcome = "Hit or Stand?"
        prompt = ""
        inPlay = True

def hit():
    global prompt, outcome, score, inPlay, deck, player_hand
    if inPlay:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            if player_hand.get_value() > 21:
                prompt = "You are BUSTED!!! You loose."
                score -= 1
                outcome = "New Deal?"
                inPlay = False
       
def stand():
    global prompt, player_hand, dealer_hand, score, inPlay, deck, outcome
    if inPlay:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            prompt = "Dealer BUSTED!!! You win."
            score += 1
        elif player_hand.get_value() > dealer_hand.get_value():
            prompt = "You win."
            score += 1
        else:
            prompt = "You loose."
            score -= 1
        outcome = "New Deal?"
        inPlay = False

# draw handler    
def draw(canvas):
    canvas.draw_text("BLACKJACK", (100, 70), 70, "Black")
    canvas.draw_text("DEALER", (36, 185), 30, "White", "monospace")
    canvas.draw_text("PLAYER", (36, 385), 30, "White", "monospace")
    canvas.draw_text(outcome, (210, 385), 25, "Silver")
    canvas.draw_text(prompt, (210, 185), 25, "Silver")
    canvas.draw_text("Score : " + str(score), (210, 130), 40, "Red", "sans-serif")
    dealer_hand.draw(canvas, [-65, 200])
    player_hand.draw(canvas, [-65, 400])
    if inPlay:
        dealer_hand.cards[0].draw_back(canvas, [36, 199])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal)
frame.add_button("Hit",  hit)
frame.add_button("Stand", stand)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric