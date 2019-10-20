import FileHandle as fh
import random
import Individual as ind

class GA:
    currentGen = 0 #Current Generation of the process
    individualDefaultSize = 0
    bestfitness = 0 #The fitness of the best individual
    cleanMaze = [] #Maze after the GA Process
    workingMaze = [] #Maze for test the individuals
    population = [] #Array of individuals
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
        self.cleanMaze = self.workingMaze
        
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
            #Creating an individual and setting the initial x and y position at the 'S' location
            newIndividual = ind.Individual()
            newIndividual.actualXPos = self.initialX
            newIndividual.actualYPos = self.initialY
            for l in range(self.individualSize):
                op = random.randint(0,3)
                if(op == 0):
                    newIndividual.genotype.append('U') #U for Up movement
                elif(op == 1):
                    newIndividual.genotype.append('R') #R for Right
                elif(op == 2):
                    newIndividual.genotype.append('D') #D for down
                elif(op == 3):
                    newIndividual.genotype.append('L') #L for Left
            self.population.append(newIndividual)
        
        #Calculating the fitness of each individual
        for o in range(len(self.population)):
            for step in self.population[o].genotype:
                if(self.population[o].pathFound == 0): #No Path has been found yet
                    if(step == 'U'):
                        if(self.population[o].actualYPos > 1): #Boundary Condition 
                            self.population[o].actualYPos -= 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].pathFound = 1
                                self.population[o].path = self.workingMaze
                                self.workingMaze = self.cleanMaze #Reset the maze
                                print("Path Found")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualYPos += 1 #Returning to the position before hit.
                    elif(step =='R'):
                        if(self.population[o].actualXPos < len(self.workingMaze[o]) - 2): #Boundary Condition 
                            self.population[o].actualXPos += 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].pathFound = 1
                                self.population[o].path = self.workingMaze
                                self.workingMaze = self.cleanMaze #Reset the maze
                                print("Path Found")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualXPos -= 1
                    elif(step == 'D'):
                        if(self.population[o].actualYPos < len(self.workingMaze[o]) - 2): #Boundary Condition 
                            self.population[o].actualYPos += 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].pathFound = 1
                                self.population[o].path = self.workingMaze
                                self.workingMaze = self.cleanMaze #Reset the maze
                                print("Path Found")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualYPos -= 1 
                    elif(step == 'L'):
                        if(self.population[o].actualXPos > 1): #Boundary Condition 
                            self.population[o].actualXPos -= 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].pathFound = 1
                                for a in self.workingMaze:
                                    print(a)
                                self.population[o].path = self.workingMaze
                                self.workingMaze = self.cleanMaze #Reset the maze
                                print("Path Found")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualXPos += 1
            print(o,"Individual Fitness",self.population[o].fitness)
            fh.FileHandle.fileWriting(self,"files/testingMaze.txt",self.workingMaze) #Getting one of the paths
            self.workingMaze = self.cleanMaze #Cleaning the maze for the next individual

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