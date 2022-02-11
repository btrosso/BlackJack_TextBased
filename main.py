import random
import os
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """
    Returns a random card from the deck
    :return card:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_card = random.choice(cards)
    return dealt_card


def calculate_score(cards):
    """
    Takes a list of cards and returns the score calculated from the cards.
    :param cards:
    :return score:
    """
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a PUSH."
    elif computer_score == 0:
        return "You Lose. Opponent has BlackJack."
    elif user_score == 0:
        return "YOU WIN! You got BlackJack."
    elif user_score > 21:
        return "You Lose. You went over 21."
    elif computer_score > 21:
        return "YOU WIN! Opponent went over 21."
    elif user_score > computer_score:
        return "YOU WIN!"
    else:
        return "You Lose."


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
