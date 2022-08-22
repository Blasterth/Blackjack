from base64 import standard_b64decode
import random
import CONSTANTS


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


#Player Bet Class
class PlayerBet:
    #Attributes
    def __init__(self,money=100):
        self.money = money
        self.bet_amount = 0
    #Bet
    def bet(self):
        self.wager = 0
        while True:
            try:
                self.wager = input("Please input the amount you would like to bet.")
                if int(self.wager) <= self.money:
                    self.bet_amount = int(self.wager)
                    return f"You bet {self.bet_amount}."
            except:
                return "Try again."
    #Money Remaining
    def __repr__(self):
        return f"{self.money} remaining.\n{self.bet_amount} in the bet area."


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
        self.value += new_card.value
    #Stand
    global stand
    def stand(self):
        self.status = "Standing"
    #Surrender
    def surrender(self):
        self.status = "Surrendered"
    #Cards in hand
    def __repr__(self):
        for card in self.cards_in_hand:
            return card.__repr__()


#Player Class
class Player(PlayerHand,PlayerBet):
    #Attributes
    def __init__(self,name="Player"):
        self.name = name


#Dealer Hand Class
class DealerHand(PlayerHand):
    pass

#Dealer Class
class Dealer(DealerHand):
    #Attributes
    def __init__(self,name="Dealer"):
        self.name = name