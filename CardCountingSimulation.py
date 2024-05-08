import random

def create_deck(num_decks):
    """Create a deck of cards with the specified number of decks."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for _ in range(num_decks) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Return the value of a single card."""
    if card['value'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['value'] == 'Ace':
        return 11
    else:
        return int(card['value'])

def hand_value(hand):
    """Return the total value of a hand of cards."""
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['value'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def count_cards(card, count):
    """Update the card counting based on the drawn card."""
    if card['value'] in ['2', '3', '4', '5', '6']:
        count += 1
    elif card['value'] in ['10', 'Jack', 'Queen', 'King', 'Ace']:
        count -= 1
    return count

def play_blackjack():
    """Play a game of blackjack with card counting."""
    sum_trues = 0
    for x in range(500):
        shoe = create_deck(2)
        count = 0
        max = 0
        true = 0
        tc = 0
        while len(shoe) > 52:  # determine when to reshuffle deck once specified number of cards remain
            card = shoe.pop(0)
            count = count_cards(card, count)
            tc = count/(len(shoe)/52)
            if count > max:
                max = count
                true = max/(len(shoe)/52)
            if len(shoe) == 52:
                sum_trues += true
            if len(shoe) < 52:
                shoe = create_deck(2)
            print(f"Card: {card['value']} of {card['suit']}, Count: {count}, True Count: {tc}, Max True Count: {true}")
    print("Average Highest True Count for 500 different shoes ", sum_trues/500)    

# Simulate card counting for 500 shoes
play_blackjack()
