import Classes
import CONSTANTS


def bet_input():
    money_wagered = 0
    while True:
        try:
            money_wagered = input("Please input the amount of money you would like to bet.")
            if int(money_wagered) <= Classes.PlayerBet.money:
                money_wagered = int(money_wagered)
                return money_wagered
        except:
            return CONSTANTS.BAD_INPUT_ERROR_MESSAGE