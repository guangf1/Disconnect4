# Adapted from Connect-4-Gym-env-Reinforcement-learning by Lucas Bertola with modifications
# Repository: https://github.com/lucasBertola/Connect-4-Gym-env-Reinforcement-learning

import numpy as np
from .Player import Player

class BabySmarterPlayer(Player):

    def __init__(self, _=""):
        pass

    def play_single(self,obs):
        valid_moves = [c for c in range(7) if obs[0, c] == 0]
        return np.random.choice(valid_moves)

    def play(self, observation):
        if isinstance(observation, list):
            return [self.play_single(obs) for obs in observation]
        else:
            return self.play_single(observation)

    def getName(self):
        return "BabySmarterPlayer"

    def getElo(self):
        return 1058

    def isDeterministic(self):
        return False