class City:
    agents = []
    
    def __init__(self, sizex, sizey, num_agents, agent_spread, agent_variance):

        for(i in xrange(num_agents)):
            self.agents.append(
