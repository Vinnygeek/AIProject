import FileHandle as fh
import random

class GA:
    currentGen = 0 #Current Generation of the process
    individualDefaultSize = 0
    bestfitness = 0 #The fitness of the best individual
    solvedMaze = [] #Maze after the GA Process
    workingMaze = [] #Maze for test the individuals
    population = [] #Number of individuals
    initialX = 0 #Initial X position, the beginnig of the path
    initialY = 0 #Initial y position of the path
    finalX = 0 #Final x position of the path, its the x goal
    finalY = 0 #Final y position of the path

    def __init__(self, mazeFile, numIndividuals,individualSize, crossoverIndex, crossoverMethod, mutationIndex, numGenerations):
        self.mazeFile = mazeFile
        self.numIndividuals = numIndividuals
        self.individualSize = individualSize
        self.crossoverIndex = crossoverIndex
        self.crossoverMethod = crossoverMethod
        self.mutationIndex = mutationIndex
        self.numGenerations = numGenerations
        self.workingMaze = fh.FileHandle.readFileWords(self,self.mazeFile)
        self.solvedMaze = self.workingMaze
        
        #calculating the default size(which is the number of empry spaces of the maze)
        for i in self.workingMaze:
            for j in i:
                if(j == ' '):
                    self.individualDefaultSize = self.individualDefaultSize + 1
        self.individualSize = self.individualSize*self.individualDefaultSize

        #calculating the x and y beginning position and final position
        for i in range(len(self.workingMaze)):
            for j in range(len(self.workingMaze[0])):
                if(self.workingMaze[i][j] == 'S'):
                    self.initialX = i
                    self.initialY = j
                elif(self.workingMaze[i][j] == 'E'):
                    self.finalX = i
                    self.finalY = j

        #Setting the population with the movements randomly
        for k in range(self.numIndividuals):
            newIndividual = []
            for l in range(self.individualSize):
                op = random.randint(0,3)
                if(op == 0):
                    newIndividual.append('U') #U for Up movement
                elif(op == 1):
                    newIndividual.append('R') #R for Right
                elif(op == 2):
                    newIndividual.append('D') #D for down
                elif(op == 3):
                    newIndividual.append('L') #L for Left
            self.population.append(newIndividual)
        
        #print(self.population)

    def printConfigData(self):
        print("Maze File: ",self.mazeFile,)
        print("Population: ",self.numIndividuals)
        print("Individual Default size: ",self.individualDefaultSize) #The size is the quantity of the blank spaces on the maze
        if(self.numIndividuals*self.individualDefaultSize > 0):
            print("Individual size: ",self.numIndividuals*self.individualDefaultSize)
        else:
            print("Individual size: Unset")
        print("Crossover Index: ",self.crossoverIndex,)
        if(self.crossoverMethod == 0):
            print("Crossover Method: Roulette.")
        else:
            print("Crossover Method: Tournament.")
        print("Mutation Index: ",self.mutationIndex,)
        print("Nº Generations set: ",self.numGenerations)
        print("Initial Position: (",self.initialX,' ',self.initialY,')')
        print("Final Position: (",self.finalX,' ',self.finalY,')')      
    
    #def beginGA():
        #if(self.crossoverMethod == 0):
            #beginRoulette()
        #else:
         #   beginTournament()
    
    #def beginRoulette():
        
    #def beginTournament():