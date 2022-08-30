import Classes
import CONSTANTS


##Intro
print("Welcome to Blackjack. Copyright (c) 2022 Parsa Aryan")

#Get Username
new_player = Classes.Player()
new_player_name = input("Please input your name. (An empty input means you wanna use the name 'Player'.)")
if len(new_player_name) == 0:
    pass
else:
    new_player.name = new_player_name

#Get Money
def get_money():
    new_player_money = input("Please input the amount you would like to wager.")
    if len(new_player_money) == 0:
        print(CONSTANTS.EMPTY_INPUT_ERROR_MESSAGE)
        get_money()
    elif new_player_money.isnumeric() == True:
        if int(new_player_money) >= 1 and int(new_player_money) in range(100,1000+1):
            new_player.money == int(new_player_money)
            print(f"You start with {new_player_money}.")
        else:
            print(CONSTANTS.OUT_OF_RANGE_ERROR_MESSAGE)
            get_money()
    else:
        print(CONSTANTS.BAD_INPUT_ERROR_MESSAGE)
        get_money()

#Create Deck
new_deck = Classes.Deck()
new_deck.shuffle()

#Create Dealer
new_dealer = Classes.Dealer()


##Gameplay
print("GO!")

#Number of Victories
new_dealer_victories = 0
new_player_victories = 0

#Deal Cards
for card in range(2):
    new_dealer.hit(new_deck.deal_one())
    new_player.hit(new_deck.deal_one())