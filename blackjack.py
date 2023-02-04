# Joe Goodman
# 02/03/23
# black jack card game

"""
questions
1. does import really need to be first line
"""

from p1_random import P1Random

# helper function to make custom error messages
# this makes debugging easier
def error(msg):
    raise Exception(msg)

# maps the numbers 1-13 inclusive
# to Cards which have name and a point_value
#
# this class expects to be treated nicely!
# do not pass it unchecked input!
class Card:
    def __init__(self, number):
        # number is the point value, unless it is >10, then it's just 10
        self.point_value = number if number <= 10 else 10

        # map the number to a card name
        # 1 is an ACE
        # for numbers >1 but <=10, the name and the number are the same
        # 11, 12, and 13 are mapped to JACK, QUEEN, and KING
        name = None
        if number == 1:
            name = "ACE"
        elif number <= 10:
            name = str(number)
        elif number == 11:
            name = "JACK"
        elif number == 12:
            name = "QUEEN"
        elif number == 13:
            name = "KING"
        else:
            error("unreachable!")

        # this will never be None as name is either assigned to or
        # an Excpetion is raised
        self.name = name

def main():
    # global values to track
    playing = True

    # number of games played
    game_number = 1

    # number of player wins
    player_wins = 0

    # number of dealer wins
    dealer_wins = 0
    
    # number of ties
    ties = 0

    while playing:
        # print the game number and menu
        print_game_number(game_number)
        print_menu()

        # ask the user which option they would like to select
        user_input = get_checked_user_input("Choose an option: ")

        # determine what to do based on the users input
        if user_input == 1:
            # give the player another card
            pass
        elif user_input == 2:
            # dealers turn and decide winner
            pass
        elif user_input == 3:
            # print game stats
            pass
        elif user_input == 4:
            playing = False
        else:
            error("unreachable!")

# get input from the user and ensure that it is valid
# this function will reject any input that is not "1", "2", "3", or "4"
# it will loop forever or until it gets valid input
def get_checked_user_input(msg):
    # a list of all valid inputs
    valid_inputs = ["1", "2", "3", "4"]
    while True:
        # get input from the user
        user_input = input(msg)

        # if it is valid, return the input as an int
        if user_input in valid_inputs:
            return int(user_input)

        # otherwise, let the user know to try again
        else:
            print("Invalid input!") 
            print("Please enter an integer value between 1 and 4.") 

# print the game number
def print_game_number(game_number):
    print(f"START GAME #{game_number}")

# print the menu
def print_menu():
    print("1. Get another card") 
    print("2. Hold hand") 
    print("3. Print statistics") 
    print("4. Exit")

if __name__ == "__main__":
    main()

