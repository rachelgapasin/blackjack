import os
import random
from art import logo

def clear():
  os.system('clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards_list):
    score = sum(cards_list)
    if len(cards_list) == 2 and score == 21:
        return 0
    if 11 in cards_list and score > 21:
        ace = cards_list.index(11)
        cards_list[ace] = 1
        score = sum(cards_list)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "😱 It's a draw. 😱"
    elif user_score == 0:
        return "🥳 Blackjack! You win! 🥳"
    elif computer_score == 0:
        return "😔 Opponent has Blackjack. You lose. 😔"
    elif user_score > 21:
        return "😔 You went over. You lose. 😔"
    elif computer_score > 21:
        return "🥳 Computer went over. You win! 🥳"
    elif user_score > computer_score:
        return "🥳 You win! 🥳"
    else:
        return "😔 Computer wins. 😔"

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    continue_game = True
    while continue_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        formatted_user_score = user_score
        if user_score == 0:
          formatted_user_score = 21
        print(f"\nYour cards: {user_cards}, current score: {formatted_user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_game = False
        else:
            draw_card = input(
                "\nType 'y' to get another card, type 'n' to pass: ").lower()
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                continue_game = False
                while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

    score = compare(user_score, computer_score)
    if user_score == 0: user_score = 21
    if computer_score == 0: computer_score = 21
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}\n"
    )
    print(f"            {score}")

    print("-------------------------------------------------------- ")

while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
