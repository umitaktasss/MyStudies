import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)


# random pick of card from a deck

def deal_cards():
    """ Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# add up the score for both user and computer

def calculate_score(cards):
    """ return the score calculated from the cards and checks for multiple rules need to be followed """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# comparing user score and computer score

def compare(user_score, computer_score):
    """comparison between user and computer scores"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "draw"
    elif user_score == 0:
        return "win with a blackjack"
    elif computer_score == 0:
        return "you lose as opponent has blackjack"
    elif user_score > 21:
        return "you lose as score is above 21"
    elif computer_score > 21:
        return "you win as opponent went ahead"
    elif user_score > computer_score:
        return 'you win as your score is high'
    else:
        return "you lose"


def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to deal another card? Type y or n: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    # computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while True:
    play_game()
    play_again = input("Do you want to play again? Type y or n: ")
    if play_again != "y":
        print("Bye!")
        break
