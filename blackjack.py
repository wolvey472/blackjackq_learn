# FIrst q learning project
# Black jack 
# Carson Shae

import random as rd

cards = ["spades", "clubs", "hearts", "diamonds"]

def draw_card():
    pl_cards = []
    dl_cards = []

    for i in range(4):
        num = rd.randint(1,10)
        if num == 1:
            num = str("ace")
        mod = rd.choice(cards)
        card = str(num) +" of " + mod
        print(card)
        
        if len(dl_cards) == 0 and len(pl_cards) == 0:
            pl_cards.append(card)
            continue
        if len(dl_cards) == 0 and len(pl_cards) == 1:
            dl_cards.append(card)
            continue
        if len(dl_cards) == 1 and len(pl_cards) == 1:
            pl_cards.append(card)
        else:
            dl_cards.append(card)
        

    print(dl_cards, pl_cards)
    score(dl_cards=dl_cards, pl_cards=pl_cards)
    return dl_cards, pl_cards

def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        rank = card.split(" ")[0]
        if rank == "ace":
            aces += 1
            total += 11
        else:
            total += int(rank)
    # demote aces from 11 to 1 while we are busted
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def score(dl_cards, pl_cards):
    dl_score = hand_total(dl_cards)
    pl_score = hand_total(pl_cards)
    print(pl_score, dl_score)
    return dl_score, pl_score

draw_card()
