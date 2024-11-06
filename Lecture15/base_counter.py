def base_counter(DNA,proportion=0.2):
    DNA_length=len(DNA)
    undetermined_bases=''.join([base for base in DNA if base not in 'ATGC'])
    undetermined_bases_length=len(undetermined_bases)
    undetermined_bases_proportion=undetermined_bases_length/DNA_length
    if undetermined_bases_proportion > proportion:
        return True
    else:
        return False

assert base_counter("ATCGNNAGTCXYZZ")==True