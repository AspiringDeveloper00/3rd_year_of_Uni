import random
import tkinter
#user gives the letter
choice=input('Choose letter: K or T?')

T='10101010001000000000000010000000000000100000000000001000000000000010000000000'
K='10000000000010100000000010001000000010000010000000001000100000000000101000000'

t=False
if choice== 'T':
    t=True
    letter=T
elif choice=='K':
    t=True
    letter=K
else:
    print("Please type only K or T")

# Number of individuals in each generation/the population
pop=200
#valid genes
genes='01'

#class representing individual in population
class Individual(object):

    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness =self.calc_fitness()

    @classmethod
    #create random genes for mutation
    def mutated_genes(self):
        global genes
        gene= random.choice(genes)
        return gene

    @classmethod
    #create chromosome or string of genes
    def create_gnome(self):
        global letter
        gnome_len=len(letter)
        return [self.mutated_genes() for _ in range(gnome_len)]

    #Perform mating and produce new offspring
    def mate(self, par2):
        # chromosome for offspring
        child_chromosome= []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            #create random probability
            prob = random.random()

            # if prob is less than  0.45 insert gene from parent1
            if prob<0.45:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90 insert gene from parent2
            elif prob<0.90:
                child_chromosome.append(gp2)
            #otherwise insert random gene(mutate) for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())
        #create new Individual(offspring) using generated chromosome for offspring
        return Individual(child_chromosome)

    #calculate fittness score(it is the number of characters in string which differ from target string).
    def calc_fitness(self):
        global letter
        fitness=0
        #loop simultaneously and check the differences between the 2 strings(individual,target)
        for gs, gt in zip(self.chromosome,letter):
            #for every different element fitness increases
            if gs != gt: fitness+=1
        return fitness
    #shows in cmd the process that the genetic algorithm follows
    def grid_proccess(str, k):

        for i in range(len(str)):
            if i % k == 0:
                sub = str[i:i + k]
                lst = []
                for j in sub:
                    lst.append(j)
                print(' '.join(lst))

    #shows the final result in grid
    def grid_like(str):

        master=tkinter.Tk()
        master.title("Αποτέλεσμα Γενετικού Αλγορίθμου")
        master.geometry("469x616")
        c=0
        for i in range(11):
            for j in range(7):

                if str[c]=='1':
                    button=tkinter.Button(master,bg='dark blue')
                    button.grid(row=i,column=j,ipadx=28,ipady=15)
                else:
                    button=tkinter.Button(master,bg='white')
                    button.grid(row=i,column=j,ipadx=28,ipady=15)
                c=c+1

        master.mainloop()

#driver code
def main():
    global pop

    #current Generation
    generation=1
    found=False
    population = []
    # if the user gave T or K:
    if t:
        #create initial population
        for _ in range(pop):
            gnome= Individual.create_gnome()
            population.append(Individual(gnome))

        while not found :
            #sort the population in increasing order of fitness score
            population = sorted(population, key= lambda x: x.fitness)

            #if the individual having lowest fitness score is 0 then we know that
            # we have reached to the target and break the loop
            if population[0].fitness <=0:
                found = True
                break

            #otherwise generate new offspring for new generation
            new_generation=[]

            #perform elitism ,that mean 10% of fittest population goes to the next Generation
            temp= int((10*pop)/100)
            new_generation.extend(population[:temp])

            #from 50% of fitness population , individuals wil mate to produce offspring
            temp= int((90*pop)/100)
            for _ in range (temp):
                parent1=random.choice(population[:50])
                parent2=random.choice(population[:50])
                child = parent1.mate(parent2)
                new_generation.append(child)


            population= new_generation

            print("Generation: {}\tFitness: {}\t".
                  format(generation,
                         population[0].fitness,
                         Individual.grid_proccess("".join(population[0].chromosome), 7)))

            generation+=1

        print(Individual.grid_like("".join(population[0].chromosome)))

if __name__=='__main__':
        main()
