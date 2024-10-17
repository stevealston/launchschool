import random
import os
import time

PLAYER = {"name": 'player', "score": 0, "cards": [], "is_playing": True}
DEALER = {"name": 'dealer', "score": 0, "cards": []}

def prompt(msg):
    answer = input(f"==> {msg}").strip().lower()
    return answer

def initialize_deck():
    deck = []

    for suit in ['♥', '♠', '♣', '♦']:
        for i in range(2, 11):
            card = {}
            card["suit"] = suit
            card["type"] = f"{i}"
            card["value"] = i
            deck.append(card)
        for key in ['J', 'Q', 'K']:
            card = {}
            card["suit"] = suit
            card["type"] = key
            card["value"] = 10
            deck.append(card)

        card = {}
        card["suit"] = suit
        card["type"] = 'A'
        card["value"] = 11
        deck.append(card)

    return deck

def first_line_formatting(card):
    if len(card['type']) == 2:
        return f"│{card['type']}       │"

    return f"│{card['type']}        │"
    
def last_line_formatting(card):
    if len(card['type']) == 2:
        return f"│       {card['type']}│"

    return f"│        {card['type']}│"
    
def create_card(card):
    return [
        "┌─────────┐",
        first_line_formatting(card),
        "│         │",
        f"│    {card['suit']}    │",
        "│         │",
       last_line_formatting(card),
        "└─────────┘"
    ]

def create_blank_card():
    return [
        "┌─────────┐",
        "│         │",
        "│         │",
        "│         │",
        "│         │",
        "│         │",
        "└─────────┘"
    ]

def create_cards(user):
    cards = []
    for card in user["cards"]:
        cards.append(create_card(card))

    if user["name"] == 'dealer' and PLAYER["is_playing"]:
        cards[0] = create_blank_card()

    return cards

def display_scores(user):
    if user["name"] == 'player':
        print(f"===== {user['name'].capitalize()}" +
              f" has: {user['score']} =====")
    elif user["name"] == 'dealer' and not PLAYER["is_playing"]:
        print(f"===== {user['name'].capitalize()}" +
              f" has: {user['score']} =====")
    else:
        print(f"===== {user['name'].capitalize()} has: unknown =====")

def display_cards(*cards):
    num_lines = len(cards[0])    

    for i in range(num_lines):
        print(" ".join(card[i] for card in cards))

def display_hands():
    os.system('clear')

    display_scores(DEALER)
    display_cards(*create_cards(DEALER))
    display_scores(PLAYER)
    display_cards(*create_cards(PLAYER))
    print()

def initialize_game(deck):
    for _ in range(2):
        PLAYER["cards"].append(deal_card(deck))
        DEALER["cards"].append(deal_card(deck))    

def deal_card(deck):
    chosen_card = random.choice(deck)
    
    for card in deck:
        if (card["suit"] == chosen_card["suit"]
            and card["type"] == chosen_card["type"]
            and card["value"] == chosen_card["value"]):
            deck.remove(card)

    return chosen_card

def hit(deck, user):
    if user["name"] == 'player' and user["is_playing"]:
        PLAYER["cards"].append(deal_card(deck))
    else:
        DEALER["cards"].append(deal_card(deck))

    calculate_score(user)

def determine_ace_value(user, card):
    if user["score"] + 11 > 21:
        card["value"] = 1
    else:
        card["value"] = 11
    
    return card["value"]

def calculate_score(user):
    score = 0
    for card in user["cards"]:
        if card["type"] == 'A':
            card["value"] = determine_ace_value(user, card)
        score += card["value"]

    user["score"] = score
    return score

def determine_winner():
    if 21 - PLAYER["score"] < 21 - DEALER["score"]:
        print("===== YOU'RE A WINNER!!!! =====")
    elif 21 - PLAYER["score"] == 21 - DEALER["score"]:
        print("===== It's a DRAW =====")
    else:
        print("===== You LOSE!! =====")

def detect_bust(user):
    return user["score"] > 21

def reset_game():
    PLAYER["score"], DEALER["score"] = 0, 0
    PLAYER["cards"], DEALER["cards"] = [], []
    PLAYER["is_playing"] = True

def play_blackjack():
    # while True:
    while True:
        deck = initialize_deck()
        initialize_game(deck)
        calculate_score(PLAYER)
        calculate_score(DEALER)

        while True:
            display_hands()

            if detect_bust(DEALER):
                print()
                print("===== YOU'RE A WINNER!!!! =====")
                break
            
            if PLAYER["is_playing"]:
                answer = prompt('Hit or Stay? ')
                if answer == 'hit':
                    hit(deck, PLAYER)
                    calculate_score(PLAYER)
                    display_hands()
                else:
                    PLAYER["is_playing"] = False

                if detect_bust(PLAYER):
                    print()
                    print("===== YOU LOSE! =====")
                    break
      
            else:
                time.sleep(1)
                if DEALER["score"] < 17:
                    hit(deck, DEALER)
                else:
                    print()
                    determine_winner()
                    break
                time.sleep(2)


        play_again = prompt('Play Again? (y or n)')

        if play_again == 'n':
            break

        reset_game()


play_blackjack()
