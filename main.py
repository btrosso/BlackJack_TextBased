import random


# from art import logo

# ############### Our Blackjack House Rules #####################
#
# ## The deck is unlimited in size.
# ## There are no jokers.
# ## The Jack/Queen/King all count as 10.
# ## The the Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
# ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn.
# ## Cards are not removed from the deck as they are drawn.
# ## The computer is the dealer.

def game():
    def get_current_score(hand):
        score = 0
        for card in hand:
            score += card
        return score

    def play_again():
        user_response = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
        if user_response == 'y':
            return True
        else:
            return False

    def declare_winner():
        print(f"Your final hand: {user_hand}, final score: {user_hand_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_hand_score}")
        if winner:
            print("YOU WIN!")
        elif push:
            print("It's a push.")
        elif not winner and game_over:
            print("You Lose.")

    def view_current_hand():
        print(f"Your cards: {user_hand}, current score: {user_hand_score}")
        print(f"Computer's first card: {computer_hand[0]}")

    def hit():
        user_hand.append(random.choice(cards))

    def computer_hit(score, game_over):
        if score < 17:
            computer_hand.append(random.choice(cards))
        else:
            return

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = [random.choice(cards), random.choice(cards)]
    user_hand_score = get_current_score(user_hand)
    computer_hand = [random.choice(cards), random.choice(cards)]
    computer_hand_score = get_current_score(computer_hand)
    play = play_again()
    winner = False
    game_over = False
    push = False

    # print(logo)
    while play:

        view_current_hand()

        if user_hand_score == 21 or computer_hand_score > 21:
            winner = True
            game_over = True
        elif computer_hand_score == 21 or user_hand_score > 21:
            winner = False
            game_over = True
        elif user_hand_score == computer_hand_score:
            push = True
            game_over = True

        if game_over:
            declare_winner()
            play = play_again()
            if play:
                game()
        else:
            hit_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_choice == 'y':
                hit()
                user_hand_score = get_current_score(user_hand)

            computer_hit(score=computer_hand_score)
            computer_hand_score = get_current_score(computer_hand)
            if computer_hand_score >= 17:
                game_over = False


game()

