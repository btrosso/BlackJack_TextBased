import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


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
        return sum(hand)


user_cards.append(deal_card())
user_cards.append(deal_card())
# print(user_cards)

computer_cards.append(deal_card())
computer_cards.append(deal_card())

# print(calculate_score(user_cards))
