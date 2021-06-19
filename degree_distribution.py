class DegreeDistribution:
    def __init__(self, network):
        """
        Computes the degree distribution of a network. Make sure that both degree 0 and the maximum degree
        are included!
        """
        # TODO: initialise a list to store the observations for each degree (including degree 0!)
        self.maxDegree = network.max_degree()
        self.Size = network
        self.histogram = [0] * (self.maxDegree + 1)


        # TODO: fill the histogram with the degree distribution
        
        for k, node in network.nodes.items():
            deg = node.degree()
            self.histogram[deg] = self.histogram[deg] + 1

        # TODO: normalize with amount of nodes in network
    def normalisation(self):
        
        self.normalisation = []
        max_Degree = 0
        while max_Degree <= self.maxDegree:
            self.normalisation.append((float(self.histogram[max_Degree])/self.Size.size()))
            max_Degree += 1 
        return self.normalisation
        
