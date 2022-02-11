import random
import os
from art import logo


def game():
    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    def deal_card():
        dealt_card = random.choice(cards)
        return dealt_card

    # calculate hand score
    def calculate_score(hand):

        # if blackjack return 0, 0 will represent blackjack
        if len(hand) == 2 and sum(hand) == 21:
            sum_cards = 0
            return sum_cards
        # else return actual sum
        else:
            sum_cards = sum(hand)
            if 11 in hand and sum_cards > 21:
                hand.remove(11)
                hand.append(1)
                sum_cards = sum(hand)
                # test code
                # print(hand)
            return sum_cards

    def compare(u_score, c_score):
        if u_score == c_score:
            print("It's a PUSH.")
        elif c_score == 0:
            print("You Lose.")
        elif user_score == 0:
            print("YOU WIN!")
        elif user_score > 21:
            print("You Lose.")
        elif c_score > 21:
            print("YOU WIN!")
        else:
            if user_score > c_score:
                print("YOU WIN!")
            elif user_score < c_score:
                print("You Lose.")

    # test code
    # user_cards.append(11)
    # user_cards.append(12)

    # deal user cards
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    # test code
    # print(user_cards)

    # deal comp cards
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    # test code
    # print(calculate_score(user_cards))

    # users turn
    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your hand: {user_cards}, current_score: {user_score}")
        print(f"Computer's first care: {computer_cards[0]}")
        if computer_score == 21 or user_score == 21:
            game_over = True
        elif user_score > 21:
            game_over = True

        # if game has not ended ask user if they want to draw
        hit = input("Type 'y' to draw another card or type 'n' to pass: ").lower()
        if hit == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True

    # computers turn
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(u_score=user_score, c_score=computer_score)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("If score is '0' that means black jack. ")

    restart = input("Would you like to restart the game? Type 'y' or 'n': ").lower()
    if restart == 'y':
        os.system("clear")
        game()


game()
