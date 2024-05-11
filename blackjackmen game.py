import random

def create_deck():
    """Create a deck of cards"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_total(hand):
    """Calculate the total value of a hand"""
    total = 0
    ace_count = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            total += 10
        elif card['rank'] == 'Ace':
            total += 11
            ace_count += 1
        else:
            total += int(card['rank'])
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

def display_hand(hand):
    """Display a hand of cards"""
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

def play_blackjack():
    """Play a game of blackjack"""
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # ASCII art title
    print("""
   ____  _            _        _            _
 |  _ \| |          | |      (_)          | |
 | |_) | | __ _  ___| | __    _  __ _  ___| | ___ __ ___   __ _ _ __
 |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ / '_ ` _ \ / _` | '_ \
 | |_) | | (_| | (__|   <    | | (_| | (__|   <| | | | | | (_| | | | |
 |____/|_|\__,_|\___|_|\_\   | |\__,_|\___|_|\_\_| |_| |_|\__,_|_| |_|
                            _/ |
                           |__/


    """)

    print("Your hand:")
    display_hand(player_hand)
    print("\nDealer's hand:")
    print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
    print("Hidden card")

    player_total = calculate_total(player_hand)

    while player_total < 21:
        action = input("\nDo you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print("\nYour new hand:")
            display_hand(player_hand)
            player_total = calculate_total(player_hand)
            if player_total > 21:
                print("\nBusted! You lose.")
                return
        elif action == 's':
            break

    dealer_total = calculate_total(dealer_hand)
    print("\nDealer's hand:")
    display_hand(dealer_hand)
    print(f"\nDealer's total: {dealer_total}")

    while dealer_total < 17:
        dealer_hand.append(deck.pop())
        dealer_total = calculate_total(dealer_hand)
        print("\nDealer hits.")
        print("\nDealer's new hand:")
        display_hand(dealer_hand)
        print(f"\nDealer's total: {dealer_total}")

    if dealer_total > 21 or player_total > dealer_total:
        print("\nCongratulations! You win.")
    elif dealer_total > player_total:
        print("\nDealer wins.")
    else:
        print("\nIt's a tie.")

play_blackjack()
