from string import maketrans

def to_rna(dna):
    return dna.translate(maketrans('GCTA', 'CGAU'))


