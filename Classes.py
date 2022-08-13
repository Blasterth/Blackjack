from base64 import standard_b64decode
import random
import CONSTANTS
import functions


#Card Class
class Card:
    #Attributes
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = CONSTANTS.VALUE_DICTIONARY[self.rank]
    #Name of the card
    def __repr__(self):
        return f"{self.rank} of {self.suit}"


#Deck Class
class Deck:
    #Attributes
    def __init__(self):
        self.card_list = []
        for suit in CONSTANTS.SUIT_LIST:
            for rank in CONSTANTS.RANK_LIST:
                self.card_list.append(Card(rank,suit))
    #Shuffle
    def shuffle(self):
        random.shuffle(self.card_list)
    #Deal One
    def deal_one(self):
        return self.card_list.pop()


#Player Hand Class
class PlayerHand:
    #Attributes
    def __init__(self):
        self.cards_in_hand = []
        self.value = 0
        for card in self.cards_in_hand:
            self.value += card.value
        self.status = "Hitting"
        if self.value < 21:
            self.status = "Bust"
            stand()
    #Hit
    def hit(self,new_card):
        print("Hit!")
        self.cards_in_hand.append(new_card)
    #Stand
    global stand
    def stand(self):
        self.status = "Standing"
    #Cards in hand
    def __repr__(self):
        for card in self.cards_in_hand:
            return card.__repr__()


#Player Bet Class
class PlayerBet:
    #Attributes
    def __init__(self,money=100):
        self.money = money
        self.bet_amount = 0
    #Bet
    def bet(self):
        self.wagered_money = print(functions.bet_input())
        self.money -= self.wagered_money
        self.bet_amount += self.wagered_money
    #Money Remaining
    def __repr__(self):
        return f"{self.money} remaining.\n{self.bet_amount} in the bet area."


#Player Class
class Player(PlayerHand,PlayerBet):
    #Attributes
    def __init__(self,name="Player"):
        self.name = name
    #Option List
    def options(self):
        self.player_desired_option = input()


#Dealer Hand Class
class DealerHand:
    pass

#Dealer Class
class Dealer:
    pass

class DealerHand:
    pass

#Dealer Class
class Dealer:
    pass