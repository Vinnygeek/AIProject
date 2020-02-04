# AIProject(Ubuntu Version)
A Genetic Algorithm for maze path finding. development for the Artifitial Intelligence Class project on 2019
2nd Period.

## Genetic Algorithm:
In order to perform the Genetic Algorithm on the maze, we first need to set the `mazeFile`, `numIndividuals`, `individualSize`, `crossoverIndex`, 
`crossoverMethod`, `mutationIndex`,`mutationIndexGenotype` and the `numGenerations` attributes in the beginning of the process; then, accordingly to the crossover Method
choosed, the GA engine begins the process. On begining of the process, we generate the population with the genotype of all individuals calculated randomly. The gens are suited to the following possible characters:
*'U' for the up movement.
*'R' for the right movement.
*'D' for the down movement.
*'L' for the left movement.
With all set, we calculate the fitness of each individual by giving points for every movement in blank and penalizing it for hits and repeated blocks on the path. We take the best individual and save it to keep elitism.
#### The Roulette Method:
If the Roulette Method is choosed, we begin the generations by choosing the interval of choice for each individual. Then we pick randonly a number between 0 and the sum of the fitness of each, then we verify which of them belongs to the interval given by this last number and then we save the lucky one on the `matingPool` for the crossover process.

#### The Tournament:

#### Crossover
The crossover process is the same for both Roulette Wheel or Tournament method. It consists of shuffling the individuals on the `matingPool` in order to get the random ones to perform the process; so, given two individuals, we pick the second half of the second one on the backwards order(first we take the last gen, then the gen before the last and etc...) and apply on the first half of the first one on the forward order(we substiture the first gen, then the second and so on...). After the process, we recalculate the fitness and save the best individual to keep elitism.

### Overview

1. Generate the initial population ramdonly accordingly to the `numGenerations` and the `individualSize`attributes. the `individualSize`
will be multiply by the default individual size, which is the qtd of the blank space on the maze.

2. Calculate the fitness of each individual created previously.

3. Selecting ramdomly the individuals for mating pool acordingly to the `crossoverIndex`.

4. If we are using the Roulette Method, then we roll the wheel and choose the individuals for the mating process.
If the tournament is set, than we must choose the best ones accordingly to the `crossoverIndex` to randomly be mating on the process.

5. Select the individuals for mutation duly to the `mutationIndex` set initially, and randomly choose the gen for change and the value accordingly to the `mutationIndexGenotype`.

6. Recalculate the fitness of each individual again, saving the best one.

7. Repeat all the process from the 3rd step until the number of generations is achieved.

### The Fitness Calculation

This step is performed for both Roulette and Tournament configuration.
We take the individual, which would be an arrayList with all the movements done from the beginning to the end. and then
we sum step by step from the first element which will be the starting point to the solution element. The best fitness will be that one 
with the least number of steps from the start and finish place.
The following situations could be used to penalize some individuals' fitness.
* The individual path contains circles.
* The individual returns to a previously point, indicating that it took a deadend path somehow.
* If the individual doesn't hit the objective at all, it will be penalized with the worst fitness value.
