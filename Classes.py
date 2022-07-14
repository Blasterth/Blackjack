import CONSTANTS

#Card Class
class Card:
    #Attributes
    def __init__(self,symbol,suit,value=None):
        self.symbol = symbol
        self.suit = suit
        self.value = value
        #Check if cards are okay
        if self.symbol not in CONSTANTS.SYMBOL_LIST:
            raise Exception("Symbols are based on the letters/numbers on the top right of real cards.")
        elif self.suit not in CONSTANTS.SUIT_LIST:
            raise Exception("We don't have such a suit\nCheck the sppelling/Casing.")
        #Setting card Values
        else:
            try:
                self.value = int(self.symbol)
            except:
                if self.symbol in CONSTANTS.FACE_CARDS_LIST:
                        self.value = 10
                elif self.symbol == "A":
                    self.value = 11
    #Name of the card
    def __str__(self):
        try:
            return f"{int(self.symbol)} of {self.suit}"
        except:
            if self.symbol == "J":
                return f"Jack of {self.suit}"
            elif self.symbol == "Q":
                return f"Queen of {self.suit}"
            elif self.symbol == "K":
                return f"King of {self.suit}"
            elif self.symbol == "A":
                return f"Ace of {self.suit}"


#Player Hand Class
class PlayerHand:
    pass

#Player Bet Class
class PlayerBet:
    pass

#Player Class
class Player:
    pass

#Dealer Hand Class
class DealerHand:
    pass

#Dealer Class
class Dealer:
    pass

#Deck Class
class Deck:
    pass