class Individual:
    def __init__(self):
        self.fitness = 0
        self.RouletteNumber = 0
        self.genotype = []
        self.actualXPos = 0
        self.actualYPos = 0
        self.pathFound = 0
        self.path = []
        self.crossoverMade = 0 #Used in the crossover. 0 if it was not mated yet, 1 otherwis
