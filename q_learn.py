# this could get bad...
#Q-Learning project black jack
# Carson Shae

# https://en.wikipedia.org/wiki/Q-learning
# https://medium.com/@goldengrisha/a-beginners-guide-to-q-learning-understanding-with-a-simple-gridworld-example-2b6736e7e2c9
# https://en.wikipedia.org/wiki/Markov_chain
# https://natureofcode.com/

import numpy as np
import pandas as pd
# why do i do this
# just pick one -> no ;)

import random as rd
from collections import defaultdict

from blackjack import draw_card, get_state, hand_total, step

EPISODES = 200_000
ALPHA = 0.5
GAMMA = 1.0
ACTIONS = ("hit", "stand")

def best_action(q_table, state):
    values = q_table[state]
    highest = max(values.values())
    tied_actions = [action for action in ACTIONS if values[action] == highest]
    return rd.choice(tied_actions)


def train(episodes=EPISODES):
    # A new state starts with two estimates: {"hit": 0.0, "stand": 0.0}.
    
    q_table = defaultdict(lambda: {"hit": 0.0, "stand": 0.0})

    for episode in range(episodes):
# this shows our exploration going down to 5%
        epsilon = max(0.05, 1.0 - episode / (episodes * 0.8))
        dl_cards, pl_cards = draw_card()
        state = get_state(dl_cards, pl_cards)
        done = False

        while not done:
            if rd.random() < epsilon:
                action = rd.choice(ACTIONS)  # Explore: try an action.
            else:
                action = best_action(q_table, state)  # Use what was learned.

            next_state, reward, done = step(dl_cards, pl_cards, action)
#no reward after hand is done
            if done:
                target = reward
            else:
                target = reward + GAMMA * max(q_table[next_state].values())

            old_value = q_table[state][action]
            q_table[state][action] += ALPHA * (target - old_value)
            state = next_state

        if (episode + 1) % 50_000 == 0:
            print(f"Trained on {episode + 1:,} games")

    return q_table

def evaluate(q_table, games=10_000):
    results = {"wins":0, "losses":0, "ties":0}

    for x in range(games):
        dl_cards, pl_cards = draw_card()
        state = get_state(dl_cards=dl_cards, pl_cards=pl_cards)
        done = False # could use is False
        while not done:
            action = best_action(q_table, state)
            state, reward, done = step(dl_cards, pl_cards, action)

        if reward == 1:
            results['wins'] += 1
        elif reward == -1:
            results['losses'] +=1
        else:
            results["ties"] += 1
    return results









