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
    return dl_cards, pl_cards
       

draw_card()