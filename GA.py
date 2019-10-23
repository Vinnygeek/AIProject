# -*- coding: utf-8 -*-
import FileHandle as fh
import random
import Individual as ind
import time
import numpy
import operator
import copy


class GA:
    #matingPool = [] #will store the index of each individual for mating
    #mutationPool = [] #will store the index of each individual for mutation
    #currentGen = 0 #Current Generation of the process
    #individualDefaultSize = 0
    #bestfitness = 0 #The fitness of the best individual
    #cleanMaze = [] #Maze after the GA Process
    #workingMaze = [] #Maze for test the individuals
    #population = [] #Array of individuals
    #bestIndividual = ind.Individual() #Keeps the best individual(Elitism)
    #nIndToCross = 0
    #nIndToMutate = 0
    #initialX = 0 #Initial X position, the beginnig of the path
    #initialY = 0 #Initial y position of the path
    #finalX = 0 #Final x position of the path, its the x goal
    #finalY = 0 #Final y position of the path
    #nGenotypeToMutate = 0

    def __init__(self, mazeFile, numIndividuals,individualSize, crossoverIndex, crossoverMethod, mutationIndex,mutationIndexGenotype, numGenerations):
        self.matingPool = [] #will store the index of each individual for mating
        self.bestIndividual = ind.Individual()
        self.population = []
        self.individualDefaultSize = 0
        self.mazeFile = mazeFile
        self.numIndividuals = numIndividuals
        self.individualSize = individualSize
        self.crossoverIndex = crossoverIndex
        self.crossoverMethod = crossoverMethod
        self.mutationIndex = mutationIndex #Percentage of individuals to mutate
        self.mutationIndexGenotype = mutationIndexGenotype #Percentage of genoma to mutate
        self.numGenerations = numGenerations
        fyfy = fh.FileHandle()
        self.workingMaze = fh.FileHandle.readFileWords(fyfy,self.mazeFile)
        self.cleanMaze = copy.deepcopy(self.workingMaze)
        self.bestSolutionMaze = self.cleanMaze
        self.nIndToCross = int(round(self.crossoverIndex*self.numIndividuals/100))
        self.nIndToMutate = int(round(self.mutationIndex*self.numIndividuals/100))
        self._elitism = []

        #calculating the default size(which is the number of empry spaces of the maze)
        for i in self.workingMaze:
            for j in i:
                if(j == ' '):
                    self.individualDefaultSize = self.individualDefaultSize + 1
        self.individualSize = self.individualSize*self.individualDefaultSize

        #Calculate the number of gens to mutate
        self.nGenotypeToMutate = int(round(self.mutationIndexGenotype*self.individualSize/100))
        
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
        #Creating population
        for k in range(self.numIndividuals): 
            #Creating an individual and setting the initial x and y position at the 'S' location
            newIndividual = ind.Individual()
            newIndividual.actualXPos = self.initialX
            newIndividual.actualYPos = self.initialY
            for l in range(self.individualSize): #self.individualSize
                op = self.genRandom(0,3)
                if(op == 0):
                    newIndividual.genotype.append('U') #U for Up movement
                elif(op == 1):
                    newIndividual.genotype.append('R') #R for Right
                elif(op == 2):
                    newIndividual.genotype.append('D') #D for down
                elif(op == 3):
                    newIndividual.genotype.append('L') #L for Left
            random.shuffle(newIndividual.genotype)
            self.population.append(newIndividual)
            del newIndividual

        #Calculating initial Fitness
        self.calculateFitness()

        #Saving initial best individual
        for indiv in self.population:
            if(indiv.fitness > self.bestIndividual.fitness):
                self.bestIndividual = copy.deepcopy(indiv)
        self._elitism.append([0,self.bestIndividual.fitness])
        #Showing all genotypes and the best Individual genotype
        #for inder in self.population:
            #print("On initial best intividual set: Fitness are",inder.fitness)
        #print("BestGenotypefiness is----------------------------",self.bestIndividual.fitness)


        #Beginning the GA Process on generations and applying mutation
        for _generation in range(self.numGenerations):
            #print(_generation + 1,"Generation.","Best Fitness so far:",self.bestIndividual.fitness)
            self.beginGA()
            self.beginMutation()
            self._elitism.append([_generation + 1,copy.deepcopy(self.bestIndividual.fitness)])
        #For debug purpose---------------------------------------------------------------
        #for k in range(len(self.population)):
            #print("on ",k,"iteration",self.population[k].genotype)

        #---------------------------------------------------------------------
    def calculateFitness(self):
        #Calculating the fitness of each individual
        for o in range(len(self.population)):
            self.population[o].fitness = 0 #Reset previously Fitness set before
            self.population[o].pathFound = 0
            self.population[o].actualXPos = self.initialX
            self.population[o].actualYPos = self.initialY
            self.workingMaze = copy.deepcopy(self.cleanMaze)

            for step in self.population[o].genotype:
                if(self.population[o].pathFound == 0): #No Path has been found yet
                    if(step == 'U'):
                        if(self.population[o].actualYPos > 1): #Boundary Condition 
                            self.population[o].actualYPos -= 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 50
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].fitness += 3000
                                self.population[o].pathFound = 1
                                self.population[o].path = copy.deepcopy(self.workingMaze)
                                self.workingMaze = copy.deepcopy(self.cleanMaze) #Reset the maze
                                self.bestSolutionMaze = copy.deepcopy(self.population[o].path)
                                #print("Path Found in U")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualYPos += 1 #Returning to the position before hit.
                    elif(step =='R'):
                        if(self.population[o].actualXPos < len(self.workingMaze[0]) - 2): #Boundary Condition 
                            self.population[o].actualXPos += 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 50
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].fitness += 3000
                                self.population[o].pathFound = 1
                                self.population[o].path = copy.deepcopy(self.workingMaze)
                                self.workingMaze = copy.deepcopy(self.cleanMaze) #Reset the maze
                                self.bestSolutionMaze = copy.deepcopy(self.population[o].path)
                                #print("Path Found in R")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualXPos -= 1
                    elif(step == 'D'):
                        if(self.population[o].actualYPos < len(self.workingMaze[0]) - 2): #Boundary Condition 
                            self.population[o].actualYPos += 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 50
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].fitness += 3000
                                self.population[o].pathFound = 1
                                self.population[o].path = copy.deepcopy(self.workingMaze)
                                self.workingMaze = copy.deepcopy(self.cleanMaze) #Reset the maze
                                self.bestSolutionMaze = copy.deepcopy(self.population[o].path)
                                #print("Path Found in D")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualYPos -= 1 
                    elif(step == 'L'):
                        if(self.population[o].actualXPos > 1): #Boundary Condition 
                            self.population[o].actualXPos -= 1 
                            if(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == ' '):
                                self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] = '*'
                                self.population[o].fitness += 50
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'S'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == '*'):
                                self.population[o].fitness -= 1
                            elif(self.workingMaze[self.population[o].actualXPos][self.population[o].actualYPos] == 'E'):
                                self.population[o].pathFound = 1
                                self.population[o].fitness += 3000
                                self.population[o].path = copy.deecopy(self.workingMaze)
                                self.workingMaze = copy.deepcopy(self.cleanMaze) #Reset the maze
                                self.bestSolutionMaze = copy.deepcopy(self.population[o].path)
                                #print("Path Found in L")
                            else:#A wall was hit
                                self.population[o].fitness -= 2
                                self.population[o].actualXPos += 1
            for _ind in self.population:
                if(_ind.fitness <= 0):
                    _ind.fitness = 10 #Setting the 10 points fitness to all the negative fitness
            #print(o,"Individual Fitness",self.population[o].fitness)
            fyfy2 = fh.FileHandle()
            fh.FileHandle.fileWriting(fyfy2,"files/testingMaze.txt",self.workingMaze) #Getting a test maze
            fh.FileHandle.fileWriting(fyfy2,"files/bestSolutionMaze.txt",self.bestSolutionMaze) #Getting the best maze file.txt
        self.workingMaze = self.cleanMaze #Cleaning the maze for the next individual

    def genRandom(self,lLimit,Rlimit):
        value = random.randint(lLimit,Rlimit)
        return value

    def printConfigData(self):
        print("Maze File: ",self.mazeFile,)
        print("Population: ",self.numIndividuals)
        print("Individual Default size: ",self.individualDefaultSize) #The size is the quantity of the blank spaces on the maze
        if(self.numIndividuals*self.individualDefaultSize > 0):
            print("Individual size: ",self.numIndividuals*self.individualDefaultSize)
        else:
            print("Individual size: Unset")
        print("Crossover Index: ",self.crossoverIndex,'%')
        print("# Individuals to crossover:",self.nIndToCross)
        if(self.crossoverMethod == 0):
            print("Crossover Method: Roulette.")
        else:
            print("Crossover Method: Tournament.")
        print("Mutation Individuals Index: ",self.mutationIndex,'%')
        print("# Individuals to mutate:",self.nIndToMutate)
        print("Mutation Genotype Index: ",self.mutationIndexGenotype,'%')
        print("# of Gens to mutate: ",self.nGenotypeToMutate)  
        print("# Generations set: ",self.numGenerations)
        print("Initial Position: (",self.initialX,' ',self.initialY,')')
        print("Final Position: (",self.finalX,' ',self.finalY,')')
        print("Best Individual fitness:",self.bestIndividual.fitness)      
    
    def beginGA(self):
        if(self.crossoverMethod == 0):
            self.beginRoulette()
        else:
            self.beginTournament()
    
    def beginRoulette(self):
        #print("on roulette")
        fitnessSum = 0
        counting = 0
        for tr in self.population:
            fitnessSum += tr.fitness
            tr.roulettenumber = fitnessSum
        #Begin selection for mating pool
        for mp in range(self.nIndToCross):
            rate = random.randint(0,fitnessSum)
            #print("Random Selected",rate)
            counting = 0
            for innj in range(len(self.population)):
                if(counting <= rate <= self.population[innj].roulettenumber):
                    self.matingPool.append(innj.__int__())
                    counting = self.population[innj].roulettenumber
                else:
                    counting = self.population[innj].roulettenumber
            counting = 0
        #for aka in self.population:
            #print("Individual Fitness",aka.fitness)
        #print("fitnessSum",fitnessSum)
        #print("Mating pool",self.matingPool)
        self.beginCrossover()
        #print("After Roulette crossover best individual fitness is:",self.bestIndividual.fitness)
    def beginCrossover(self):
        #print("On Crossover")
        random.shuffle(self.matingPool)
        for mate in range(int(round(len(self.matingPool)/2))):
            secMateIndex = len(self.matingPool) - mate - 1
            newfirstInd = copy.deepcopy(self.population[self.matingPool[mate]].genotype)
            newSecInd = copy.deepcopy(self.population[self.matingPool[secMateIndex]].genotype)
            for gen in range(int(round(len(newfirstInd)/2))):
                newfirstInd[gen] = copy.deepcopy(self.population[self.matingPool[secMateIndex]].genotype[len(newfirstInd) - 1 - gen])
                newSecInd[gen] = copy.deepcopy(self.population[self.matingPool[mate]].genotype[len(newfirstInd) - 1 - gen])
            self.population[self.matingPool[mate]].genotype = copy.deepcopy(newfirstInd)
            self.population[self.matingPool[secMateIndex]].genotype = copy.deepcopy(newSecInd)

        #Calculating fitness
        #print("Before calculate Fitness on crossover",self.bestIndividual.fitness)
        self.calculateFitness()
        #print("After Calculating Fitness on crossover",self.bestIndividual.fitness)
        #Keeping the best Individual
        self.saveBestIndividual()

        #flushig the matingPool for the next operations
        self.matingPool = []
        #For Debug Purpose----------------------------------------------------------
        #for k in range(len(self.population)):
                #print("on ",k,"iteration",self.population[k].genotype)

    def beginTournament(self):
        #sort the individuals
        self.population.sort(key=operator.attrgetter('fitness'),reverse = True)

        #choose the best one accordingly to the index on a for loop
        for _ind in range(self.nIndToCross):
            self.matingPool.append(copy.deepcopy(_ind))

        #Begin the crossover
        self.beginCrossover()
        #Save the est individual again

    def beginMutation(self):
        #Shuflling the individuals to mutate
        random.shuffle(self.population)
        for m1 in range(self.nIndToMutate):
            for m2 in range(self.nGenotypeToMutate):
                rad = self.genRandom(0,3)
                if(rad == 0):
                    self.population[m1].genotype[m2] = 'U' #U for Up movement
                elif(rad == 1):
                    self.population[m1].genotype[m2] = 'R' #R for Right
                elif(rad == 2):
                    self.population[m1].genotype[m2] = 'D' #D for down
                elif(rad == 3):
                    self.population[m1].genotype[m2] = 'L' #L for Left
        #Calculating fitness
        self.calculateFitness()

        #Saving the Best Individual after mutation Process
        self.saveBestIndividual()

    def saveBestIndividual(self):
        betterIndividualFound = False #This attribute will be true if a better individual is found 
        #print("Saving the best individual: Actual = ",self.bestIndividual.fitness)
        for indiv in self.population:
            #print("On Sabing The best individual Fitness = to ",indiv.fitness)
            if(indiv.fitness > self.bestIndividual.fitness):
                self.bestIndividual = copy.deepcopy(indiv)
                betterIndividualFound = True
        if(betterIndividualFound == False): #none better individual was found on the process
        #Killing the worse individual accordingly to fitness and adding the best actual individual
        #Checking if the best individual aren't already on the population
            itson = False #Means that the actual best individuo isn't on the population
            for betterin in self.population:
                if(betterin.fitness == self.bestIndividual.fitness):
                    itson = True
            if(itson == False):
                self.population.sort(key=operator.attrgetter('fitness'),reverse = True)
                self.population.pop()
                self.population.append(copy.deepcopy(self.bestIndividual))
                random.shuffle(self.population)


         