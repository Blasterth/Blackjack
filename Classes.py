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
    def __init__(self):
        self.money = 0
        self.bet_amount = 0
    #Bet
    def bet(self):
        self.wager = input("Please input the amount you would like to wager.")
        if len(self.wager) == 0:
            print(CONSTANTS.EMPTY_INPUT_ERROR_MESSAGE)
            self.bet()
        elif self.wager.isnumeric() == True:
            if int(self.wager) >= 1 and int(self.wager) <= self.money:
                self.bet_amount = int(self.wager)
                self.money -= int(self.wager)
                print(f"You bet {self.wager}.")
            else:
                print(CONSTANTS.OUT_OF_RANGE_ERROR_MESSAGE)
                self.bet()
        else:
            print(CONSTANTS.BAD_INPUT_ERROR_MESSAGE)
            self.bet()


#Player Hand Class
class PlayerHand:
    #Attributes
    def __init__(self):
        self.cards_in_hand = []
        self.value = 0
    #Hit
    def hit(self,new_card):
        print("Hit!")
        self.cards_in_hand.append(new_card)
    #Cards in hand
    def __repr__(self):
        for card in self.cards_in_hand:
            return card.__repr__()


#Player Class
class Player(PlayerHand,PlayerBet):
    #Attributes
    def __init__(self,):
        PlayerHand.__init__(self)
        PlayerBet.__init__(self)


#Dealer Hand Class
class DealerHand(PlayerHand):
    #Attributes
    def __init__(self):
        PlayerHand.__init__(self)


#Dealer Class
class Dealer(DealerHand):
    #Attributes
    def __init__(self,name="Dealer"):
        DealerHand.__init__(self)
        self.name = name