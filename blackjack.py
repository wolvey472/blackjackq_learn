# FIrst q learning project
# Black jack 
# Carson Shae

import random as rd

cards = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "jack", "queen", "king"]



def draw_one_card():
  
    return rd.choice(ranks) + " of " + rd.choice(cards)


def draw_card():
    pl_cards = []
    dl_cards = []

    for i in range(2):
        pl_cards.append(draw_one_card())
        dl_cards.append(draw_one_card())
    
    return dl_cards, pl_cards

def hand_details(hand):
    total = 0
    aces = 0
    for card in hand:
        rank = card.split(" ")[0]
        if rank == "ace":
            aces += 1
            total += 11
        elif rank in ("jack", "queen", "king"):
            total += 10
        else:
            total += int(rank)
    # demote aces from 11 to 1 while we are busted
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
       
    return total, aces > 0
# check return

def hand_total(hand):
    return hand_details(hand)[0]

def score(dl_cards, pl_cards):
    dl_score = hand_details(dl_cards)
    pl_score = hand_details(pl_cards)
    print("player: ", pl_score)
    print("dealer: ", dl_score)

    return dl_score, pl_score


def get_state(dl_cards, pl_cards):
    
    player_total, usable_ace = hand_details(pl_cards)
    dealer_upcard = hand_total([dl_cards[0]])
    return player_total, dealer_upcard, usable_ace


def step(dl_cards, pl_cards, action):

    if action == "hit":
        pl_cards.append(draw_one_card())
        if hand_total(pl_cards) > 21:
            return get_state(dl_cards, pl_cards), -1, True
        return get_state(dl_cards, pl_cards), 0, False

    if action != "stand":
        raise ValueError("Action must be 'hit' or 'stand'.")

    while hand_total(dl_cards) < 17:
        dl_cards.append(draw_one_card())

    dealer_total = hand_total(dl_cards)
    player_total = hand_total(pl_cards)
    if dealer_total > 21 or player_total > dealer_total:
        reward = 1
    elif player_total < dealer_total:
        reward = -1
    else:
        reward = 0
    return get_state(dl_cards, pl_cards), reward, True


if __name__ == "__main__":
    # This runs only when you run blackjack.py directly, not when importing it.
    dealer, player = draw_card()
    print("Player cards:", player)
    print("Dealer cards:", dealer)
    score(dealer, player)

