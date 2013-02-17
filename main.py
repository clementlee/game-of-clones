import random
import multiprocessing

class PvPGame:
    """the equivalent of the Prisoner's Dilemma, a player vs player game in
    in which sides decide to either cooperate or to defect."""
    pass

class CoopGame:
    """A cooperative game in which the more people participating the more
    benefit there is to gain."""
    coop = 1.05
    defect = 1.03
    def __init__(self, coop = 1.05, defect = 1.03):
        self.coop = coop
        self.defect = defect
    pass

class Agent:
    """The 'clone' of the simulation; each individual agent/actor keeps
    its own state and evaluating functions."""

    id = 0
    life = 100
    prev_enc = {}
    def __init__(self):
        pass

    def update(self):
        """Updates the agent for every single iteration"""
        pass

def main():
    print "hi"

if __name__ == '__main__':
    main()
