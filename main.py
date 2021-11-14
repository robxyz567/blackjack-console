import random
from help import rules

CARDS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
LOGO_NAME = "BLACKJACK"
LOGO_LETTERS = []
for LETTER in LOGO_NAME:
    LOGO_LETTERS.append(LETTER)


def print_cards(list_of_cards):

    to_print = []
    for card in list_of_cards:
        if card == 10:
            to_print.append(f"|{card}  | ")
        else:
            to_print.append(f"|{card}   | ")
    nr = len(list_of_cards)
    print(nr * " ____  ")
    print("".join(to_print))
    print(nr * "| %$ | ")
    print(nr * "|____| ")


def draw_card():

    return random.choice(CARDS)


def calculate_score(list_of_cards):

    list_of_values = list_of_cards.copy()
    for i in range(len(list_of_values)):
        if list_of_values[i] == 'A':
            list_of_values[i] = 11
        elif list_of_values[i] == 'J' or 'Q' or 'K':
            list_of_values[i] = 10

    score = sum(list_of_values)
    if score == 21:
        return score
    for i in range(len(list_of_values)):
        if list_of_values[i] == 11:
            if score > 21:
                list_of_values[i] = 1
                score = sum(list_of_values)
    return score


def choose_winner(user_score, computer_score):

    if computer_score == 21:
        print("\nYou lose!")
    elif user_score == 21:
        print("\nYou win!")
    elif user_score > 21:
        print("\nYou lose!")
    elif computer_score > 21:
        print("\nYou win!")
    elif user_score == computer_score:
        print("\nDraw!")
    else:
        if user_score > computer_score:
            print("\nYou win!")
        else:
            print("\nYou lose!")


def game():

    user_drawing = True

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    print("Your cards:")
    print_cards(user_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while user_drawing:

        wanna_draw = input("Do you want draw another card? If yes type y, if not type n: ")

        if wanna_draw == 'y':
            user_cards.append(draw_card())
            print("Your cards:")
            print_cards(user_cards)
        else:
            user_drawing = False

        user_score = calculate_score(user_cards)

    while computer_score < 17:              # The computer's game strategy is that it only draws cards
                                            # if the sum of its cards is less than 17
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    choose_winner(user_score, computer_score)
    print("Computer cards:")
    print_cards(computer_cards)

    wanna_play_again = input("\nWanna play again? If yes type 'y', if not type n: ")
    if wanna_play_again == 'y':
        game()


print_cards(LOGO_LETTERS)

user_choice_1 = input("\nWelcome to BlackJack Game!"
                      "\nIf you want to read about the rules, type 'help'. "
                      "\nIf you are ready to play the game, type 'y': "
                      "\nYour choice: ")

if user_choice_1 == 'help':
    print(rules)
    user_choice_2 = input("Can we start? If yes type 'y': ")
    if user_choice_2 == 'y':
        game()
elif user_choice_1 == 'y':
    game()
