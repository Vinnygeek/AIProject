import csv
import GA
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy

def createCSV():
    newCsv = []
    for i in range(4):
        if(i != 0):
            newElement = []
            for j in range(4):
                if(j != 0):
                    #print("On",i*10,j*10,"iteration")
                    nova = GA.GA("files/LabirintoExemplo01.txt",i*10,2,56,0,13,5,j*10).bestIndividual.fitness 
                    newElement.append(copy.deepcopy(i*10))
                    newElement.append(copy.deepcopy(j*10))
                    newElement.append(copy.deepcopy(nova))
                    newCsv.append(copy.deepcopy(newElement))
                    newElement = []
    print("Data",newCsv)
    
    #Normalizing the data on the fitness of the best individual
    mySum = 0
    for datai in newCsv:
        if(datai[2] > mySum):
            mySum = copy.deepcopy(datai[2])

    for datai2 in newCsv:
        datai2[2] = datai2[2]*100/mySum

    #Saving the results on a CSV file
    with open('results.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(newCsv)
    csvFile.close()

def plotElitism():
    myelitism = GA.GA("files/LabirintoExemplo01.txt",10,2,56,0,13,5,20)._elitism
    mySum = 0
    for datai in myelitism:
        if(datai[1] > mySum):
            mySum = copy.deepcopy(datai[1])
    
    X = []
    Y = []
    for datai2 in myelitism:
        datai2[1] = datai2[1]*100/mySum
        X.append(copy.deepcopy(datai2[0]))
        Y.append(copy.deepcopy(datai2[1]))

    plt.xlabel("Generation")
    plt.ylabel("Fitness[%]")
    plt.title("Elitism on Roulette Wheel")
    plt.plot(X,Y)
    plt.show()

def plotSurface():

    DataAll1D = np.loadtxt("person.csv", delimiter=",")

    # create 2d x,y grid (both X and Y will be 2d)
    X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

    # repeat Z to make it a 2d grid
    Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, Z, cmap='ocean')

    plt.show()


def plotScattered():
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')

    x, y, z = np.loadtxt('results.csv', delimiter=',', unpack=True)

    ax1.scatter(x,y,z)
    plt.xlabel("Population")
    plt.ylabel("N Generations")
    plt.title("Fitness")
    plt.show()

#createCSV()
#plotScattered()
#plotElitism()
#createCSV()
