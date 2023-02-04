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
        # for numbers <=10, the name and the number are the same
        # 11, 12, and 13 are mapped to JACK, QUEEN, and KING
        name = None
        if number <= 10:
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
    pass

if __name__ == "__main__":
    main()
