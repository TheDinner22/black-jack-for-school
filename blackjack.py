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

# represents a player which has a hand 
# which is an array of Cards
#
# has methods for:
# adding to the hand
# determining total number of points
# and clearing the hand
#
# this class expects to be treated nicely!
# do not pass it unchecked input!
class Player:
    def __init__(self):
        self.hand = []

    # takes the number and attempts to create a Card from that number
    # then appends that Card to the players hand
    # will throw an error if a Card cannot be created from the number
    #
    # every time a card is added to the players hand,
    # we need to print the cards name and their total points
    # this function also prints the new card's name and the players new total
    def add_to_hand(self, number):
        # create card and add to hand
        card = Card(number)
        self.hand.append(card)

        # print card name and player's points
        print(f"Your card is a {card.name}!")
        print(f"Your hand is: {self.points()}")
        print("")

    # calculates how many points the player has in
    # their hand
    def points(self):
        counter = 0
        for card in self.hand:
            counter += card.point_value
        return counter

    # clear the players hand
    def clear_hand(self):
        self.hand = []

def main():
    # flag which indicates whether or not to terminate the program
    done = False

    # number of games played
    game_number = 0

    # number of player wins
    player_wins = 0

    # number of dealer wins
    dealer_wins = 0
    
    # number of ties
    ties = 0

    # random number generator to be used throughout the program
    rng = P1Random()

    # create the player
    player = Player();

    # every iteration of this loop represents an entire game
    while not done:
        # increment the game number
        game_number += 1
        # clear the players hand

        player.clear_hand()

        # flag which indicates whether or not the game is over
        game_over = False

        # print the game number
        print_game_number(game_number)

        # draw the player their first card
        rand_int = rng.next_int(13) + 1
        player.add_to_hand(rand_int)

        # every iteration of this loop represents one turn in a game
        while not game_over:
            # print the menu
            print_menu()

            # ask the user which option they would like to select
            user_input = get_checked_user_input("Choose an option: ")
            print("")

            # determine what to do based on the users input
            if user_input == 1:
                # give the player another card
                rand_int = rng.next_int(13) + 1
                player.add_to_hand(rand_int)
                # check for blackjack
                if player.points() == 21:
                    print("BLACKJACK! You win!")
                    player_wins += 1
                    game_over = True
                    
                #check for bust
                elif player.points() > 21:
                    print("You exceeded 21! You lose.")
                    dealer_wins += 1
                    game_over = True

            # dealers turn and decide winner
            elif user_input == 2:
                # determine the dealers hand
                dealer_points = rng.next_int(11) + 16
                # print the dealers hand and the players hand
                print(f"Dealer's hand: {dealer_points}")
                print(f"Your hand is: {player.points()}")
                print("")

                # is the dealer bust? then the player wins
                if dealer_points > 21:
                    print("You win!")
                    player_wins += 1
                    game_over = True

                # is it a tie?
                elif dealer_points == player.points():
                    print("It's a tie! No one wins!")
                    ties += 1
                    game_over = True

                # did the dealer win?
                elif dealer_points > player.points():
                    print("Dealer wins!")
                    dealer_wins += 1
                    game_over = True

                # if none of the above were true, we know the player won
                else:
                    print("You win!")
                    player_wins += 1
                    game_over = True

            elif user_input == 3:
                # print game stats
                print_game_stats(player_wins, dealer_wins, ties, game_number)
            elif user_input == 4:
                # exit the loop, kills the program
                done = True
                game_over = True
                continue
            else:
                error("unreachable!")

        # only here for formatting
        print("")

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
            print("")
            print("Invalid input!") 
            print("Please enter an integer value between 1 and 4.") 
            print("")

# print the game number
def print_game_number(game_number):
    print(f"START GAME #{game_number}")
    print("")

# print the menu
def print_menu():
    print("1. Get another card") 
    print("2. Hold hand") 
    print("3. Print statistics") 
    print("4. Exit")
    print("")

# print the stats of the game
def print_game_stats(player_wins, dealer_wins, ties, game_number):
    # compute % of player wins and round to one decimal place
    player_wins_percent = round((player_wins / game_number) * 100, 1)

    # print stats
    print(f"Number of Player wins: {player_wins}")
    print(f"Number of Dealer wins: {dealer_wins}")
    print(f"Number of tie games: {ties}")
    print(f"Total # of games played is: {game_number - 1}")
    print(f"Percentage of Player wins: {player_wins_percent}%")

if __name__ == "__main__":
    main()

