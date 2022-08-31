import Classes
import CONSTANTS


##Intro
print("Welcome to Blackjack. Copyright (c) 2022 Parsa Aryan")

#Create Player
new_player = Classes.Player()

#Get Money
def get_money():
    new_player_money = input("Please input the amount you would like to start with (100-1000).")
    if len(new_player_money) == 0:
        print(CONSTANTS.EMPTY_INPUT_ERROR_MESSAGE)
        get_money()
    elif new_player_money.isnumeric() == True:
        new_player_money = int(new_player_money)
        if new_player_money >= 1 and new_player_money in range(100,1001):
            new_player.money = new_player_money
            print(f"You start with {new_player.money}.")
        else:
            print(CONSTANTS.OUT_OF_RANGE_ERROR_MESSAGE)
            get_money()
    else:
        print(CONSTANTS.BAD_INPUT_ERROR_MESSAGE)
        get_money()
get_money()

#Create Deck
new_deck = Classes.Deck()
new_deck.shuffle()

#Create Dealer
new_dealer = Classes.Dealer()


##Variables

#Number of Victories
new_dealer_victories = 0
new_player_victories = 0
pushes = 0

#Time
turn = 1


##Logic

#Initial Deal
def initial_deal():
    #Deal First 2 Cards
    for card in range(2): new_dealer.hit(new_deck.deal_one())
    for card in range(2): new_player.hit(new_deck.deal_one())

    #Take the value of first 2 cards into account
    #Note: From first Ace onward the value of other ones is reduced to 1 (A Hard Hand)
    if new_dealer.cards_in_hand[0].rank == "Ace" and new_dealer.cards_in_hand[1].rank == "Ace":
        new_dealer.cards_in_hand[1].value == 1
    for card in new_dealer.cards_in_hand:
        new_dealer.value += card.value
    if new_player.cards_in_hand[0].rank == "Ace" and new_player.cards_in_hand[1].rank == "Ace":
        new_player.cards_in_hand[1].value == 1
    for card in new_player.cards_in_hand:
        new_player.value += card.value

#Display
def display():
    print(f"\nTurn {turn}")
    print("Player's turn:")
    print(f"Player Victories: {new_player_victories}|Dealer Victories: {new_dealer_victories}|Pushes: {pushes}")
    print(f"You've got {new_player.money}")
    print("\nPlayer's cards:")
    for card in new_player.cards_in_hand:
        print(card)
    print("\nDealer's cards:")
    for card in new_dealer.cards_in_hand:
        if card == new_dealer.cards_in_hand[0]:
            print("HOLE CARD")
        else:
            print(card)

#Player Turn
def new_player_turn():
    new_player.bet()
    def new_player_action():
        display()
        new_player_input = input("\nType:\nHit to get a card.\nStand to stop getting card.\nSurrender to ...")
        if len(new_player_input) == 0:
            print(CONSTANTS.EMPTY_INPUT_ERROR_MESSAGE)
            new_player_action()
        elif new_player_input.lower() == "hit":
            new_player.hit(new_deck.deal_one())
            if new_player.cards_in_hand[-1].rank == "Ace" and new_player.value >= 11:
                new_player.cards_in_hand[-1].value == 1
            new_player.value += new_player.cards_in_hand[-1].value
            print(new_player.value)
            if new_player.value > 21:
                print("Player Busts!")
                print(CONSTANTS.DEALER_VICTORY)
                new_player.bet_amount = 0
                global new_dealer_victories
                new_dealer_victories += 1
            else:
                new_player_action()
        elif new_player_input.lower() == "stand":
            new_dealer_turn()
        elif new_player_input.lower() == "surrender":
            new_player.bet_amount % 2
            new_player.money += new_player.bet_amount
            new_player.bet_amount = 0
            new_dealer_victories += 1
        else:
            print(CONSTANTS.BAD_INPUT_ERROR_MESSAGE)
            new_player_action()
    new_player_action()

#Dealer Turn
global new_dealer_turn
def new_dealer_turn():
    print("\nDealer's turn:")
    for card in new_dealer.cards_in_hand:
        print(card)
    while new_dealer.value < 17:
        new_dealer.hit(new_deck.deal_one())
        print(new_dealer.cards_in_hand[-1])
        if new_dealer.cards_in_hand[-1].rank == "Ace" and new_dealer.value >= 11:
            new_dealer.cards_in_hand[-1].value == 1
        new_dealer.value += new_dealer.cards_in_hand[-1].value
        print(new_dealer.value)
    if new_dealer.value > 21:
        print("Dealer Busts!")
        print(CONSTANTS.PLAYER_VICTORY)
        global new_player_victories
        new_player.bet_amount *= 2
        print(new_player.bet_amount)
        new_player.money += new_player.bet_amount
        print(new_player.money)
        new_player.bet_amount = 0
        print(new_player.bet_amount)
        new_player_victories += 1

    else:
        compare_value()

#Comparing Values
global compare_value
def compare_value():
    if new_player.value > new_dealer.value: #Player Wins
        if new_player.value == 21:
            new_player.bet_amount *= 2.5
            new_player.bet_amount %= 1
        else:
            new_player.bet_amount *= 2
        new_player.money += new_player.bet_amount
        new_player.bet_amount = 0
        global new_player_victories
        new_player_victories += 1
        print(CONSTANTS.PLAYER_VICTORY)
    elif new_player.value < new_dealer.value: #Dealer Wins
        new_player.bet_amount = 0
        global new_dealer_victories
        new_dealer_victories += 1
        print(CONSTANTS.DEALER_VICTORY)
    else: #Draw Scenarios
        if new_player.value == 21:
            if len(new_player.cards_in_hand) == 2 and len(new_dealer.cards_in_hand) != 2: #Player Wins
                new_player.bet_amount *= 2
                new_player.money += new_player.bet_amount
                new_player.bet_amount = 0
                new_player_victories += 1
                print(CONSTANTS.PLAYER_VICTORY)
            elif len(new_player.cards_in_hand) != 2 and len(new_dealer.cards_in_hand) == 2: #Dealer Wins
                    new_player.bet_amount = 0
                    new_dealer_victories += 1
                    print(CONSTANTS.DEALER_VICTORY)
            else: #Push
                new_player.money += new_player.bet_amount
                new_player.bet_amount = 0
                global pushes
                pushes += 1
                print(CONSTANTS.PUSH)
        else: #Push
                new_player.money += new_player.bet_amount
                new_player.bet_amount = 0
                pushes += 1
                print(CONSTANTS.PUSH)

#Replay
def replay():
    replay_input = input("Continue? (y/n)")
    if len(replay_input) == 0:
        print(CONSTANTS.EMPTY_INPUT_ERROR_MESSAGE)
    elif replay_input.lower() == "y":
        global gameplay
        gameplay()
    elif replay_input.lower() == "n":
        "Thank u 4 playing."
        exit()
    else:
        print(CONSTANTS.BAD_INPUT_ERROR_MESSAGE)
        replay()

#Cleaner
def cleaner():
    new_player.cards_in_hand.clear()
    new_dealer.cards_in_hand.clear()
    global new_deck
    new_deck = Classes.Deck()


##Gameplay
def gameplay():
    initial_deal()
    new_player_turn()
    cleaner()
    global turn
    turn += 1
    replay()

gameplay()