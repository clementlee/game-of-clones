class Agent:
    """The 'clone' of the simulation; each individual agent/actor keeps
    its own state and evaluating functions."""
    
    id = 0
    life = 100
    posx = 0 #position along "game board"
    posy = 0
    prev_enc = {} #memory of previous encounters with others, keyed by Agent id
                  #stores float value

    pos_attr = 0.5 #attraction towards positive outcomes
    neg_attr = -0.5 #attraction towards negative outcomes

    def __init__(self, life = 100, posx = 0, posy = 0, pos_attr = 0.5,
                 neg_attr = 0.5):
        self.id = Agent.counter
        self.life = life
        self.posx = posx
        self.posy = posy
        self.pos_attr = pos_attr
        self.neg_attr = neg_attr
        Agent.counter += 1
        Agent.map[self.id] = self; #maps id to self, allowing future lookup

    def update(self):
        """Updates the agent for every single iteration"""
        if self.life <= 0: #death
            del Agent.map[self.id] #removing from lookup is equivalent to death
        self.life -= 1 #update lifetime

        #breeding
        scale = 0.1   #overall breeding rate
        maxlife = 100.0 #maximum life possible
        ratio = 2*(maxlife - self.life)/maxlife
        breedposs = scale * normpdf(ratio)
        print "Breed chance for agent #"+str(self.id)+", age "+str(self.life)+\
              " is "+str(breedposs)

    def evalpvp(self, pvpgame):
        pass

    def evalcoop(self, coopgame):
        pass

    def __eq__(self, other):
        return self.id == other.id

Agent.counter = 0; #lifetime counter of all Agents
Agent.map = {}     #mapping from Agent id to actual Agent.
Agent.statii = enum('NONE','COOP','PVP')
Agent.colors = {
