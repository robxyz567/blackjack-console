import random
from art import logo
from help import rules

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():

    return random.choice(CARDS)


def calculate_score(list_of_cards):

    score = sum(list_of_cards)
    if score == 21:
        return score
    for card in list_of_cards:
        if card == 11:
            if score > 21:
                list_of_cards.remove(11)
                list_of_cards.append(1)
                score = sum(list_of_cards)
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

    print(f"\nYour cards values: {user_cards}")

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while user_drawing:

        wanna_draw = input("Do you want draw another card? If yes type y, if not type n: ")

        if wanna_draw == 'y':
            user_cards.append(draw_card())
            print(f"Your cards values: {user_cards}")
        else:
            user_drawing = False

        user_score = calculate_score(user_cards)

    while computer_score < 17:

        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    choose_winner(user_score, computer_score)
    print(f"Computer cards values: {computer_cards}:")

    wanna_play_again = input("\nWanna play again? If yes type 'y', if not type n: ")
    if wanna_play_again == 'y':
        game()


print(logo)

user_choice_1 = input("Welcome to BlackJack Game."
                      "\nIf you want to read about the rules, type 'help'."
                      "If you are ready to play the game, type 'y': ")
if user_choice_1 == 'help':
    print(rules)
    user_choice_2 = input("We start? If yes type 'y': ")
    if user_choice_2 == 'y':
        game()
elif user_choice_1 == 'y':
    game()
