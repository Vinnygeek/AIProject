# AIProject
A Genetic Algorithm and Ant Colony Optimization for maze path finding. development for the Artifitial Intelligence Class project on 2019
2nd Period.

## Genetic Algorithm:
In order to perform the Genetic Algorithm on the maze, we first need to set the `mazeFile`, `numPopulation`, `individualSize`, `crossoverIndex`, 
`crossoverMethod`, `mutationIndex` and the `numGenerations` attributes in the beginning of the process; then, accordingly to the crossover Method
choosed, the GA engine begins the process.
#### The Roulette Method:
If the Roulette Method is choosed, we begin with the initial population generated ramdonly and with the same percentage on the wheel. As the
algorith takes further, the fitness of each individual will be used to reset the percentage of the disk, giving a big amount for the best fit
and the small one to the worst.

#### The Tournament:

### Overview

1. Generate the initial population ramdonly accordingly to the `numGenerations` and the `individualSize`attributes. the `individualSize`
will be multiply by the default individual size, which is the qtd of the blank space on the maze.

2. Calculate the fitness of each individual created previously.

3. Selecting ramdomly the individuals for mating pool acordingly to the `crossoverIndex`.

4. If we are using the Roulette Method, then we roll the wheel and choose the individuals for the mating process.
If the tournament is set, than (...).

5. Select the individuals for mutation duly to the `mutationIndex` set initially.

6. Recalculate the fitness of each individual again.

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

## Ant Colony Optmization
parallel to the GA method prescribed before, the ACO lies on the Evolutionary Algorithm class as well.
