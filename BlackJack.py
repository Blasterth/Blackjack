import Classes


##Intro
print("Welcome to Blackjack. Copyright (c) 2022 Parsa Aryan")

#Get Username
user = Classes.Player()
user_name = input("Please input your name. (An empty input means you wanna use the name (Player).)")
if len(user_name) == 0:
    pass
else:
    user.name = user_name

#Create Deck
game_deck = Classes.Deck()
game_deck.shuffle()

#Create Dealer
table_dealer = Classes.Dealer()