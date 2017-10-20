import random
import math
def population_initialization(pop_size,size): #Population initialization
	
	input_array=[]

	for i in range(0,size):
		weight=int(input('Enter weight w '))
		benefit=int(input('Enter the benefit of including the following item '))
		tup=(weight,benefit)
		input_array.append(tup)
	pop=[[random.randint(0,1) for i in range(size)] for j in range(pop_size)]
	
	return input_array,pop
def select(pop,fitness):
	size=len(pop)
	totalfit=sum(fitness)
	ran=random.randint(0,totalfit)
	tempSum=0
	parent1=[]
	fit1=0
	for i in range(size):
		tempSum+=fitness[i]
		if(tempSum>=ran):
			parent1=pop.pop(i)
			fit1=fitness.pop(i)
			break
	tempSum=0
	parent2=[]
	fit2=0
	ran2=random.randint(0,sum(fitness))
	for i in range(len(pop)):
		tempSum+=fitness[i]
		if(tempSum>=ran2):
			parent2=pop[i]
			pop+=[parent1]
			fitness+=[fit1]
	return parent1,parent2
def newPopulation(pop, fitness, pm,px,pu):
  popSize = len(pop)
  size=len(pop[0])
  newPop = []
  newPop += [selectElite(pop, fitness)]

  while(len(newPop) < popSize):
    (parent1, parent2) = select(pop, fitness)
    #newPop += [mutation(crossover(parent1,parent2), pm,size)]
    mutated=[]

    mutated=uniformCrossover(parent1,parent2,px,pu) #Uniform crossover 
    #print('Uniform cross over se ',mutated)
    for i in range(2):
    	newPop+=[mutation(mutated[i],pm,size)]
  return newPop

def calculate_fitness(pop,input_array,max_weight): #Fitness function-Calculating fitness
	fitness=[]
	for i in range(len(pop)):
		benefit=0
		weight=max_weight+1
		while(weight>max_weight):
			benefit=0
			weight=0
			ones=[]
			for j in range(len(pop[i])):
				if(pop[i][j]==1):
					benefit+=input_array[j][1]
					weight+=input_array[j][0]
					ones+=[j]
				if(weight>max_weight):
					pop[i][ones[random.randint(0, len(ones)-1)]] = 0
		
		
		fitness+=[benefit]
	return fitness
def selectElite(pop,fitness):
	elite=0
	for i in range(len(fitness)):
		if fitness[i]>fitness[elite]:
			elite=i
	return pop[elite]
def crossover(parent1,parent2): #CrossOver Function (Single Point CrossOver)
	random_index=random.randint(0,len(parent1)-1)
	return parent1[:random_index]+parent2[random_index:]

def uniformCrossover(parent1,parent2,px,pu): #CrossOver Function (Uniform CrossOver)
	child1=parent1[:]
	child2=parent2[:]
	if px>random.random():
		for i in range(len(parent1)):
			if pu>random.random():
				child1[i]=parent2[i]
				child2[i]=parent1[i]
	return [child1,child2]

def mutation(chromosome,pm,size): #Mutation Function
	for i in range(size):
		if random.random()<pm:
			if (chromosome[i]==1):
				chromosome[i]=0
			else:
				chromosome[i]=1
	return chromosome


if __name__=='__main__':
	input_array=[]
	fitness=[]
	pop=[[]]
	size=int(input('Enter the number of items :-'))
	pop_size=int(input('Enter population size :- '))
	max_weight=int(input('Enter the maximum weight '))
	pm=float(input('Enter mutation probability '))
	px=float(input('Enter crossover probability '))
	pu=0.5 #Uniform crossover rate
	input_array,pop=population_initialization(pop_size,size)

	print('Input given is  (weight,benefit)',input_array)
	
	fitness=calculate_fitness(pop,input_array,max_weight)
	print('Intial population ',pop)

	print('Fitness values of chromosomes (benefit,max_volume,index)',fitness)
	i=0
	while i!=1000:
		i=i+1
		pop=newPopulation(pop, fitness, pm,px,pu)
		print('New Population ',pop)
		fitness = calculate_fitness(pop,input_array,max_weight)
		print('Fitness values ',fitness)
	print('Final Solution :-',selectElite(pop,fitness))
	final=selectElite(pop,fitness)
	max_benefit=0
	for i in range(len(final)):
		if(final[i]==1):
			max_benefit+=input_array[i][1]
	print('Maximum Benefit :--->',max_benefit)
