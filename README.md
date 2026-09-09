# Blackjack with Q-Learning

**Author: Carson Shae**  
**My first Q-learning project**

This project combines a Python blackjack game with a Q-learning agent that learns when to hit or stand through repeated games. The project explores how the learning rate and number of training episodes affect the agent's performance.

## Project files

| File | Purpose |
| --- | --- |
| `blackjack.py` | My original blackjack code. Defines the cards, deals the opening hands, and calculates hand totals. |
| `q_learn.py` | Imports the original game functions and adds hit/stand actions, rewards, training, and evaluation. |
| `README.md` | Project explanation, running instructions, and experiment findings. |

This README uses `q_learn.py` as the learner's filename. If your copy is named `q_learning.py`, use that filename in the run command instead.

The original blackjack code can stay unchanged. The learning script reuses `draw_card()` and `hand_total()` and hides repeated game printouts during training.

## How to run

Python 3 is required. The project uses only Python's standard library, so no extra packages need to be installed.

1. Put the original `blackjack.py` and the learning script in the same folder.
2. Open a terminal in that folder.
3. Run the learning script:

```bash
python q_learn.py
```

If the learner is named `q_learning.py`, run `python q_learning.py` instead. If the original game has a different filename, update `blackjack` in the learner's import statement to match it, without the `.py` extension.

By default, the script trains on 200,000 games, evaluates the agent on 10,000 freshly dealt games, and shows three example games. Each run starts with a fresh Q-table; the learned values are not automatically saved between runs.

## Blackjack rules used

- The player can hit or stand.
- Number cards use their face value. Jacks, queens, and kings count as 10.
- Aces count as 11 unless they need to count as 1 to prevent a bust.
- The dealer hits below 17 and stands on every 17, including a soft 17.
- A player bust ends the round immediately with a loss.
- Cards are drawn with replacement, so the same card can appear more than once.
- All wins receive the same reward. This version has no special two-card blackjack payout, splitting, or doubling down.

## How Q-learning works

The agent keeps a Q-table with an estimated value for hitting and standing in each situation. During training, it tries actions, observes the results, and updates those estimates.

The agent's **state** contains three values:

| State value | Meaning |
| --- | --- |
| Player total | The current value of the player's hand. |
| Dealer's visible card | The value of the dealer's first card; an ace is represented as 11. |
| Usable ace | Whether the player has an ace currently counting as 11. |

For example, `(16, 10, False)` means the player has 16, the dealer shows a 10-value card, and the player has no usable ace. The dealer's hidden card is excluded from the state.

The available actions are `hit` and `stand`. The final rewards are:

| Result | Reward |
| --- | --- |
| Win | `+1` |
| Loss | `-1` |
| Tie | `0` |

A hit that does not bust also returns `0` while the round continues. The `done` value tells the learner whether the round has ended.

During training, the agent sometimes chooses randomly to explore. Otherwise, it chooses the action with the highest Q-value. When both actions have the same value, it breaks the tie randomly.

## Training settings

These are the starting settings in the learning script. Change `ALPHA` and `EPISODES` near the top of the file to run experiments.

```python
EPISODES = 200_000
ALPHA = 0.05
GAMMA = 1.0
```

| Setting | Meaning |
| --- | --- |
| `ALPHA` | Learning rate: how strongly each new target changes an existing Q-value. Larger values make bigger updates; smaller values make smaller updates. |
| `EPISODES` | Number of complete games used for training. More episodes give the agent more experience. |
| `GAMMA` | Discount factor for future rewards. A value of `1.0` keeps the full value of the eventual reward. |
| `epsilon` | Chance of choosing a random action during training. It starts at `1.0` and decreases to a minimum of `0.05`. |

## Understanding the test results

The message **"Results from 10,000 NEW games (learning switched off)"** marks the evaluation stage.

The agent uses its learned Q-values to play freshly dealt games. It stops updating those values and stops deliberately choosing random actions for exploration. Ties between equal Q-values are still broken randomly.

The printed wins, losses, and ties measure the performance of the strategy learned during that run.

## My experiments and findings

For comparisons, change one setting at a time, keep the evaluation at 10,000 games, and repeat settings across several runs. Random deals and exploration can cause results to vary between runs.

### Learning rate (`ALPHA`)

**Training episodes kept constant:** _Add the episode count here._

| Trial | Learning rate | Win % | Loss % | Tie % | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

**What I found:**

_Write what happened when you used smaller and larger learning rates. Describe which results were consistent across runs and which varied._

**Learning rate I would use again and why:**

_Add your choice and explanation here._

### Training episodes (`EPISODES`)

**Learning rate kept constant:** _Add the learning rate here._

| Trial | Training episodes | Win % | Loss % | Tie % | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

**What I found:**

_Write how performance changed with fewer or more training games. Note whether extra training continued to help, gave similar results, or produced mixed results._

**Episode count I would use again and why:**

_Add your choice and explanation here._

### Overall conclusion

**Chosen learning rate:** _Add value._  
**Chosen episode count:** _Add value._

_Explain what these experiments taught you about Q-learning and what you would try next._
