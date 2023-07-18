
from random import randint, uniform, choice
from statistics import stdev
FILE_PATH = 'data.csv'

NUM_GROUPS = 7

NUM_GENERATIONS = 20
POPULATION_SIZE = 500
TOURNAMENT_SIZE = 10
CROSSOVER_RATE = .9
MUTATION_RATE = .01

def get_data(file_path) :

    keys = list()
    values = list()

    with open(file_path, 'r') as reader :
        lines = reader.readlines()

        split_lines = [line.split(',') for line in lines]

        keys = [split_line[0] for split_line in split_lines]
        values = [float(split_line[1]) for split_line in split_lines]

        return keys, values
    
KEYS, VALUES = get_data(FILE_PATH)

def fitness(genome) :

    group_sizes = [0 for _ in range(NUM_GROUPS)]

    for i, gene in enumerate(genome) :
        group_sizes[gene] += VALUES[i]

    return -stdev(group_sizes)

def tournament_select(population) :
    
    tournament = list()

    for i in range(TOURNAMENT_SIZE) :
        tournament.append(population[randint(0, POPULATION_SIZE - 1)])

    max_i = 0
    max_fitness = fitness(tournament[i])

    for i in range(1, len(tournament)) :
        current_fitness = fitness(tournament[i])
        if current_fitness > max_fitness :
            max_fitness = current_fitness
            max_i = i

    return tournament[max_i]

def select_parents(population) :
    return [tournament_select(population) for _ in range(POPULATION_SIZE)]

def crossover(a_genome, b_genome) :
    
    if uniform(0, 1) < CROSSOVER_RATE :
        
        mid_point = randint(0, len(a_genome) - 1)

        c_genome = a_genome[:mid_point] + b_genome[mid_point:]
        d_genome = b_genome[:mid_point] + a_genome[mid_point:]

        return c_genome, d_genome
    
    else :

        return a_genome, b_genome
    
def mutate(genome) :
    for i in range(len(genome)) :
        if uniform(0, 1) < MUTATION_RATE :
            genome[i] = randint(0, NUM_GROUPS - 1)

def evolve(population) :

    breeders = select_parents(population)

    new_population = list()

    for _ in range(POPULATION_SIZE) :
        new_population.append(choice(crossover(choice(breeders), choice(breeders))))

    for i in range(POPULATION_SIZE) :
        mutate(new_population[i])

    return new_population

    

def max_fitness(population) :
    
    max_fitness = fitness(population[0])

    for i in range(1, POPULATION_SIZE) :
        
        current_fitness = fitness(population[i])

        if current_fitness > max_fitness :
            max_fitness = current_fitness

    return max_fitness



population = [[randint(0, NUM_GROUPS - 1) for _ in range(len(KEYS))] for _ in range(POPULATION_SIZE)]

for i in range(NUM_GENERATIONS) :

    print(f'Generation {i + 1}. Fitness: {max_fitness(population)}')

    population = evolve(population)

