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

## My findings


**DISCLAIMER:**
 - I'm 17 -> i cant gamble
 - im also not a mathmetician, data scientist, or gambling expert
 - just a kid who likes to code
 - this project is for learning not gambling advice

 i'm self taught in python and am fascinated by how Python and machine learning can help us explore the way AI learns and expand how we, as humans, understand the world. 
 
 Thats all just a kid with a passion and some free time :)


### Experiment 1 
---
what does a lower learning rate (alpha) yield?

`q_value = old_q_value + learning_rate * (target - old_q_value)`

Each iteration is trained fresh on 1 million hands of black jack \
The results showed are after training each with 10,000 hands \
Learning rate (alpha) starts at 0.01 and is divided by 10 each iteration

| Learning Rate | Win | Loss | Tie |
| --- | --- | --- | --- |
| 0.01 | 4,287 | 4,700 | 1,013 |
| 0.001 | 4,300 | 4,806 | 894 |
| 0.0001 | 4,075 | 5,048 | 877 |
| 1e-05 | 4,263 | 4,894 | 843 |
| 1e-06 | 4,258 | 4,907 | 835 |
| 1e-07 | 4,148 | 4,992 | 860 |
| 1e-08 | 4,163 | 4,991 | 846 |
| 1e-09 | 4,140 | 4,932 | 928 |
| 1e-10 | 4,179 | 5,009 | 812 |
| 1e-11 | 4,241 | 4,916 | 843 |

**Conclusion**
---
- 0.001 had the highest win rate at 43%
- 0.01 had the fewest losses at 47%
However overall a lower learning rate did not yield better results in general -> I belive the cause of this is that a very small learning rate is too slow for the number of training games provided.

### Experiment 2
---
can more training examples yield a better result?

| Learning rate | Episodes | Win | Loss | Tie |
| --- | --- | --- | --- | --- |
| 0.01 | 200,000 | 4,235 | 4,807 | 958 |
| 0.01 | 300,000 | 4,271 | 4,798 | 931 |
| 0.01 | 400,000 | 4,315 | 4,737 | 948 |
| 0.01 | 500,000 | 4,234 | 4,822 | 944 |
| 0.01 | 600,000 | 4,331 | 4,740 | 929 |
| 0.01 | 700,000 | 4,255 | 4,813 | 932 |
| 0.01 | 800,000 | 4,280 | 4,777 | 943 |
| 0.01 | 900,000 | 4,345 | 4,786 | 869 |
| 0.01 | 1,000,000 | 4,254 | 4,854 | 892 |
| 0.001 | 1,100,000 | 4,214 | 4,952 | 834 |
| 0.001 | 1,200,000 | 4,173 | 4,888 | 939 |
| 0.001 | 1,300,000 | 4,226 | 4,939 | 835 |
| 0.001 | 1,400,000 | 4,319 | 4,877 | 804 |
| 0.001 | 1,500,000 | 4,255 | 4,880 | 865 |
| 0.001 | 1,600,000 | 4,195 | 4,904 | 901 |
| 0.001 | 1,700,000 | 4,194 | 4,985 | 821 |
| 0.001 | 1,800,000 | 4,230 | 4,878 | 892 |
| 0.001 | 1,900,000 | 4,189 | 4,917 | 894 |

**Conclusion**
---
After training on up to 1.9 million games, the agent settled at about 42% wins, 48% losses, and 9% ties. Training longer than 200,000 games didn't help and the higher learning rate (0.01) did slightly better than 0.001. The agent learned to play blackjack well but even perfect play still loses to the house over time :(



## Overall Conclusion
---
My experiments showed that a small learning rate and more training do not automatically produce better results. Most runs finished with win rates around 41–43%. In Experiment 1, 0.001 had the highest win rate, but 0.01 had fewer losses and more ties. Since my agent earns +1 for wins, −1 for losses, and 0 for ties, 0.01 actually earned the better total reward. 
Experiment 2 showed no consistent improvement as training increased. However, I also changed the learning rate from 0.01 to 0.001 after one million episodes, so I cannot separate the effect of more training from the effect of that change. Very small learning rates might slow learning too much, but these results alone do not prove that explanation.

This connects to Charles de Granville’s paper, Applying Reinforcement Learning to Blackjack Using Q-Learning, which states:

“the learning agent performed considerably better than random, and converged to a near optimal policy.”


And again this should not be taken as gambling advice as we saw in the result no experiment came close to becoming profitable over 10,000 hands

The broader lesson is that AI performance depends on the settings, available information, and rules of its environment not just how long it trains.

For my first Q-learning project, the biggest takeaway is that teaching a computer to make decisions is only half the challenge. Figuring out whether those decisions actually improved is the other half. 🙂


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


**Chosen episode count:** _Add value._

_Explain what these experiments taught you about Q-learning and what you would try next._
