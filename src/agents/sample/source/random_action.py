import random


class Agent:

    def __init__(self, available_actions):
        self.available_actions = available_actions
        return

    def train_inst(self, observation, label):
        return self.predict(observation)

    def predict(self, observation):
        action = random.choice(self.available_actions)
        return action

    def train(self):
        pass

    def reset(self):
        pass
