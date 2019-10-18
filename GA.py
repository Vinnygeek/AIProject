import FileHandle as fh

class GA:
    currentGen = 0 #Current Generation of the process
    bestfitness = 0 #The fitness of the best individual
    solvedMaze = [] #Maze after the GA Process

    def __init__(self, mazeFile, numPopulation, crossoverIndex, crossoverMethod, mutationIndex, numGenerations):
        self.mazeFile = mazeFile
        self.numPopulation = numPopulation
        self.crossoverIndex = crossoverIndex
        self.crossoverMethod = crossoverMethod
        self.mutationIndex = mutationIndex
        self.numGenerations = numGenerations

    def printConfigData(self):
        print("Maze File: ",self.mazeFile,)
        print("Nº Population: ",self.numPopulation,)
        print("Crossover Index: ",self.crossoverIndex,)
        if(self.crossoverMethod == 0):
            print("Crossover Method: Roulette.")
        else:
            print("Crossover Method: Tournament.")
        print("Mutation Index: ",self.mutationIndex,)
        print("Nº Generations set: ",self.numGenerations,)      
    
    '''def beginGA():
        if(self.crossoverMethod == 0):
            beginRoulette()
        else:
            beginTournament()'''
    
    #def beginRoulette():

    #def beginTournament():