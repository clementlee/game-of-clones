import random
import multiprocessing
import math


def normpdf(x, mu = 0.0, sigma = 1.0):
    """Returns the value of the normal (Gaussian) distribution value at a
    specified point, with mean and standard deviation."""
    
    return (1/(sigma*normpdf.sqrt2pi))*math.e**(-((x-mu)**2)/(2*sigma**2))

normpdf.sqrt2pi = math.sqrt(2*math.pi) #constants increase speed of calculation
    
class PvPGame:
    """the equivalent of the Prisoner's Dilemma, a player vs player game in
    in which sides decide to either cooperate or to defect."""

    #the four possibilities for the game, allows for asymmetric games
    cc = 1#coop-coop
    cd = 2#coop-defect
    dc = 2#defect-coop
    dd = 3#defect-defect

    p1id = 0 #player ids
    p2id = 0

    def __init__(self, cc = 1, cd = 2, dc = 2, dd = 3, p1id = 0, p2id = 0):
        self.cc = cc #assign default values when initializing
        self.cd = cd
        self.dc = dc
        self.dd = dd
        self.p1id = p1id
        self.p2id = p2id

class CoopGame:
    """A cooperative game in which the more people participating the more
    benefit there is to gain."""

    #two possibilities for each agent, symmetric game
    coop = 1.05 #the cooperation bonus
    defect = 1.03 #the defection bonus

    idlist = [] #members of the game
    
    def __init__(self, coop = 1.05, defect = 1.03, idlist = []):
        self.coop = coop
        self.defect = defect
        idlist = []

    def calcpayout(self):
        for id in idlist:
            if id in Agent.map: #check validity of id
                agent = Agent.map[id]
                agent.evalcoop(self) #do something with this evaluation
            else: #should never happen
                print "error: Agent "+str(id)+" is either dead or nonexistent."
        

class Agent:
    """The 'clone' of the simulation; each individual agent/actor keeps
    its own state and evaluating functions."""

    id = 0
    life = 100
    posx = 0 #position along "game board"
    posy = 0
    prev_enc = {} #memory of previous encounters with others, keyed by Agent id
    def __init__(self):
        id = Agent.counter
        Agent.counter += 1
        Agent.map[id] = self; #maps id to self, allowing future lookup
        pass

    def update(self):
        """Updates the agent for every single iteration"""
        if life <= 0: #death
            del Agent.map[id] #removing from lookup is equivalent to death
        life -= 1

    def evalPvP(self, pvpgame):
        pass

    def evalCoop(self, coopgame):
        pass

    def __eq__(self, other):
        return self.id == other.id
Agent.counter = 0; #lifetime counter of all Agents
Agent.map = {}     #mapping from Agent id to actual Agent.

def main(): #main method
    print "hi"

if __name__ == '__main__':
    main()
