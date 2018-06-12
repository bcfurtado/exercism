
def distance(dna, dna_mutante):
    return sum([1 for x,y in zip(dna,dna_mutante) if x != y])

    
