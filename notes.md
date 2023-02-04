# starting the program

1. when the program is started, "START GAME #1" should be printed on the console
2. the player should automatically be dealt their first card

> each game should start with "START GAME #1" printed to the console 
> NOTE: adjust game number as needed

# how to "randomly " draw cards

1. Generate a number between 1 and 13 (inclusive)
2. there is a mapping between numbers and cards
    - 1 is an ace
    - 2-10 (inclusive) are the numbered cards
    - 11 is the jack
    - 12 is the queen
    - 13 is the king

# card point values

Same as in regular blackjack except that aces are only ever worth one point.

# announcing dealt cards WIP

Whenever a card is dealt, print the cards name and the total number of points in that player's hand

For example, when dealt a king the stdout would read: "Your card is a KING!"
For example, when dealt a number card (2-10) with the number, n, the stdout would read: "Your card is an!"

# printing the menu after a card is dealt

after the first card is dealt, print the menu. The menu looks like this:

1. Get another card 
2. Hold hand 
3. Print statistics 
4. Exit

# what happens if the player picks an option from the menu

## get another card

If option one is chosen the player gets dealt another card.

- If that card increases their total to 21, they win and print "BLACKJACK! You win!" to the stdout
- If that card puts the player over 21, they lose and print "You exceeded 21! You lose."

> in either case, a new game is started afterwards

## Hold hand

If this option is selected, it becomes the dealer's turn.

> #### dealer logic
> 
> To determine the dealers hand:
> 
> 1. generate a number between [16, 26] 
> 2. this number is the dealers point value

### determining a winner
if the dealer's hand is above 21, the player wins
- if the dealer and the player have equal point values, it's a tie and print "It's a tie! No one wins!"
- if neither of the above applies, whoever has the most points wins
    - if the player wins print "You win!"
    - if the dealer wins print "Dealer wins!"

> after a winner or tie is annocuned, start a new game

## print statistics 

This will print game stats

You should be tracking:

1. number of games played
2. number of players wins
3. number of dealer wins
4. number of ties

This option should print all of that and the % of games won by the player to all games played

sample output:

Number of Player wins: 2
Number of Dealer wins: 2
Number of tie games: 1
Total # of games played is: 5
Percentage of Player wins: 40.0%

## Exit

If this is selected exit the program

# invalid menu input

It is safe to assume that all input from the input function in this project will nicely parse to int.
HOWEVER, we do not know if that int is in [1, 4]. It could be 32423429 for all I know.

if an int is input that != 1-4, then print this:

Invalid input! 
Please enter an integer value between 1 and 4. 

then reprint the menu

# Random numbers!

they want me to use some random number that they made and its a class

see the page on how to do that

